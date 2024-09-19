import os
from typing import List, Optional

import numpy as np
import torch
import uvicorn
from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import AutoModelForSequenceClassification, AutoTokenizer

# # Load tokenizer và model
checkpoint = "mr4/phobert-base-vi-sentiment-analysis"
tokenizer = AutoTokenizer.from_pretrained(
    checkpoint, clean_up_tokenization_spaces=True
)
model = AutoModelForSequenceClassification.from_pretrained(checkpoint)

# Initialize FastAPI app
app = FastAPI(title="Sentiment Analysis API")

# Define health and prediction routes based on environment variables or defaults
AIP_HEALTH_ROUTE = os.environ.get("AIP_HEALTH_ROUTE", "/health")
AIP_PREDICT_ROUTE = os.environ.get("AIP_PREDICT_ROUTE", "/predict")


# Pydantic models for prediction results
class Prediction(BaseModel):
    sentiment: str
    confidence: Optional[float]


class Predictions(BaseModel):
    predictions: List[Prediction]


# Health check route
@app.get(AIP_HEALTH_ROUTE, status_code=200)
async def health():
    return {"health": "ok"}


# Prediction route to handle batch requests
@app.post(
    AIP_PREDICT_ROUTE,
    response_model=Predictions,
    response_model_exclude_unset=True,
)
async def predict(request: Request):
    # Extract the JSON body from the request
    body = await request.json()

    # Extract the instances (texts) from the request
    instances = [x["text"] for x in body["instances"]]

    # Tokenize văn bản cho mô hình
    tf_batch = tokenizer(
        instances,
        # max_length=128,
        padding=True,
        truncation=True,
        return_tensors="pt",  # Chuyển thành tensor Pytorch
    )

    # Lấy kết quả dự đoán từ mô hình
    with torch.no_grad():
        tf_outputs = model(**tf_batch)

    # Áp dụng hàm softmax để lấy xác suất (điểm tự tin)
    softmax = torch.nn.functional.softmax(tf_outputs.logits, dim=-1).numpy()

    # Tìm chỉ số của xác suất cao nhất (dự đoán cảm xúc)
    indices = np.argmax(softmax, axis=-1)

    # Lấy giá trị confidence cao nhất cho mỗi dự đoán
    confidences = np.max(softmax, axis=-1)

    # Prepare the output
    outputs = []
    for index, confidence in zip(indices, confidences):
        sentiment = model.config.id2label[index]
        outputs.append(
            Prediction(sentiment=sentiment, confidence=float(confidence))
        )

    # Return the predictions
    return Predictions(predictions=outputs)


# Main function to run the FastAPI app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

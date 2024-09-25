import os
from typing import List, Optional

import uvicorn  # noqa: F401
from fastapi import FastAPI, Request
from pydantic import BaseModel

# import torch  # noqa: F401
# import numpy as np  # noqa: F401
# # Load tokenizer và model
# storage_path = "models/"
# tokenizer = AutoTokenizer.from_pretrained(storage_path + "tokenizer/")
# model = AutoModelForSequenceClassification.from_pretrained(
#     storage_path + "model/"
# )

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


def get_prediction(instances):
    res = []
    for text in instances:
        if len(text) > 30:
            res.append(Prediction(sentiment="Tích cực", confidence=0.99))

        elif len(text) > 10:
            res.append(Prediction(sentiment="Tiêu cực", confidence=0.9))
        else:
            res.append(Prediction(sentiment="Trung lập", confidence=0.8))
    return Predictions(predictions=res)


# def get_prediction_confidence(instances):
#     tf_batch = tokenizer(
#         instances,
#         # max_length=128,
#         padding=True,
#         truncation=True,
#         return_tensors="pt",  # Chuyển thành tensor Pytorch
#     )

#     # Lấy kết quả dự đoán từ mô hình
#     with torch.no_grad():
#         tf_outputs = model(**tf_batch)

#     # Áp dụng hàm softmax để lấy xác suất (điểm tự tin)
#     softmax = torch.nn.functional.softmax(tf_outputs.logits, dim=-1).numpy()

#     # Tìm chỉ số của xác suất cao nhất (dự đoán cảm xúc)
#     indices = np.argmax(softmax, axis=-1)

#     # Lấy giá trị confidence cao nhất cho mỗi dự đoán
#     confidences = np.max(softmax, axis=-1)

#     # Prepare the output
#     outputs = []
#     for index, confidence in zip(indices, confidences):
#         sentiment = model.config.id2label[index]
#         outputs.append(
#             Prediction(sentiment=sentiment, confidence=float(confidence))
#         )
#     return Predictions(predictions=outputs)


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

    output = get_prediction(instances)

    # Return the predictions
    return output


# Main function to run the FastAPI app
if __name__ == "__main__":
    # "filename:fastapi_app" = "main:app"
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
    # body = {
    #     "instances": [
    #         {"text": "Test Trung lập"},
    #         {"text": "test Tích cực, ket qua tra ve Tích cực"},
    #         {"text": "Tiêu cực"},
    #     ]
    # }
    # instances = [x["text"] for x in body["instances"]]
    # print(get_prediction(instances))

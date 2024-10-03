import os
from typing import List, Optional

import joblib
import uvicorn
from fastapi import FastAPI, HTTPException, Request
from model import SimpleSentimentModel  # noqa: F401
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI(title="Sentiment Analysis API")

# Load the model with a safe file path
model_path = os.path.join("models", "model.pkl")
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at {model_path}")

# Load the model, making sure SimpleSentimentModel is already imported
model = joblib.load(model_path)


# Pydantic models for prediction results
class Prediction(BaseModel):
    sentiment: str
    confidence: Optional[float]


class Predictions(BaseModel):
    predictions: List[Prediction]


# Function to process batch predictions
def get_prediction(instances):
    res = []
    for text in instances:
        sentiment, confidence = model.predict(text)
        res.append(Prediction(sentiment=sentiment, confidence=confidence))
    return Predictions(predictions=res)


# Health check route
@app.get("/health", status_code=200)
async def health():
    return {"health": "ok"}


# Prediction route to handle batch requests
@app.post(
    "/predict",
    response_model=Predictions,
    response_model_exclude_unset=True,
)
async def predict(request: Request):
    # Extract the JSON body from the request
    body = await request.json()

    # Validate the request body
    if "instances" not in body or not isinstance(body["instances"], list):
        raise HTTPException(
            status_code=400,
            detail="Invalid input format. 'instances' should be a list of texts.",
        )

    # Extract the instances (texts) from the request
    instances = [x["text"] for x in body["instances"]]

    # Get predictions
    output = get_prediction(instances)

    # Return the predictions
    return output

# Main function to run the FastAPI app
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080)

import pickle
from typing import List, Optional

import uvicorn  # noqa: F401
from fastapi import FastAPI, Request
from model_training import SimpleSentimentModel  # noqa: F401
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI(title="Sentiment Analysis API")
with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)


# Pydantic models for prediction results
class Prediction(BaseModel):
    sentiment: str
    confidence: Optional[float]


class Predictions(BaseModel):
    predictions: List[Prediction]


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

    # Extract the instances (texts) from the request
    instances = [x["text"] for x in body["instances"]]

    output = get_prediction(instances)
    # Return the predictions
    return output


# Main function to run the FastAPI app
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)

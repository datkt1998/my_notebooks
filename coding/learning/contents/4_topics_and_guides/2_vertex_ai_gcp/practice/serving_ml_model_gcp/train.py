import os

import joblib
from model import SimpleSentimentModel  # Ensure this import is correct

if __name__ == "__main__":
    # Create an instance of the model
    model = SimpleSentimentModel()

    # Create directory if it doesn't exist
    model_dir = "models"
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    # Save the model using joblib, ensuring correct context
    joblib.dump(model, os.path.join(model_dir, "model.pkl"))
    print("Model saved successfully!")

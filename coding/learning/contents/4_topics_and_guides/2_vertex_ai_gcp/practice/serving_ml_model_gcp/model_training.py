import pickle
import random

from sklearn.base import BaseEstimator, TransformerMixin


class SimpleSentimentModel(BaseEstimator, TransformerMixin):
    negative_length_threshold = 10
    positive_length_threshold = 30
    negative_ls = ["tiêu cực", "xấu", "tệ", "negative"]
    positive_ls = ["tích cực", "thích", "positive"]

    def __init__(self):
        pass

    def predict(self, text):
        text_lower = text.lower()
        if any(word in text_lower for word in self.negative_ls):
            return "negative", random.randrange(90, 100, step=1) / 100
        elif any(word in text_lower for word in self.positive_ls):
            return "positive", random.randrange(90, 100, step=1) / 100
        elif len(text) <= self.negative_length_threshold:
            return "negative", random.randrange(70, 90, step=1) / 100
        elif len(text) >= self.positive_length_threshold:
            return "positive", random.randrange(70, 90, step=1) / 100
        else:
            return "neutral", random.randrange(70, 95, step=1) / 100


if __name__ == "__main__":
    model = SimpleSentimentModel()
    with open("models/model.pkl", "wb") as f:
        pickle.dump(model, f)

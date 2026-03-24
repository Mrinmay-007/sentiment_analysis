import pickle

MODEL_PATH = "models/sentiment_analysis_model.pkl"

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

def predict_sentiment(text: str):
    result = model.predict([text])
    return result[0]
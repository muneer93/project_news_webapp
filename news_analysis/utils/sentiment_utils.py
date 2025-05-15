# sentiment_utils.py
from transformers import pipeline

# Load model once (this takes time, so do it globally)
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text):
    if not text.strip():
        return None
    result = sentiment_pipeline(text[:512])  # Truncate long text to 512 tokens
    return result[0]  # e.g. {'label': 'POSITIVE', 'score': 0.99}

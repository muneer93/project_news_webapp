from transformers import pipeline
from collections import Counter

model_name = "distilbert-base-uncased-finetuned-sst-2-english"
sentiment_pipeline = pipeline("sentiment-analysis", model=model_name, tokenizer=model_name)

MAX_TOKENS = 512  # typical max length for distilbert models

def chunk_text_by_tokens(text, tokenizer, max_tokens=MAX_TOKENS):
    inputs = tokenizer(text, return_tensors="pt", truncation=False)
    input_ids = inputs["input_ids"][0]  # tensor of token ids
    chunks = []
    for i in range(0, len(input_ids), max_tokens):
        chunk_ids = input_ids[i:i+max_tokens]
        chunk_text = tokenizer.decode(chunk_ids, skip_special_tokens=True)
        chunks.append(chunk_text)
    return chunks

def analyze_sentiment(text, tokenizer):
    chunks = chunk_text_by_tokens(text, tokenizer)
    results = [sentiment_pipeline(chunk, truncation=True)[0] for chunk in chunks]

    labels = [r['label'] for r in results]
    scores = [r['score'] for r in results]

    most_common_label = Counter(labels).most_common(1)[0][0]
    avg_score = sum(scores) / len(scores)

    return {"label": most_common_label, "average_score": avg_score}

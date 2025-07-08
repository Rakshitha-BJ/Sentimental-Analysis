from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

MODEL_NAME = "cardiffnlp/twitter-xlm-roberta-base-sentiment"

# ✅ Use the slow tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_fast=False)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
labels = ['Negative', 'Neutral', 'Positive']

def classify_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=1)
    sentiment = labels[probs.argmax()]
    return sentiment, probs.tolist()[0]

import streamlit as st
import torch
from transformers import BertTokenizer, BertForSequenceClassification

model_name = "nlptown/bert-base-multilingual-uncased-sentiment"

tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)

def predict_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

    with torch.no_grad():
        outputs = model(**inputs)

    return torch.argmax(outputs.logits).item() + 1

st.title("BERT Sentiment Analyzer")

text = st.text_area("Enter text")

if st.button("Analyze"):
    score = predict_sentiment(text)
    st.write(f"Sentiment Rating: {score}/5")

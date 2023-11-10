import streamlit as st
from transformers import pipeline

# Load sentiment analysis pipeline
summarizer = pipeline("summarization")

# Streamlit UI
st.title("Text Summarization App")
text = st.text_area("Enter text:")
if st.button("Analyze"):
    if text:
        summary = summarizer(text, max_length=150, do_sample=False)
        gist = summary[0]['summary_text']
        st.write(f"Summary: {gist}")

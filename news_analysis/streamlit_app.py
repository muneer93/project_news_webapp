import warnings
warnings.filterwarnings("ignore", category=UserWarning) # For production

import streamlit as st
from utils.sentiment_utils import analyze_sentiment


st.title("YouTube Comment Sentiment")

comment = st.text_area("Paste a comment:")
if st.button("Analyze"):
    result = analyze_sentiment(comment)
    if result:
        st.write(f"**Sentiment**: {result['label']} ({round(result['score'] * 100, 2)}%)")
    else:
        st.write("Please enter some text.")
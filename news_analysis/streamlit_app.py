import streamlit as st
from utils.youtube_utils import fetch_video_data
from utils.sentiment_utils import analyze_sentiment
from utils.bias_utils import analyze_bias
from transformers import AutoTokenizer, pipeline

sentiment_pipeline = pipeline("sentiment-analysis")
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

def main():
    st.title("YouTube Video Bias & Sentiment Analyzer")

    video_url = st.text_input("Enter YouTube Video URL:")

    # Add a button so fetching happens only on click
    if st.button("Fetch Video Data"):
        if not video_url:
            st.error("Please enter a YouTube video URL.")
            return

        st.info("Fetching video data...")
        video_data = fetch_video_data(video_url)

        if not video_data:
            st.error("Failed to fetch video data. Please check the URL and try again.")
            return

        metadata = video_data.get("metadata", {})
        transcript = video_data.get("transcript")
        # comments = video_data.get("comments")  # You can add this if needed

        st.subheader("Video Information")
        st.write(f"**Title:** {metadata.get('title', 'N/A')}")
        st.write(f"**Channel:** {metadata.get('channel_title', 'N/A')}")
        st.write(f"**Published At:** {metadata.get('published_at', 'N/A')}")
        st.write(f"**Views:** {metadata.get('view_count', 'N/A')}")

        if transcript:
            st.subheader("Caption Text (Preview)")
            st.write(transcript[:500] + "...")  # Show preview

            # Analyze Sentiment
            sentiment = analyze_sentiment(transcript, tokenizer)
            st.subheader("Sentiment Analysis")
            st.write(sentiment)

            # Calculate Bias Score
            bias = analyze_bias(transcript)
            st.subheader("Bias Score")
            st.write(bias)
        else:
            st.warning("No captions available for this video.")

if __name__ == "__main__":
    main()

import streamlit as st
import pandas as pd
import plotly.express as px

from utils.yt_utils import extract_video_id, get_comments
from utils.translate_utils import translate_to_english
from utils.sentiment_model import classify_sentiment

st.set_page_config(page_title="YouTube Sentiment Analyzer", layout="wide")
st.title("🎥 YouTube Comment Sentiment Analyzer")

# API Key Input
api_key = st.text_input("🔑 Enter your YouTube Data API v3 Key", type="password")

# Video URL Input
video_url = st.text_input("📺 Enter YouTube Video URL")

if st.button("Analyze Comments"):
    if not video_url or not api_key:
        st.warning("Please provide both API Key and Video URL.")
    else:
        with st.spinner("Fetching and analyzing comments..."):
            video_id = extract_video_id(video_url)
            if not video_id:
                st.error("❌ Invalid YouTube URL")
            else:
                comments = get_comments(api_key, video_id)
                if not comments:
                    st.error("❌ No comments found or API error.")
                else:
                    data = []
                    for c in comments:
                        original = c['text']
                        translated = translate_to_english(original)
                        sentiment, prob = classify_sentiment(translated)
                        data.append({
                            'Author': c['author'],
                            'Comment': original,
                            'Translated': translated,
                            'Sentiment': sentiment,
                            'Likes': c['likes']
                        })
                    df = pd.DataFrame(data)

                    st.subheader("📊 Sentiment Breakdown")
                    st.plotly_chart(
                        px.pie(df, names='Sentiment', title="Sentiment Distribution", hole=0.4),
                        use_container_width=True
                    )

                    st.plotly_chart(
                        px.histogram(df, x='Sentiment', color='Sentiment', title="Sentiment Histogram"),
                        use_container_width=True
                    )

                    st.subheader("🔥 Most Liked Comment")
                    top_comment = df.sort_values("Likes", ascending=False).iloc[0]
                    st.info(f"💬 \"{top_comment['Comment']}\" — 👍 {top_comment['Likes']} likes")

                    st.subheader("🗃 All Comments Table")
                    st.dataframe(df)

                    csv = df.to_csv(index=False).encode('utf-8')
                    st.download_button("⬇ Download CSV", csv, "sentiment_analysis.csv", "text/csv")


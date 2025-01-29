import streamlit as st
import pandas as pd
import altair as alt

st.title("Real-Time Threads Sentiment Analysis")

# Load data
data = pd.read_csv("threads_posts.csv")

# Sentiment Distribution
st.subheader("Sentiment Distribution")
sentiment_counts = data["sentiment"].value_counts()
st.bar_chart(sentiment_counts)

# Sentiment Trend Over Time
st.subheader("Sentiment Trend Over Time")
data["timestamp"] = pd.to_datetime(data["timestamp"])
trend = data.groupby([pd.Grouper(key="timestamp", freq="1min"), "sentiment"]).size().reset_index(name="count")
chart = alt.Chart(trend).mark_line().encode(
    x="timestamp:T",
    y="count:Q",
    color="sentiment:N"
)
st.altair_chart(chart, use_container_width=True)

# Display Sample Posts
st.subheader("Sample Threads Posts")
st.write(data.tail(10))

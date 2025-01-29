from kafka import KafkaConsumer
from textblob import TextBlob
import pandas as pd

# Kafka Configuration
KAFKA_TOPIC = "threads-stream"
KAFKA_SERVER = "localhost:9092"

# Consumer Setup
consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_SERVER, value_deserializer=lambda x: json.loads(x.decode("utf-8")))

data = []

for message in consumer:
    post = message.value
    sentiment = TextBlob(post["text"]).sentiment.polarity
    sentiment_label = "Positive" if sentiment > 0 else "Negative" if sentiment < 0 else "Neutral"
    data.append({"text": post["text"], "sentiment": sentiment_label, "timestamp": post["created_at"]})
    print(data[-1])

    # Save data to a CSV (or database)
    pd.DataFrame(data).to_csv("threads_posts.csv", index=False)

from threads import Threads
import json
from kafka import KafkaProducer

# Kafka Configuration
KAFKA_TOPIC = "threads-stream"
KAFKA_SERVER = "localhost:9092"
producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER, value_serializer=lambda v: json.dumps(v).encode("utf-8"))

# Initialize Threads Client
threads = Threads()

# Fetch posts by hashtag (replace this with available methods)
def fetch_threads_posts(hashtag):
    posts = threads.search_hashtag(hashtag)  # Example method (check documentation)
    for post in posts:
        data = {
            "text": post["caption"],  # Adapt to match the actual API response
            "created_at": post["timestamp"]  # Adjust field names if necessary
        }
        producer.send(KAFKA_TOPIC, data)
        print(f"Post sent: {data}")

# Call the function
fetch_threads_posts("ai")

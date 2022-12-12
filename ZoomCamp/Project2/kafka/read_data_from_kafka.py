import json
import time
from kafka import KafkaConsumer
from kafka import KafkaProducer

# topic
STOCKS_DATA_KAFKA_TOPIC = "stock_data"
TWITTER_COUNTS_KAFKA_TOPIC = "twitter_counts"
TWITTER_TWEETS_KAFKA_TOPIC = "twitter_tweets"

def read_from_kafka(which_data, topic):
    # reads kafka topic
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers="localhost:9092"
    )
    print(f'Listening to {which_data} data...')

    while True:
        for number, message in enumerate(consumer):
            print(f'Reading row {number}...')
            consumed_message = json.loads(message.value.decode())
            print(consumed_message)

# read_from_kafka('stock data', STOCKS_DATA_KAFKA_TOPIC)
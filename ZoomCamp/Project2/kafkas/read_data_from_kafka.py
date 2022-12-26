from json import loads
import pandas as pd
from kafka import KafkaConsumer
from kafka import KafkaAdminClient

# import time

# topic
# STOCKS_DATA_KAFKA_TOPIC = "stock_data"
# TWITTER_COUNTS_KAFKA_TOPIC = "twitter_counts"
# TWITTER_TWEETS_KAFKA_TOPIC = "twitter_tweets"

def read_from_kafka(which_data, topic):
    # reads kafka topic
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers="localhost:9092",
        auto_offset_reset='earliest', # earliest reads all data from beginning
        enable_auto_commit=True,
        group_id='consumer.group.1',
        value_deserializer=lambda x: loads(x.decode("utf-8")),
        consumer_timeout_ms=1000
    )
    print(f'Listening to {which_data} data...')

    data = []
    for number, message in enumerate(consumer):
        print(f'Reading row {number}...')
        data.append(message.value)
    print('Finished reading stream.')

    # # clear kafka topic
    # admin_client = KafkaAdminClient(bootstrap_servers='localhost:9092')
    # admin_client.delete_topics(topics=[topic])

    return pd.DataFrame(data)

# read_from_kafka('stock data', STOCKS_DATA_KAFKA_TOPIC)
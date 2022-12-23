from json import dumps
from kafka import KafkaProducer

''' import functions from other files '''
import sys, os
sys.path.insert(0, os.path.abspath(os.getcwd()))
from data.stocks_data import all_stock_pull
from data.twitter_data import counts, response

# topic
STOCKS_DATA_KAFKA_TOPIC = "stock_data"
TWITTER_COUNTS_KAFKA_TOPIC = "twitter_counts"
TWITTER_TWEETS_KAFKA_TOPIC = "twitter_tweets"

# function to write data to the kafka producer
def write_to_kafka(which_data, dataframe, topic):
    # producer writes to kafka
    producer = KafkaProducer(
        bootstrap_servers="localhost:9092",
        value_serializer=lambda x: dumps(x).encode("utf-8")
    )
    print(f'Going to be writing in {which_data} data...')

    # get df and make it dictionary
    data_dict = dataframe.to_dict('records')

    # iterate through df and send to producer
    for number, row in enumerate(data_dict):
        producer.send(topic,value=row)
        print(f'Sent row {number}')
    print('Sent all data.')
    producer.flush()

write_to_kafka('stocks data', all_stock_pull('1wk'), STOCKS_DATA_KAFKA_TOPIC)
# write_to_kafka('twitter tweets', response('AAPL'), TWITTER_TWEETS_KAFKA_TOPIC)
# write_to_kafka('twitter counts', counts('AAPL', 'hour'), TWITTER_COUNTS_KAFKA_TOPIC)
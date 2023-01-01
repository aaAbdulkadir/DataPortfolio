from json import dumps
from kafka import KafkaProducer
import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import datetime

# list of stocks
list_of_stocks = pd.read_html('https://en.wikipedia.org/wiki/Nasdaq-100')[4]['Ticker'].to_list()
list_of_stocks = [f'${stock}' for stock in list_of_stocks]

# producer writes to kafka
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    # batch_size=131072, # process more data
    value_serializer=lambda x: dumps(x).encode("utf-8")
)

for stock in list_of_stocks:
    limit = 0
    for tweet in sntwitter.TwitterSearchScraper(stock).get_items():
        # get 50 tweets per stock with date, username and tweet
        if limit == 20:
            break
        else:
            data = {
                "date": datetime.strftime(tweet.date, '%Y-%m-%d %H:%M:%S'),
                "username": tweet.user.username,
                "tweet": tweet.content,
                "cashtag": stock
            }
            producer.send(
                topic="stock_tweets",
                value=data
            )
            limit += 1
    print(f'{stock} done')

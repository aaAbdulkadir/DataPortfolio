import sys, os
sys.path.insert(0, os.path.abspath(os.getcwd()))
from kafkas.write_data_to_kafka import write_to_kafka
from kafkas.read_data_from_kafka import read_from_kafka
from data.stocks_data import all_stock_pull
from data.twitter_data import counts, response
import time
from datetime import datetime
import pandas as pd

from flask import Flask, render_template

# topic
STOCKS_DATA_KAFKA_TOPIC = "stock_data"
TWITTER_COUNTS_KAFKA_TOPIC = "twitter_counts"
TWITTER_TWEETS_KAFKA_TOPIC = "twitter_tweets"

write_to_kafka('stocks data', all_stock_pull('1wk'), STOCKS_DATA_KAFKA_TOPIC)
x = read_from_kafka('stock data', STOCKS_DATA_KAFKA_TOPIC)
html_table = x.head().to_html()

app = Flask(__name__)

@app.route('/')
def data():
    return render_template('flasktest/templates/data.html', table=html_table)

if __name__ == '__main__':
    app.run()
    time.sleep(30)
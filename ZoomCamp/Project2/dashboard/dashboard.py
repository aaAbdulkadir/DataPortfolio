import streamlit as st
import sys, os
sys.path.insert(0, os.path.abspath(os.getcwd()))
from kafkas.write_data_to_kafka import write_to_kafka
from kafkas.read_data_from_kafka import read_from_kafka
from data.stocks_data import all_stock_pull
from data.twitter_data import counts, response
from streamlit_autorefresh import st_autorefresh
import time
from datetime import datetime

# topic
STOCKS_DATA_KAFKA_TOPIC = "stock_data"
TWITTER_COUNTS_KAFKA_TOPIC = "twitter_counts"
TWITTER_TWEETS_KAFKA_TOPIC = "twitter_tweets"

# @st.cache

st_autorefresh(interval=10000, key="fizzbuzzcounter")

# st.set_page_config(
#     page_title="STOCK-TWITTER ANALYTICS",
#     layout="centered",
#     initial_sidebar_state="expanded",
# )

# title
st.markdown("<h1 style='text-align: center;'>NASDAQ 100 Twitter Dashboard</h1>", unsafe_allow_html=True)

# date right now
now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
st.write('')
st.write(f'Last update: {now}')

write_to_kafka('stocks data', all_stock_pull('1wk'), STOCKS_DATA_KAFKA_TOPIC)
x = read_from_kafka('stock data', STOCKS_DATA_KAFKA_TOPIC)
st.write(x.head())

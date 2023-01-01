from json import loads
import pandas as pd
from kafka import KafkaConsumer
import streamlit as st
import time

# initialise consumer to read in kafka data
consumer = KafkaConsumer(
    "stock_tweets",
    bootstrap_servers="localhost:9092",
    auto_offset_reset='earliest', # earliest reads all data from beginning
    enable_auto_commit=True,
    group_id='consumer_group_1',
    value_deserializer=lambda x: loads(x.decode("utf-8")),
    session_timeout_ms=30000 # Set session timeout to 30 seconds
    # consumer_timeout_ms=1000
)

# streamlit page config
st.set_page_config(
    page_title="Tweets",
    layout="centered",
    initial_sidebar_state="expanded",
)

# title
st.markdown("<h1 style='text-align: center;'>Tweets</h1>", unsafe_allow_html=True)

# styling of tweets
def twitter_style(username, tweet, date):
    if '\n' in tweet:
        tweet = tweet.replace('\n', '<br>')
    return f"""
            <p style='background-color: #1DA1F2;
                font-size: 14px;
                font-family: Arial, Helvetica, sans-serif;
                color: white;
                padding-top: 20px;
                padding-right: 80px;
                padding-bottom: 20px;
                padding-left: 80px;
                border-radius: 10px;'>@{username}: <br> <br> \"{tweet}\" <br> <br> Created at:{date}</p>
            """

# stock list
list_of_stocks = pd.read_html('https://en.wikipedia.org/wiki/Nasdaq-100')[4]['Ticker'].to_list()
list_of_stocks = [f'${stock}' for stock in list_of_stocks]
stock_selection = st.selectbox(
    'Select the stock you would like to see tweets for',
    list_of_stocks)

with st.empty():
    for message in consumer:
        if (message.value)['cashtag'] == stock_selection:
            print(message.value)
            st.markdown(twitter_style((message.value)['username'], (message.value)['tweet'], (message.value)['date']), unsafe_allow_html=True)
            time.sleep(3)
        else:
            st.write('Data loading...')


# while True:
#     for message in consumer:
#         st.markdown(twitter_style(message['username'], message['tweet'], message['date']), unsafe_allow_html=True)
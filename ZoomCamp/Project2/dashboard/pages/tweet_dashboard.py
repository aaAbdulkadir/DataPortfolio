import streamlit as st
import pandas as pd
import sys, os
sys.path.insert(0, os.path.abspath(os.getcwd()))
from data.twitter_data import response
from kafkas.read_data_from_kafka import read_from_kafka
from kafkas.write_data_to_kafka import write_to_kafka
from streamlit_autorefresh import st_autorefresh
import time

# @st.cache
st.set_page_config(
    page_title="Tweets",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.write('')

# title
st.markdown("<h1 style='text-align: center;'>Tweets</h1>", unsafe_allow_html=True)

# styling of tweets
def twitter_style(username, text, date):
    if '\n' in text:
        text = text.replace('\n', '<br>')
    return f"""
            <p style='background-color: #1DA1F2;
                font-size: 14px;
                font-family: Arial, Helvetica, sans-serif;
                color: white;
                padding-top: 20px;
                padding-right: 80px;
                padding-bottom: 20px;
                padding-left: 80px;
                border-radius: 10px;'>@{username}: <br> <br> \"{text}\" <br> <br> Created at:{date}</p>
            """

# stock list
list_of_stocks = pd.read_html('https://en.wikipedia.org/wiki/Nasdaq-100')[4]['Ticker'].to_list()
stock_selection = st.selectbox(
    'Select the stocks you would like to see tweets for',
    list_of_stocks)

# tweets
write_to_kafka('tweets', response(stock_selection), 'tweets2')
df = read_from_kafka('twitter tweets', 'tweets2')
for index, row in df.iterrows():
    st.markdown(twitter_style(row['username'], row['text'], row['created_at']), unsafe_allow_html=True)
    time.sleep(3)



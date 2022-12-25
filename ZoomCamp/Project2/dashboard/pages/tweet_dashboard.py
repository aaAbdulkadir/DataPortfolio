import streamlit as st
import pandas as pd
import sys, os
sys.path.insert(0, os.path.abspath(os.getcwd()))
from data.twitter_data import response
from kafkas.read_data_from_kafka import read_from_kafka
from kafkas.write_data_to_kafka import write_to_kafka
import time

# @st.cache
st.set_page_config(
    page_title="Twwets",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.write('')

# title
st.markdown("<h1 style='text-align: center;'>Tweets</h1>", unsafe_allow_html=True)

# stock list
list_of_stocks = pd.read_html('https://en.wikipedia.org/wiki/Nasdaq-100')[4]['Ticker'].to_list()
stock_selection = st.selectbox(
    'Select the stocks you would like to see tweets for',
    list_of_stocks)

# tweets
while True:
    write_to_kafka('tweets', response(stock_selection), 'tweets')
    df = read_from_kafka('twitter tweets', 'tweets')
    for index, row in df.iterrows():
        st.write(row['username'], row['text'])
        time.sleep(2)
    st.write('')
    st.write('')


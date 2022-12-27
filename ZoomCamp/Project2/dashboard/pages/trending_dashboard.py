import streamlit as st
import pandas as pd
import sys, os
sys.path.insert(0, os.path.abspath(os.getcwd()))
from data.twitter_data import counts
from kafkas.read_data_from_kafka import read_from_kafka
from kafkas.write_data_to_kafka import write_to_kafka
from streamlit_autorefresh import st_autorefresh
import time
import plotly.express as px

# stock list
list_of_stocks = pd.read_html('https://en.wikipedia.org/wiki/Nasdaq-100')[4]['Ticker'].to_list()
stock_selection = st.selectbox(
    'Select the stock you would like to see tweet counts of',
    list_of_stocks)

tweet_count = counts(stock_selection, 'day')
fig = px.line(
        tweet_count,
        x="end", 
        y="tweet_count", 
    )
fig.update_layout(title_text='Tweet count in the past week', title_x=0.5)
st.plotly_chart(fig)
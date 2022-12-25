import streamlit as st
import sys, os
sys.path.insert(0, os.path.abspath(os.getcwd()))
from data.stocks_data import stock_data
import datetime
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Historical Data",
    layout="centered",
    initial_sidebar_state="expanded",
)

# title
st.markdown("<h1 style='text-align: center;'>Historical Data</h1>", unsafe_allow_html=True)

# date right now
now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
st.write('')
st.write(f'Last update: {now}')
st.write('')
st.write('')

# stock list
list_of_stocks = pd.read_html('https://en.wikipedia.org/wiki/Nasdaq-100')[4]['Ticker'].to_list()
stock_selection = st.multiselect(
    'Select the stocks you would like to monitor',
    list_of_stocks)

# time interval
time_interval = st.selectbox(
    'Select the time interval',
    ['Daily', 'Weekly', 'Monthly'])

if time_interval == 'Daily':
    time_interval = '1d'
elif time_interval == 'Weekly':
    time_interval = '1wk'
elif time_interval == 'Monthly':
    time_interval = '1mo'

# stock dates
max_val = datetime.datetime.now()
min_val= (datetime.date(2000,1,1))

col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input(
        "Start date",
        min_value=min_val, max_value=max_val, value=max_val-datetime.timedelta(days=90))
with col2:
    end_date = st.date_input(
        "End date",
        min_value=min_val, max_value=max_val, value=max_val)


# if logic to make sure to print only when stock is selected
if len(stock_selection) < 1 or start_date == end_date:
    st.caption('Make sure to pick at least one stock with two unique dates.')
else:
    dfs = []
    for stock in stock_selection:
        dfs.append(stock_data(stock, time_interval, start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")))
    final_df = pd.concat(dfs)
    st.write('')

    # visualisation
    fig = px.line(
            final_df,
            x="Date", 
            y="Close", 
            color="Ticker",
            line_group="Ticker", 
        )
    fig.update_layout(title_text='Closing Price vs Time Frame', title_x=0.5)
    st.plotly_chart(fig)

    fig2 = px.line(
            final_df,
            x="Date", 
            y="Volume", 
            color="Ticker",
            line_group="Ticker", 
        )
    fig2.update_layout(title_text='Volume vs Time Frame', title_x=0.5)
    st.plotly_chart(fig2)



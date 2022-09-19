import streamlit as st
from datetime import datetime
import pandas as pd

from cmc import cmc_project

# date today
today = datetime.today()
date = datetime(today.year, today.month, today.day)

# list of dashboards
dashboard_list = ('Home', 'CoinMarketCap', 'Galleria Holdings', 'COVID-19', 'NBA')

# create sidebar
st.sidebar.title("Dashboards")

# choices of dashboards
choice = st.sidebar.selectbox(
    "Choices", dashboard_list
)

# header of page
if choice != dashboard_list[0]:
    st.title(choice)
else:
    st.title('Portfolio Projects')

# direct to selected dashboard
if choice == dashboard_list[0]:
    st.header('Welcome!')
elif choice == dashboard_list[1]:
    cmc_project()
elif choice == dashboard_list[2]:
    st.header('Data Architecture and ETL Pipeline')
elif choice == dashboard_list[3]:
    st.header('ETL Pipeline and Data Analysis')
else:
    st.header('Machine Learing using NBA Data')


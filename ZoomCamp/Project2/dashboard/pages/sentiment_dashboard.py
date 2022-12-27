import streamlit as st
import pandas as pd
import sys, os
sys.path.insert(0, os.path.abspath(os.getcwd()))
from data.twitter_data import response
from kafkas.read_data_from_kafka import read_from_kafka
from kafkas.write_data_to_kafka import write_to_kafka
from streamlit_autorefresh import st_autorefresh
import time
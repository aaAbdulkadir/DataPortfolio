import pandas as pd 
import datetime
from datetime import timedelta
import time

# gets df with stocks in list of stocks
def stock_data(ticker, interval, start, end):
    # split dates up
    start_year, start_month, start_day = int(start.split('-')[0]), int(start.split('-')[1]), int(start.split('-')[2])
    end_year, end_month, end_day = int(end.split('-')[0]),int(end.split('-')[1]), int(end.split('-')[2])

    # period intervals
    period_1 = int(time.mktime(datetime.datetime(start_year, start_month, start_day, 23, 59).timetuple()))
    period_2 = int(time.mktime(datetime.datetime(end_year, end_month, end_day, 23, 59).timetuple()))

    query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period_1}&period2={period_2}&interval={interval}&events=history&includeAdjustedClose=true'

    df = pd.read_csv(query_string)
    df['Ticker'] = ticker

    return df

# intervals: 1d, 1wk, 1mo
def all_stock_pull(interval):
    # get a list of top 100 nasdaq
    list_of_stocks = pd.read_html('https://en.wikipedia.org/wiki/Nasdaq-100')[4]['Symbol'].to_list()

    # get date today
    today = datetime.datetime.now().strftime("%Y-%m-%d")

    # get date one year ago
    last_year = (datetime.datetime.now() - timedelta(days=365)).strftime("%Y-%m-%d")

    # all stocks combined
    dfs = []
    for stock in list_of_stocks:
        dfs.append(stock_data(stock, interval, last_year, today))

    return pd.concat(dfs)

# print(all_stock_pull('1d'))
# print(all_stock_pull('1wk'))
# print(all_stock_pull('1mo'))
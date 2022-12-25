import pandas as pd 
import datetime
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

def concat_stocks(stock_selection, time_interval, start_date, end_date):
    dfs = []
    for stock in stock_selection:
        dfs.append(stock_data(stock, time_interval, start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")))
    return pd.concat(dfs)
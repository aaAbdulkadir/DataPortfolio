import pandas as pd

def transformations():

    # load data
    date = pd.read_csv('../data/cmc/Date.csv')
    perfomrance = pd.read_csv('../data/cmc/Performance.csv')
    Summary = pd.read_csv('../data/cmc/Summary.csv')
    Top90 = pd.read_csv('../data/cmc/Top 90 Day Performance.csv')
    gainers = pd.read_csv('../data/cmc/Top Gainers.csv')
    losers = pd.read_csv('../data/cmc/Top Losers.csv')
    trending = pd.read_csv('../data/cmc/Trnending.csv')

    # make graphs
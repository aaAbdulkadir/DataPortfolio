import pandas as pd

def API_data(api_key, output_file):

    from requests import Request, Session
    from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
    import json

    def cmc_api(url):
        parameters = {
        'start':'1',
        'limit':'5000',
        'convert':'USD'
        }
        headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
        }

        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
            
        # normalize json file into pd
        df = pd.json_normalize(data['data'])

        # put data into df
        df['timestamp'] = pd.to_datetime('now')

        return df

    # top 5000 coins listed  on cmc
    latest_listings = cmc_api('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest')

    useful_columns = ['id', 'name', 'symbol', 'slug', 'num_market_pairs', 'date_added',
        'max_supply', 'circulating_supply', 'total_supply','cmc_rank', 'last_updated',
        'quote.USD.price', 'quote.USD.volume_24h','quote.USD.volume_change_24h', 
        'quote.USD.percent_change_1h', 'quote.USD.percent_change_24h', 'quote.USD.percent_change_7d',
        'quote.USD.percent_change_30d', 'quote.USD.percent_change_60d','quote.USD.percent_change_90d', 
        'quote.USD.market_cap', 'quote.USD.market_cap_dominance', 'quote.USD.fully_diluted_market_cap', 'timestamp']

    df = latest_listings[useful_columns]

    # rename columns
    for col in useful_columns:
        if 'quote' in col:
            new_col = col.split('.')[-1]
            df = df.rename(columns={col:new_col})

    df.to_parquet(output_file)
    print(f'API data succesfully saved in {output_file}')

def bs4_data(output_file):

    from bs4 import BeautifulSoup
    import requests

    # trending (30 coins)
    url = 'https://coinmarketcap.com/trending-cryptocurrencies/'
    website = requests.get(url).content
    soup = BeautifulSoup(website, 'lxml')

    trending = []
    ranks = list(range(1,31))

    for coin in soup.find_all(class_='sc-1eb5slv-0 gGIpIK coin-item-symbol'):
        trending.append(coin.text)

    zip_list = zip(ranks, trending)
    trending_coins = list(zip_list)
    trending_coins = pd.DataFrame(trending_coins, columns=['rank', 'symbol'])
    trending_coins.to_parquet(output_file)
    print(f'bs4 data succesfully saved in {output_file}')

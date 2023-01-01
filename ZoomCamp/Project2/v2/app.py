import snscrape.modules.twitter as sntwitter
import pandas as pd
import time

start_time = time.time()

tweets = []
list_of_stocks = pd.read_html('https://en.wikipedia.org/wiki/Nasdaq-100')[4]['Ticker'].to_list()
list_of_stocks = [f'${stock}' for stock in list_of_stocks]

for stock in list_of_stocks:
    limit = 0
    for tweet in sntwitter.TwitterSearchScraper(stock).get_items():
        # get 50 tweets per stock
        if limit == 50:
            break
        else:
            tweets.append([tweet.date, tweet.user.username, tweet.content, stock])
            limit += 1
    print(f'{stock} done')
        
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet', 'Cashtag'])
print(df)
print ("My program took", time.time() - start_time, "to run")
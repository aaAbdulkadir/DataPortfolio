import os
import tweepy
import time

# API Keys
TWITTER_KEY = os.environ.get("TWITTER_KEY")
TWITTER_SECRET_KEY = os.environ.get("TWITTER_SECRET_KEY")
TWITTER_BEARER_TOKEN = os.environ.get("TWITTER_BEARER_TOKEN")
TWITTER_ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
TWITTER_CLIENT_ID = os.environ.get("TWITTER_CLIENT_ID")
TWITTER_CLIENT_SECRET = os.environ.get("TWITTER_CLIENT_SECRET")

client = tweepy.Client(
    TWITTER_BEARER_TOKEN, 
    TWITTER_KEY, 
    TWITTER_SECRET_KEY, 
    TWITTER_ACCESS_TOKEN, 
    TWITTER_ACCESS_TOKEN_SECRET
    )
    
# queries and filters
topic = '"world cup" worldcup'

# gets the actual tweets with the specific conditions
def response(topic):
    # query by topic, that is not a retweet, in english and in the UK or US
    query = f'{topic} -is:retweet lang:en'
    return client.search_recent_tweets(query=query, max_results=10).data

for tweet in response(topic):
    print(tweet.text)
    print(tweet.created_at)
    print(tweet.id)
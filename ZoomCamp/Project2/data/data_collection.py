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
    
query = 'covid -is:retweet'
tweet_fields = ['created_at', 'lang']
expansions=['author_id']

response = client.search_recent_tweets(query=query, max_results=10)

for tweet in response.data:
    print(tweet.text)

# client = tweepy.Client(
#     TWITTER_BEARER_TOKEN, 
#     TWITTER_KEY, 
#     TWITTER_SECRET_KEY, 
#     TWITTER_ACCESS_TOKEN, 
#     TWITTER_ACCESS_TOKEN_SECRET
#     )
# auth = tweepy.OAuth1UserHandler(
#     TWITTER_KEY, 
#     TWITTER_SECRET_KEY, 
#     TWITTER_ACCESS_TOKEN, 
#     TWITTER_ACCESS_TOKEN_SECRET
#     )
# api = tweepy.API(auth)

# search_terms = ["btc"]

# testers = []

# class MyStream(tweepy.StreamingClient):

#     # This function gets called when the stream is working
#     def on_connect(self):
#         print("Connected")

#     # This function gets called when a tweet passes the stream
#     def on_tweet(self, tweet):
#         # Displaying tweet in console
#         if tweet.referenced_tweets == None:
#             # print(tweet.text)
#             client.like(tweet.id)
#             testers.append(tweet.text)
#             print(tweet.text)
#             print('')


# # Creating Stream object
# stream = MyStream(bearer_token=TWITTER_BEARER_TOKEN)

# for term in search_terms:
#     stream.add_rules(tweepy.StreamRule(term))

# # Starting stream
# stream.filter(tweet_fields=["referenced_tweets"])
import os
import tweepy
import pandas as pd
from textblob import TextBlob

'''
Note: 2 million tweets cap per month for pulling tweets
      No cap on getting the number of tweets 

'''

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

# get a number of recent tweets for the topic: two time intervals: day and hour 
def counts(topic, time_interval):
    query = f'{topic} -is:retweet -is:reply -is:quote lang:en'
    result = client.get_recent_tweets_count(query=query, granularity=time_interval).data
    return pd.DataFrame(result)

# get a df of user and tweet with followers and likes
def response(topic):
    # get data from api
    responses = client.search_recent_tweets(
        query=f'{topic} -is:retweet lang:en -has:hashtags -has:links -has:mentions -has:media -has:images',
        tweet_fields=['created_at', 'public_metrics', 'text'], 
        user_fields=['username', 'public_metrics','location','description'],
        expansions='author_id',
        max_results=10
        )

    # get user details
    user_dict = {}
    for user in responses.includes['users']:
        user_dict[user.id] = {
            'username': user.name,
            'followers': user.public_metrics['followers_count'],
            'tweets': user.public_metrics['tweet_count'],
            'location': user.location
            }

    # get tweets and user details together
    result = []
    for tweet in responses.data:
        author_info = user_dict[tweet.author_id]
        result.append(
            {
                'author_id': tweet.author_id,
                'username': author_info['username'],
                'author_followers': author_info['followers'],
                'author_tweets': author_info['tweets'],
                'author_location': author_info['location'],
                'text': tweet.text,
                'created_at': tweet.created_at,
            }
        )

    df = pd.DataFrame(result)

    # add sentiment
    df['subjectivity'] = df['text'].apply(subjectivity)
    df['polarity'] = df['text'].apply(polarity)
    df['score'] = df['polarity'].apply(score)

    return df

# sentiment analysis using tweets collected
def subjectivity(text):
    return TextBlob(text).sentiment.subjectivity

def polarity(text):
    return TextBlob(text).sentiment.polarity

def score(number):
    if number > 0:
        return 'Positive'
    elif number < 0:
        return 'Negative'
    else:
        return 'Neutral'

# print(counts('stockname', 'day'))
# print(counts('stockname', 'hour'))
# print(response('stockname'))
import tweepy
from textblob import TextBlob

consumer_key = ''
consumer_secret = ''
access_token = 	''
access_token_secret = ''

# Authentication of the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Word that will be used to search Twitter
public_tweets = api.search('AMD')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print('')
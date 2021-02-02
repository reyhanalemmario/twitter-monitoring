#!/usr/bin/env python

import twitter_credentials
from tweepy import OAuthHandler
from tweepy import Stream

# Change this later to os.environ['EnvirontKey']
consumer_key = twitter_credentials.CONSUMER_KEY
consumer_secret = twitter_credentials.CONSUMER_SECRET
access_token = twitter_credentials.ACCESS_TOKEN
access_token_secret = twitter_credentials.ACCESS_TOKEN_SECRET

print(consumer_key)

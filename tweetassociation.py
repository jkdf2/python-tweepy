#!/usr/local/bin/python
import tweepy

#open a file called "keys" with keys and tokens for Twitter separated by newlines
keyFile = open('keys', 'r') 
consumer_key = keyFile.readline().rstrip()
consumer_secret = keyFile.readline().rstrip()
access_token = keyFile.readline().rstrip()
access_token_secret = keyFile.readline().rstrip()
keyFile.close()
print "consumer key: " + consumer_key
print "consumer secret: " + consumer_secret
print "access token: " + access_token
print "access token secret: " + access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
        print tweet.text

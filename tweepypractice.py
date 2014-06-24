#!/usr/local/bin/python
import tweepy #https://github.com/tweepy/tweepy
#tweepy tip: use `print dir(object)` to get more info about an object

#open a file called "keys" with keys and tokens for Twitter separated by newlines
keyFilename = 'keys'
keyFile = open(keyFilename, 'r') 
consumer_key = keyFile.readline().rstrip()
consumer_secret = keyFile.readline().rstrip()
access_token = keyFile.readline().rstrip()
access_token_secret = keyFile.readline().rstrip()
keyFile.close()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

username = ""

#print out each favorite tweet a user has made
for eachFavorite in tweepy.Cursor(api.favorites, id=username).items():
    print eachFavorite.user.screen_name + ": " + eachFavorite.text

#favoriting everything of a particular user
#use create_favorite to favorite
#and destroy_favorite to undo
for eachPost in tweepy.Cursor(api.user_timeline, id=username).items():
    print eachPost.id
    try:
        api.create_favorite(eachPost.id)
    except Exception:
        pass

#print out tweets from specific user
for eachPost in tweepy.Cursor(api.user_timeline, id=username).items(100):
    print eachPost.id
    print eachPost.text

##list all followers of authenticated user
friends = api.followers()
for eachFriend in friends:
    print eachFriend.screen_name

##display homepage tweets of authenticated user
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text

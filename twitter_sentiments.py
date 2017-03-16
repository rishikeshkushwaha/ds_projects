import tweepy
from textblob import *

consumer_key = 'HcRDlcwcMrO87QMV0GoQ973Kv'
consumer_secret = 'WGImy5sFHKNfGbCvPzpB5YtnNbmKZqmdVn4QbS5Z6oGkthsP7F'

access_token = '70615415-rwLzefAqP50hp3GrY9PVfy9oe7DdvEioEP1jFZRmG'
access_token_secret = '3dHxEWN4EqvKQEFxEPHkStNQYhVYohiCVZQ8fsRIzc4h2'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Kejriwal')
l = []
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    l.append(analysis.sentiment)
print(l[0])

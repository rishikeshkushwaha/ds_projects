import tweepy
from textblob import *
import numpy as np
import matplotlib.pyplot as plt

#this is just an experiment to compare latest tweets sentiments on some famous persons
consumer_key = 'HcRDlcwcMrO87QMV0GoQ973Kv'
consumer_secret = 'WGImy5sFHKNfGbCvPzpB5YtnNbmKZqmdVn4QbS5Z6oGkthsP7F'

access_token = '70615415-rwLzefAqP50hp3GrY9PVfy9oe7DdvEioEP1jFZRmG'
access_token_secret = '3dHxEWN4EqvKQEFxEPHkStNQYhVYohiCVZQ8fsRIzc4h2'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#code to plot subjectivity vs polarity
def tweets_plot(s,i):
    public_tweets = api.search(s)
    lx = []
    ly =[]
    for tweet in public_tweets:
    #print(tweet.text)
        analysis = TextBlob(tweet.text)
        lx.append(analysis.sentiment[0])
        ly.append(analysis.sentiment[1])
    plt.subplot((int(str(22)+i)))
    plt.scatter(lx, ly)
    plt.title(s)
    plt.xlabel('polarity')
    plt.axhline(y=0.5,linewidth=0.4, color='r')
    plt.axvline(x=0,linewidth=0.4, color='r')
    plt.ylabel('subjectivity')

people = ['Modi','Trump','Kejriwal','Obama']
i = 1
for s in people:
    tweets_plot(s,str(i))
    i +=1
plt.show()









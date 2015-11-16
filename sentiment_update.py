#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymongo
from pymongo import MongoClient

import os
import json
import datetime
import sys

# MongoDB setup
client = MongoClient( os.getenv('MONGOURL', 'mongodb://localhost:27017/') )
db = client.refugee_tweet_db
refugee_tweets = db.refugee_tweets

cursor = refugee_tweets.find({}, modifiers={"$snapshot": True})

def update_tweet( refugee_tweets, tweet ):
    tweet['sentiment'] = get_sentiment(tweet['text'])
    refugee_tweets.save(tweet)

def get_sentiment(text):
    print text      # TODO: Sentiment calculations there !

for tweet in cursor:
    if 'text' in tweet.keys():
        update_tweet(refugee_tweets, tweet)

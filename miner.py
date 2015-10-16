#!/usr/bin/python
# -*- coding: utf-8 -*-
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler

import pymongo
from pymongo import MongoClient

import os
import json

# Tweepy setup
consumer_key = os.environ['TWITTER_CONSUMER_KEY']
consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_secret = os.environ['TWITTER_ACCESS_SECRET']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# MongoDB setup
client = MongoClient( os.getenv('MONGOURL', 'mongodb://localhost:27017/') )
db = client.refugee_tweet_db
refugee_tweets = db.refugee_tweets

class MyListener(StreamListener):
    def on_data(self, data):
        try:
            tweet_obj = json.loads(data)
            tweet_id = refugee_tweets.insert_one(tweet_obj).inserted_id
            print("tweet %s added" % str(tweet_id))
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
    def on_error(self, status):
        print("Something went ... wrong " + str(status))
        return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#refugee', '#refugeecrisis', '#refugees'])

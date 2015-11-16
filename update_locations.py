#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymongo
from pymongo import MongoClient

import os
import json
import datetime
import sys
import requests
import csv
import time
import urllib
import re

# MongoDB setup
client = MongoClient( os.getenv('MONGOURL', 'mongodb://localhost:27017/') )
db = client.refugee_tweet_db
refugee_tweets = db.refugee_tweets

googleMapsAddress = 'https://maps.googleapis.com/maps/api/geocode/json'

with open('../../locationsAggregates_cut.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        address = row[0]

        url = googleMapsAddress + '?key=' + os.getenv('GOOGLE_MAPS_API_KEY')
        print 'address = ' + address
        url += '&address=' + urllib.quote(address)
        response = requests.get(url)
        responseObj = json.loads(response.text)
        print 'Response: '
        if responseObj['status'] == 'OK':
            location = responseObj['results'][0]['geometry']['location']
            print 'Location: '
            print location
            coordinates = { 'type': 'Point', 'coordinates': [location['lng'], location['lat']] }
            print 'coordinates'
            print coordinates

            result = refugee_tweets.update_many({'user.location': address}, { '$set': { 'coordinates': coordinates }} )

            print("Result : ", result.matched_count, ", ", result.modified_count)
        time.sleep(1);

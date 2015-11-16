# -*- coding: utf-8 -*-
import json
import codecs
import sentiment_value
from sentiment_value import * 

positive_count = 0 
negative_count = 0 
neutral_count = 0

def update(val) :
	global positive_count
	global negative_count
	global neutral_count
	if val == "negative" : 
		negative_count += 1
	elif val == "positive" : 
		positive_count += 1
	else : 
		neutral_count += 1

with codecs.open("/home/marta/Desktop/ED-projekt/refugges.json", "r", encoding='utf-8-sig') as tweets : 
	tweetes = tweets.readlines()
	for tweet in tweetes : 
		tweet = json.loads(tweet)
		text = tweet["text"]
		if(tweet["lang"]=="en") :
			words = sentiment_value.splitter(text)
			sentiment = sentiment_value.count_sentiment(words)
			update(sentiment)

print "positive: " + str(positive_count)
print "negative: " + str(negative_count)
print "neutral: " + str(neutral_count)

i = 0 
lol = ""
while i <= positive_count : 
	lol += "|"
	i += 1
print lol + " positive" 
i = 0
lol = ""
while i <= negative_count :
	lol += "|"
	i += 1
print lol + " negative"
i = 0 
lol = ""
while i <= neutral_count :
	lol += "|"
	i += 1
print lol + " neutral"

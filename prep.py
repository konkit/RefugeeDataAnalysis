import json
import codecs

with codecs.open("/home/marta/Desktop/ED projekt/cut.json") as tweets : 
	first = tweets.readline()
	tweet = json.loads(first)
	print(json.dumps(tweet, indent=4))

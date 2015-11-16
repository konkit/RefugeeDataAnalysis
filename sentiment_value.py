#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs
import nltk

#tweet = "Does media manipulate people by showing only women and children of #Syria when most of the #refugees are men?"
def splitter(text):
	nltk_splitter = nltk.data.load('tokenizers/punkt/english.pickle')
	nltk_tokenizer = nltk.tokenize.TreebankWordTokenizer()
	sentences = nltk_splitter.tokenize(text)
	tokenized_sentences = [nltk_tokenizer.tokenize(sent) for sent in sentences]
	clean_sentences = []
	for sentence in tokenized_sentences : 
		sen = []
		for word in sentence : 
			if not (len(word) == 1 and (ord(word) == 35 or (ord(word)) == 64)) : 
				sen.append(word)
		clean_sentences.append(sen) 
	return clean_sentences

def count_sentiment(tweet) :
	positive_file = codecs.open('/home/marta/Desktop/ED-projekt/positive-words.txt', "r")
	negative_file = codecs.open('/home/marta/Desktop/ED-projekt/negative-words.txt', "r")
	positive = positive_file.readlines()
	negative = negative_file.readlines()
	positive_set = []
	negative_set = []
	for i in positive : 
		positive_set.append(i.strip())
	for i in negative : 
		negative_set.append(i.strip())
	pos = 0
	neg = 0
	neutral = 0
	for i in tweet[0] : 
		if i in positive_set : 
			pos += 1
		elif i in negative_set : 
			neg += 1
		else : 
			neutral += 1
	overall_sentiment = (-1)*neg + 1*pos + 0*neutral
	if overall_sentiment < 0 : 
		overall_sentiment = "negative"
	elif overall_sentiment > 0 : 
		overall_sentiment = "positive"
	else : 
		overall_sentiment = "neutral"
	return overall_sentiment


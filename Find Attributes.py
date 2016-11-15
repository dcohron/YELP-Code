#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 19:34:40 2016

@author: Nick
"""

import csv
import re
from operator import itemgetter
import nltk
from nltk.util import ngrams
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk import load


def read_file(in_path):
    reviews = []
    with open(in_path, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            reviews.append(row[2])

    return reviews
    
    
    
in_path = r'C:\Users\Gautam\Documents\GitHub\Yelp-dataset\csv\rest_biz_review_map.csv'

review_text = read_file(in_path)

stopLex=set(stopwords.words('english'))

master_dick={}
# split the text into sentences 
# read_file returns a list, can't split a list
#sentences=review_text.split('.') 
	
# for each sentence, set lower case and strip white space 
# replace non-letter characters with space
# split sentence into words 
for review in review_text: 
     # lower case and strip white space
	review=review.lower().strip() 
    	# replace all non-letter characters with a space
	review=re.sub(r'[^a-z]',' ',review) 
	# split on space to get the words in the sentence 
	words=review.split(' ') 

     # for each word in the sentence build frequency word count
	for word in words:  
         # ignore empty words and stopwords
         if word=='' or word in stopLex:
             continue  
         elif word in master_dick:
             master_dick[word]+=1
         else:
             master_dick[word]=1
# open and see master_dick, what people actually write in a review 
 
sorted_master_dick = sorted(master_dick.items(), key=itemgetter(1), reverse=True)

# next step should be to stem and attach labels
 
 
 
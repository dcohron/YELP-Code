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
    
    
    
in_path = '/Users/Nick/Stevens Institute of Technology/Web Analytics/Final Project/data_repo/auto_reviews.csv'

review_text = read_file(in_path)

stopLex=set(stopwords.words('english'))


# split the text into sentences 
sentences=review_text.split('.') 
	
# for each sentence, set lower case and strip white space 
# replace non-letter characters with space
# split sentence into words 
for sentence in sentences: 
     # lower case and strip white space
	sentence=sentence.lower().strip() 
    	# replace all non-letter characters with a space
	sentence=re.sub('[^a-z]',' ',sentence) 
	# split on space to get the words in the sentence 
	words=sentence.split(' ') 

     # for each word in the sentence build frequency word count
	for word in words:  
         # ignore empty words and stopwords
         if word=='' or word in stopLex:continue  
         
 
 
 
 
 
 
 
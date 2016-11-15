#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 19:34:40 2016
@author: Nick Cohron

The script includes the following pre-processing steps for text:
- Sentence Splitting
- Term Tokenization
- Ngrams
- POS tagging

The run function includes all 2grams of the form: <ADVERB> <ADJECTIVE>


POS tags list: https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
"""

import csv
import re
from operator import itemgetter
import nltk
from nltk.util import ngrams
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk import load



# read file with review subset and return one corpus of reviews
def read_file(in_path):
    reviews = []
    with open(in_path, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            reviews.append(row[2])

    return reviews
    
    
# return all the 'adv adj' twograms
def getNounAdjNgrams(terms, noun, adv, n):

	result=[]

      # creates a sliding window of two words each
	grams = ngrams(terms, n) # compute 2-grams
    
   	# for each gram
    	for gram in grams:  
         # if the 2gram is an adjective followed by a noun
         if gram[0] in adj and gram[1] in noun: 
             result.append(gram)
   
	return result


# return all the terms that belong to a specific POS type
def getPOSterms(terms,POStags,tagger):
	
	tagged_terms=tagger.tag(terms)#do POS tagging on the tokenized sentence

      # dictionary for return
	POSterms={}  

      # initialize dictionary of key, value where value is a set
	for tag in POStags:
           POSterms[tag]=set()

	# for each tagged term
	for pair in tagged_terms:
         for tag in POStags: # for each POS tag 
             if pair[1].startswith(tag): 
                 POSterms[tag].add(pair[0])

	return POSterms

    
    
# main body of program    
def run(path):    

    # get raw review text from file    
    review_text = read_file(in_path)
    
    print(review_text)
    
    # make a tagger
    _POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
    tagger = load(_POS_TAGGER)

    stopLex=set(stopwords.words('english'))

    paragraph = review_text.split('.')
    
    
#==============================================================================
#     # split the text into sentences 
#     sentences=review_text.split('.') 
# 	
#     # for each sentence, set lower case and strip white space 
#     # replace non-letter characters with space
#     # split sentence into words 
#     for sentence in sentences: 
#         # lower case and strip white space
#         sentence = sentence.lower().strip() 
#         # replace all non-letter characters with a space
#         sentence = re.sub('[^a-z]',' ',sentence) 
#         # split on space to get the words in the sentence 
#         words = sentence.split(' ') 
# 
#         # for each word in the sentence
#         for word in words:  
#             # ignore empty words and stopwords
#             if word=='' or word in stopLex:continue  
#==============================================================================
         
    # split sentences
    sentences = sent_tokenize(paragraph)
    print 'NUMBER OF SENTENCES: ',len(sentences)

    adjWithNoun = []

    # for each sentence
    for sentence in sentences:

        # replace chars that are not letters or numbers with a space
        sentence = re.sub('[^a-zA-Z\d]',' ',sentence)
         
        # remove duplicate spaces
        sentence = re.sub(' +',' ', sentence).strip()

        # tokenize the lowercase sentence
        terms = nltk.word_tokenize(sentence.lower())   

        # POS tags of interest 
        POStags = ['JJ','NN'] 		
        POSterms = getPOSterms(terms,POStags,tagger)

        # get the set of adjectives and nouns
        adjectives = POSterms['JJ']
        nouns = POSterms['NN']

        # get the results for this sentence 
        # call function to get ngrams
        n = 2
        adjWithNoun += getNounAdjNgrams(terms, adjectives, adverbs, n)
		
	return adjWithNoun

 
 
 
 
 
if __name__=='__main__':
     
     # file with raw text reviews
     in_path = '/Users/Nick/Stevens Institute of Technology/Web Analytics/Final Project/data_repo/auto_reviews.csv'
     
     # send raw text for processing of attributes
     print run(in_path)
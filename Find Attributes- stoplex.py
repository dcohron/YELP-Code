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
The run function includes of grams various sizes that include <NOUN> and <ADJECTIVE>
POS tags list: https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
"""

import csv
import re
from operator import itemgetter
import nltk
from nltk.util import ngrams
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import load



def get_freq_nouns(nouns):
    
    # initialize empty dictionary 
    freqNoun = {} 
    
    for noun in nouns:
        # print noun
        # check have seen the noun before
        if noun in freqNoun: 
            # increment count
            freqNoun[noun] = freqNoun[noun]+1  
        # have not seen the noun before
        else:  
            # initialize its count to 1 
            freqNoun[noun] = 1

    # sort the dictionary
    sorted_attributes = sorted(freqNoun.items(), key=itemgetter(1), reverse=True)
    # print sorted_attributes
    
    # return the sorted dictionary    
    return sorted_attributes  


#==============================================================================
# def getNounList(terms, nouns, adjectives, n):
# 
#       # creates a sliding window of two words each
# 	grams = ngrams(terms, n) # compute 2-grams
#     
#    	# for each gram
#     	for gram in grams:  
#          # if the 2gram is an adjective followed by a noun
#          if gram[0] in adjectives and gram[1] in nouns:
#              NounList.add(gram[1])
# 	return NounList
#==============================================================================

  
# return all the 'adv adj' twograms
def getNounAdjNgrams(terms, nouns, adjectives, n):

	result=[]

      # creates a sliding window of two words each
	grams = ngrams(terms, n) # compute 2-grams
    
   	# for each gram
    	for gram in grams:  
         # if the 2gram is an adjective followed by a noun
         if gram[0] in adjectives and gram[1] in nouns: 
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
 
 
# procedure to write attributes to file 
def write_to_file(out_path, attribute_list):
    with open(out_path, 'wb') as csv_file:
        writer = csv.writer(csv_file)
        for item in attribute_list:
            writer.writerow(item)
 

# main sub-routine of program       
def run(path):   
    # initialize variables
    adjWithNoun = []
    review_count = 0
    bad_review_count = 0
    
    # make a tagger
    _POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
    tagger = load(_POS_TAGGER)

    # load sexicon of stop words
    stopLex = set(stopwords.words('english'))
    
    # get raw review text from file
    with open(in_path, 'rb') as f:
        review = []
        reader = csv.reader(f)
        for row in reader:
            review = row[2]
            review_count += 1
    
            #print(review)
    


            try:
            # split sentences
                sentences = sent_tokenize(review)
                # print 'NUMBER OF SENTENCES: ', len(sentences)
                continue
            except:
                bad_review_count += 1
                #print "Oops!  That was not tokenizable. Try again..."

            # for each sentence
            for sentence in sentences:

                # replace chars that are not letters or numbers with a space
                sentence = re.sub('[^a-zA-Z\d]',' ',sentence)
         
                # remove duplicate spaces and lower case
                sentence = re.sub(' +',' ', sentence).strip()
                sentence = sentence.lower()
                
                # split on space to get the words in the sentence 
                words=sentence.split(' ')  
                
                # initialize variable to hold sentence without stop words
                shortened_sentence = ""

                # for each word in the sentence build frequency word count
                for word in words:  
                    # ignore empty words and stopwords
                    if word=='' or word in stopLex:continue 
                    else: shortened_sentence += word + ' '

                # tokenize the lowercase sentence
                terms = nltk.word_tokenize(shortened_sentence)   

                # POS tags of interest 
                POStags = ['JJ','NN'] 		
                POSterms = getPOSterms(terms,POStags,tagger)

                # get the set of adjectives and nouns
                adjectives = POSterms['JJ']
                nouns = POSterms['NN']

                # get the results for this sentence 
                # call function to get ngrams
                n = 2
                adjWithNoun += getNounAdjNgrams(terms, nouns, adjectives, n)
	
        #initializing list of Nouns from adjwithnoun
        NounList=[]

        #get a list of all Nouns from adjwithnoun
        for gram in adjWithNoun:
            NounList.append(gram[1])
                
    print review_count
    print bad_review_count
    return NounList      

 
#tag_list = nltk.pos_tag(sentence)
 
 
if __name__=='__main__':
     
     # file with raw text reviews

     in_path = r'/Users/Nick/Stevens Institute of Technology/Web Analytics/Final Project/data_repo/reviews/diner_reviews.csv'
     out_path = r'/Users/Nick/Stevens Institute of Technology/Web Analytics/Final Project/data_repo/attributes/newattributes- diner.csv'

#     in_path = r'C:\Users\Gautam\Documents\GitHub\Yelp-dataset\csv\auto_reviews.csv'

     
     # send raw text for processing of attributes
     noun_list = run(in_path)
     # print type(noun_list)
     # print noun_list
     
     # frequency analysis of nouns extracted as potential attributes
     attributes = get_freq_nouns(noun_list)
     # print type(attributes)
     
     # save attribute list to file
     write_to_file(out_path, attributes)
     
     n = 10
     first_n_attributes = attributes[:n]
     
     print first_n_attributes
     print len(attributes)
     
     
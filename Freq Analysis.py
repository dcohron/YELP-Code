#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 19:51:31 2016

@author: Nick Cohron
Purpose:  Frequency Analysis of Category Attributes
"""

import re
import csv
from csv import reader
from operator import itemgetter


def run(path):
    
    freqCategory={} # empty dict 
#    attribute = ""
    

    for key, value in biz_dict.iteritems():
        # just get the string for categories
        categories = biz_dict[key]
        # remove punctuation and first and last bracket
        categories = re.sub("[!@#$.'']", "", categories)
        categories = categories[1:-1]
        print categories


        for category in categories.split(','):
            # strip white space
            category = category.strip()
            print(category)
            if  category in freqCategory: # have seen the category before
                freqCategory[category] = freqCategory[category]+1 # increment each count 
            else: # have not seen the category before 
                freqCategory[category] = 1 # initialize its count to 1   
   
#    fin.close() # close connection to file


    # sort the dictionary
    sorted_attributes = sorted(freqCategory.items(), key=itemgetter(1), reverse=True)

    # return the sorted dictionary    
    return sorted_attributes   
 
def save_to_file (path, attributeList): 
    with open(path,'wb') as out:
        csv_out = csv.writer(out)
        for row in attributeList:
            csv_out.writerow(row) 
    
    
def main ():
     fname = '/Users/Nick/Stevens Institute of Technology/Web Analytics/Final Project/data_repo/restaurants.csv'
     return run(fname)
     
data = main()
print data

save_to_file( "/Users/Nick/Stevens Institute of Technology/Web Analytics/Final Project/data_repo/biz_sorted_attributes.csv", data)


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
    
#==============================================================================
#     fin = open(path, 'r') # open file 
#     for line in reader(fin): # for each line in the file 
#         print(line)
#         categories = line[0]
#         print(categories)
#==============================================================================
 
#==============================================================================
#     with open(path, 'rb') as f:
#         mycsv = csv.reader(f)
#         for row in mycsv:
#             categories = row[1]
#         
#         print(categories)
#==============================================================================

    for key, value in restaurant_dict.iteritems():
        categories = restaurant_dict[key]
        categories = re.sub("[!@#$.'']", "", categories)
        categories = categories[1:-1]
        print categories


        for category in categories.split(','):
            category = category.strip()
            print(category)
            if  category in freqCategory: # have seen the category before
                freqCategory[category] = freqCategory[category]+1 # increment each count 
            else: # have not seen the category before 
                freqCategory[category] = 1 # initialize its count to 1   
   
#    fin.close() # close connection to file


    # sort the dictionary
    sorted_attributes = sorted(freqCategory.items(),key=itemgetter(1),reverse=True)

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

save_to_file( "/Users/Nick/Stevens Institute of Technology/Web Analytics/Final Project/data_repo/sorted_attributes.csv", data)


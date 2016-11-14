#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 10:16:31 2016

@author: Nick
"""

import csv




def matching_business_ids(path, target_dict):
    subset = ()
    
    with open(path, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[10] in target_dict:
                subset.extend(row[10], row[13], row[14])
    
    return subset

    
    

# read in the file and put into data frame
input = '/Users/Nick/Stevens Institute of Technology/Web Analytics/Final Project/data_repo/yelp_academic_dataset_review.csv'
target_dict = restaurant_dict

match = matching_business_ids(input, target_dict)
# del data_frame

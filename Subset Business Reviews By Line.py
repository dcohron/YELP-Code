#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 10:16:31 2016

@author: Nick
"""

import csv




def matching_business_ids(in_path, target_dict):
    subset = []
    
    with open(in_path, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[4] in target_dict:
                subset.append(tuple((row[4], row[6], row[2])))
    
    return subset

# procedure to write to file 
def write_to_file (out_path, data):
    with open(out_path,'wb') as f:
        csv_out=csv.writer(f)
        csv_out.writerow(['business_id', 'stars','review'])
        for row in data:
            csv_out.writerow(row)
    

# set variables
in_path = '/Users/Nick/Stevens Institute of Technology/Web Analytics/Final Project/data_repo/yelp_academic_dataset_review.csv'
out_path = '/Users/Nick/Stevens Institute of Technology/Web Analytics/Final Project/data_repo/pizza_reviews.csv'
target_dict = pizza_dict

match = matching_business_ids(in_path, target_dict)

write_to_file(out_path, match)


#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 10:16:31 2016

@author: Nick
"""

import csv




def matching_business_ids(path, target_dict):
    subset = []
    
    with open(path, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[4] in target_dict:
                subset.extend([row[4], row[6], row[2]])
    
    return subset

# procedure to write to file 
def write_to_file (out_path, data):
    with open('ur file.csv','wb') as out:
        csv_out=csv.writer(out)
        csv_out.writerow(['business_id', 'stars','review'])
        for row in data:
            csv_out.writerow(row)
    

# set variables
input = '/Users/Nick/Stevens Institute of Technology/Web Analytics/Final Project/data_repo/yelp_academic_dataset_review.csv'
output = '/Users/Nick/Stevens Institute of Technology/Web Analytics/Final Project/data_repo/restaurant_reviews.csv'
target_dict = restaurant_dict

match = matching_business_ids(input, target_dict)

write_to_file(output, match)


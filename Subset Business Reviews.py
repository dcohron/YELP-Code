#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 10:16:31 2016

@author: Nick
"""

import csv
import pandas

def matching_business_ids(df, dict):
    subset = df[['business_id', 'stars', 'text']].query('business_id in dict')
    return subset



# read in the file and put into data frame
input = '/Users/Nick/Stevens Institute of Technology/Web Analytics/Final Project/data_repo/yelp_academic_dataset_review.csv'
target_dict = restaurant_dict

data_frame = pandas.read_csv(input)

match = matching_business_ids(data_frame, target_dict)
# del data_frame

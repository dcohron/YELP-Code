#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 17:46:46 2016

@author: Nick Cohron
"""

import csv
import pandas
from ast import literal_eval

# declare global variables
biz_dict = {}
restaurant_dict = {}

# procedure to write to file 
def write_to_file (out_path, dict):
    with open(out_path, 'wb') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in dict.items():
            writer.writerow([key, value])

# read in the file and put into data frame
input = '/Users/Nick/Stevens Institute of Technology/Web Analytics/Final Project/yelp_dataset_challenge_academic_dataset/business.csv'
data_frame = pandas.read_csv(input)

# select two columns of interest and put into a dictionary
businessID = data_frame['business_id']
categories = data_frame['categories']
# categories = literal_eval(categories)
junk = map(lambda k, v: biz_dict.update({k: v}), businessID, categories)


# delete unused variable to save memory
del data_frame
del businessID
del categories


# search biz dictionary for restaurants only and create dictionary subset
restaurant_dict = {k:v for k, v in biz_dict.iteritems() if 'Restaurants' in v}
                   
# search biz dictionary for other business types and create dictionary subset                  
hair_dict = {k:v for k, v in biz_dict.iteritems() if 'Hair Salons' in v}   
auto_dict = {k:v for k, v in biz_dict.iteritems() if 'Automotive' in v} 
home_dict = {k:v for k, v in biz_dict.iteritems() if 'Home & Garden' in v}             
             
             

# subset dictionary from restaurants for particular cuisines
fastfood_dict = {k:v for k, v in restaurant_dict.iteritems() if 'Fast Food' in v}
pizza_dict = {k:v for k, v in restaurant_dict.iteritems() if 'Pizza' in v}
mexican_dict = {k:v for k, v in restaurant_dict.iteritems() if 'Mexican' in v}
burger_dict = {k:v for k, v in restaurant_dict.iteritems() if 'Burgers' in v}      
american_dict = {k:v for k, v in restaurant_dict.iteritems() if 'American' in v}              
chinese_dict = {k:v for k, v in restaurant_dict.iteritems() if 'Chinese' in v}              
diners_dict = {k:v for k, v in restaurant_dict.iteritems() if 'Diners' in v}

# write out the dictionaries
# for restaurants
write_to_file('/Users/Nick/Stevens Institute of Technology/Web Analytics/Final Project/data_repo/restaurants.csv', restaurant_dict)
write_to_file('/Users/Nick/Stevens Institute of Technology/Web Analytics/Final Project/data_repo/fastfood.csv', fastfood_dict)
write_to_file('/Users/Nick/Stevens Institute of Technology/Web Analytics/Final Project/data_repo/mexican.csv', mexican_dict)
write_to_file('/Users/Nick/Stevens Institute of Technology/Web Analytics/Final Project/data_repo/pizza.csv', pizza_dict)              
write_to_file('/Users/Nick/Stevens Institute of Technology/Web Analytics/Final Project/data_repo/burger.csv', burger_dict)
write_to_file('/Users/Nick/Stevens Institute of Technology/Web Analytics/Final Project/data_repo/american.csv', american_dict)
write_to_file('/Users/Nick/Stevens Institute of Technology/Web Analytics/Final Project/data_repo/chinese.csv', chinese_dict)
write_to_file('/Users/Nick/Stevens Institute of Technology/Web Analytics/Final Project/data_repo/diner.csv', diners_dict)

# for other business types
write_to_file('/Users/Nick/Stevens Institute of Technology/Web Analytics/Final Project/data_repo/hair.csv', hair_dict)
write_to_file('/Users/Nick/Stevens Institute of Technology/Web Analytics/Final Project/data_repo/auto.csv', auto_dict)
write_to_file('/Users/Nick/Stevens Institute of Technology/Web Analytics/Final Project/data_repo/home.csv', home_dict)

              
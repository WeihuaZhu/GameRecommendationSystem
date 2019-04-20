# web scraping script
# rewrite in Python 3
# Author: Andy Yao
# Version 1.4
# Date 04/18/2019
# 
# encoding=utf8

import csv
import numpy as np
import json
from sklearn.feature_extraction import text
import heapq
import os
class mydict(dict):
        def __str__(self):
            return json.dumps(self)

fileName = 'review_all.txt'
# x = open(fileName).read()
# print(len(x))
prev_index = -1
game_indexes = []
with open(fileName) as f:
    reviews = []
    while True:
        line = f.readline()
        if not line:
            break
        rev_temp = json.loads(line)
        curr_index = rev_temp["index"]
        # remove duplicates
        if curr_index == prev_index:
            continue
        rev_temp = json.loads(line)
        reviews.append(rev_temp["review"])
        game_indexes.append(int(curr_index))
        prev_index = curr_index

# print(game_indexes)

with open('output_ign.csv') as csv_file:
    with open('refine_output_ign.csv', mode='w') as output_ign:
        csv_reader = csv.reader(csv_file, delimiter=',')
        output_writer = csv.writer(output_ign, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in csv_reader:
            # print(row[0])    
            if int(row[0]) in game_indexes:
                # print(row[0])
                output_writer.writerow(row)

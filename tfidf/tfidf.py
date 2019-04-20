import numpy as np
import json
from sklearn.feature_extraction import text
import heapq
import os

fileName = 'review_all.txt'
# x = open(fileName).read()
# print(len(x))
prev_index = -1
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
        prev_index = curr_index

# print(review1)
platforms = {'xbox','ps','psp','ps3','ps2','gb','gba','360','n64'}
gameGeneral = {'game','ign','play','playing','player','version','gaming','games','app','player','players','download','win','lose','won','lost'}
noMeaningWords = {'thank','thanks','didn','don','doesn','didn','nearly','hasn','haven','isn'}
stop_words = text.ENGLISH_STOP_WORDS.union(gameGeneral).union(platforms).union(noMeaningWords)
# print(stop_words)
tfidf_vec = text.TfidfVectorizer(stop_words=stop_words, min_df=0.035)
tfidf_matrix = tfidf_vec.fit_transform(reviews).toarray()

# print(tfidf_matrix.shape)

#print 10 most important words for each review according to tfidf, first 10 for testing
# for i in range(10):
#     a = list(tfidf_matrix[i])
#     idx = list(map(a.index, heapq.nlargest(80, a)))
#     output_file = open('tfidf_matrix_test.txt', 'a')
#     for j in idx:
#         print(tfidf_vec.get_feature_names()[j], end = '  ', file = output_file)
#     print('\n', file = output_file)
#     output_file.close()
#     
with open('tfdif_all_features.txt', 'w') as output_file0:
    a = list(tfidf_matrix[0])
    print(len(a))
    line = []
    for j in range(len(a)):
        line.append(tfidf_vec.get_feature_names()[j])
    print(line, file = output_file0)


with open('tfidf_matrix_boolean.txt', 'w') as output_file:
    for i in range(100):
        a = list(tfidf_matrix[i])
        idx = list(map(a.index, heapq.nlargest(200, a)))
        line = []
        for j in range(len(a)):
            line.append(0)
        sum = 0
        for j in idx:
            line[j] = 1
            # print(tfidf_vec.get_feature_names()[j])
            # print(a[j])
        for j in range(len(a)):
            print(line[j], end = '\t', file = output_file)
        print('\n', file = output_file)
# output_file.close()

with open('tfidf_matrix_float.txt', 'w') as output_file2:
    for i in range(100):
        a = list(tfidf_matrix[i])
        idx = list(map(a.index, heapq.nlargest(200, a)))
        line = []
        for j in range(len(a)):
            line.append(0)
        sum = 0
        for j in idx:
            line[j] = a[j]
            sum += a[j]
            # print(tfidf_vec.get_feature_names()[j])
            # print(a[j])
        print(sum)        
        for j in range(len(a)):
            print(line[j], end = '\t', file = output_file2)
        print('\n', file = output_file2)
# In[0]
import numpy as np
import json
from sklearn.feature_extraction import text
import heapq
import os
class mydict(dict):
        def __str__(self):
            return json.dumps(self)
# In[1]        
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
noMeaningWords = {'thank','thanks','didn','don','doesn','didn','nearly','hasn','haven','isn', 'couldn', '__', 'let', 'yes'}
gameUnrelatedWords = {'need', 'seemingly', 'does', 'make', 'despite', 'away', 'total', 'allows', 'come', 'thing', 'certainly', 'wants', 'got', 'maybe', 'likely', 'looks'}
stop_words = text.ENGLISH_STOP_WORDS.union(gameGeneral).union(platforms).union(noMeaningWords).union(gameUnrelatedWords)
# print(stop_words)
tfidf_vec = text.TfidfVectorizer(stop_words=stop_words, min_df=0.03)
tfidf_matrix = tfidf_vec.fit_transform(reviews).toarray()

# print(tfidf_matrix.shape)

#print 10 most important words for each review according to tfidf, first 10 for testing
# In[1]
for i in range(10, 20):
     a = list(tfidf_matrix[i])
     idx = []
     for j in range(80):
         idx.append(a.index(max(a)))
         a[a.index(max(a))] = - np.Inf
     for j in idx:
         print(tfidf_vec.get_feature_names()[j], end = '  ')
     print('\n')
# In[2]
with open('tfdif_all_features.txt', 'w') as output_file0:
    a = list(tfidf_matrix[0])
    print(len(a))
    line = []
    for j in range(len(a)):
        line.append(tfidf_vec.get_feature_names()[j])
    print(line, file = output_file0)


with open('tfidf_matrix_boolean.txt', 'w') as output_file:
    for i in range(len(tfidf_matrix)):
        a = list(tfidf_matrix[i])
        idx = []
        for j in range(200):
            idx.append(a.index(max(a)))
            a[a.index(max(a))] = - np.Inf
        line = [0 for k in range(len(a))]
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
    for i in range(len(tfidf_matrix)):
        a = list(tfidf_matrix[i])
        idx = []
        for j in range(200):
            idx.append(a.index(max(a)))
            a[a.index(max(a))] = - np.Inf
        line = [0 for k in range(len(a))]
        sum = 0
        a = list(tfidf_matrix[i])
        for j in idx:
            line[j] = a[j]
            sum += a[j]
            # print(tfidf_vec.get_feature_names()[j])
            # print(a[j])
        print(sum)        
        for j in range(len(a)):
            print(line[j], end = '\t', file = output_file2)
        print('\n', file = output_file2)
# In[3]
with open('tfidf_dict_form.txt', 'w') as output_file3:
    for i in range(len(tfidf_matrix)):
        a = list(tfidf_matrix[i])
        idx = []
        for j in range(200):
            idx.append(a.index(max(a)))
            a[a.index(max(a))] = - np.Inf
        dictForGame = {}
        a = list(tfidf_matrix[i])
        for j in idx:
            dictForGame[tfidf_vec.get_feature_names()[j]] = a[j]
        data = mydict(dictForGame)
        print(data, file = output_file3)
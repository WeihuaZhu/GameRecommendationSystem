import numpy as np
import json
from sklearn.feature_extraction import text
import heapq

fileName = 'review_all.txt'
# x = open(fileName).read()
# print(len(x))

with open(fileName) as f:
    reviews = []
    while True:
        line = f.readline()
        if not line:
            break
        rev_temp = json.loads(line)
        reviews.append(rev_temp["review"])

# print(review1)
platforms = {'xbox','ps','psp','ps3','ps2','gb','gba','360','n64'}
gameGeneral = {'game','ign','play','playing','player','version','gaming','games','app','player','players','download','win','lose','won','lost'}
noMeaningWords = {'thank','thanks','didn','don','doesn','didn','nearly','hasn','haven','isn'}
stop_words = text.ENGLISH_STOP_WORDS.union(gameGeneral).union(platforms).union(noMeaningWords)
# print(stop_words)
tfidf_vec = text.TfidfVectorizer(stop_words=stop_words, min_df=0.05)
tfidf_matrix = tfidf_vec.fit_transform(reviews).toarray()

#print 10 most important words for each review according to tfidf
for i in range(10):
    a = list(tfidf_matrix[i])
    idx = list(map(a.index, heapq.nlargest(10, a)))
    for j in idx:
        print(tfidf_vec.get_feature_names()[j], end = '  ')
    print()
    
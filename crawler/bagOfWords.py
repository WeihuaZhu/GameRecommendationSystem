import numpy as np
import json
from sklearn.feature_extraction import text

fileName = 'result.txt'
x = open(fileName).read()
reviews = json.loads(x)

review1 = reviews[0]["review"]
review1 = [review1]
# print(review1)
platforms = {'xbox','ps','psp','ps3','ps2','gb','gba','360','n64'}
stop_words = text.ENGLISH_STOP_WORDS.union({'game','ign','play','playing','thank','thanks','version','gaming','games','app','player','players'}).union(platforms)
# print(stop_words)
vectorizer = text.CountVectorizer(stop_words=stop_words, min_df=1)
X = vectorizer.fit_transform(review1).toarray()

d = len(vectorizer.vocabulary_)

print(vectorizer.get_feature_names())
print(X.shape)
print(d)
print(X)
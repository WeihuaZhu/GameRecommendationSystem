import numpy as np
import json
from sklearn.feature_extraction import text

fileName = 'review_all.txt'
# x = open(fileName).read()
# print(len(x))

with open(fileName) as f:
    first_line = f.readline()

reviews = json.loads(first_line)

review1 = reviews["review"]
review1 = [review1]
print(text)

# platforms = {'xbox','ps','psp','ps3','ps2','gb','gba','360','n64'}
# gameGeneral = {'game','ign','play','playing','player','version','gaming','games','app','player','players','download','win','lose','won','lost'}
# noMeaningWords = {'thank','thanks','didn','don','doesn','didn','nearly','hasn','haven','isn'}
# stop_words = text.ENGLISH_STOP_WORDS.union(gameGeneral).union(platforms).union(noMeaningWords)

# vectorizer = text.CountVectorizer(stop_words=stop_words, min_df=1)
# X = vectorizer.fit_transform(review1).toarray()

# d = len(vectorizer.vocabulary_)

# print(vectorizer.get_feature_names())
# print(X.shape)
# print(d)
# print(X)
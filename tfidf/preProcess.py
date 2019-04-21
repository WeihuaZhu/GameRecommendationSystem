import numpy as np
import json
from sklearn.feature_extraction import text

# fileName = 'review_all.txt'
# outputFileName = 'review_stem.txt'
# x = open(fileName).read()
# print(len(x))

# with open(fileName) as f:
#     line = f.readline()
#     record = json.loads(line)
#     game = record["game"]
#     index = record["index"]
#     gameUrl = record["gameUrl"]
#     review = record["review"]

line = ""
with open('tfidf_all_features.txt') as f:
    line = f.readline()
    f.close()

words = line.split('\', \'')
print(words)


from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
stemmed = [porter.stem(word) for word in words]
print(set(stemmed))


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
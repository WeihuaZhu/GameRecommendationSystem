## test TFIDF
import numpy as np
import pandas as pd 
from sklearn.metrics.pairwise import cosine_similarity


def GetGameInfo(uID,numTop = 20):
    featureL  = read_tfidf_matrix('tfidf_matrix_float.txt')
    featureM = np.asarray(featureL)
    numGame = len(featureM)
    numFeat = len(featureM[0])
    
    curFeat = featureM[uID,:].reshape(1,-1)
    simiResult = cosine_similarity(curFeat, featureM)
    # Set uID zero in  simiResult
    simiResult[0][uID]=0
    # Sort result by similarities score
    simiResultIndx = np.argsort(simiResult, axis=1)
    simiResultIndx = np.flip(simiResultIndx)

    return simiResultIndx[0][0:numTop]

def GetRecommendGames(gameIndexArr):
    GameList = []
    numGame = len(gameIndexArr)
    df = pd.read_csv('output_ign.csv', header=None, usecols=[2],delimiter = ',')

    for idx in range(numGame):
        curIndx = gameIndexArr[idx]
        gameName = df.loc[curIndx,2]
        GameList.append(gameName)
    return  GameList

def read_tfidf_matrix(filename):
    # f = open ( '../tfidf/tfidf_matrix_test.txt' , 'r')
    f = open (filename , 'r')
    matrix = []
    for line in f:
        if len(line) != 1:
            matrix.append(line.split())
    # print(line)
    # print(matrix)
    return matrix

# suggest_gameIdex = GetGameInfo(36)
# print(GetRecommendGames(suggest_gameIdex))
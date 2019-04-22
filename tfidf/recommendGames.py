## test TFIDF
import numpy as np
import sys
import pandas as pd 
from sklearn.metrics.pairwise import cosine_similarity


def GetGameInfo(uID,numTop = 75):
    featureL  = read_tfidf_matrix('tfidf_matrix_float.txt')
    featureM = np.asarray(featureL)
    numGame = len(featureM)
    numFeat = len(featureM[0])
    curFeat = featureM[uID,:].reshape(1,-1)
    simiResult = cosine_similarity(curFeat, featureM)
    # Set uID zero in  simiResult
    simiResult[0][uID]=0
    # Normalized  simiResult
    simiResultNorm = simiResult/np.linalg.norm(simiResult)
    # Make a copy  
    simiResultCopy = simiResultNorm 

    uniqueGenre,scoreArr,edChoice=getAllgenre()
    scoreArrNP = np.asarray(scoreArr)
    scoreArrNorm = scoreArrNP/np.linalg.norm(simiResult)
    edChoiceNP = np.asarray(edChoice)
    edChoiceNorm = edChoiceNP/np.linalg.norm(edChoiceNP)
    r1 = np.amax(simiResultNorm)/np.amax(scoreArrNorm)
    r2 = np.amax(simiResultNorm)/np.amax(edChoiceNorm)

    
    for j in range(numGame):
        simiResultCopy[0][j] = 0.95*simiResultNorm[0][j] + 0.05*(0.9*r1*scoreArrNorm[j]+0.1*r2*edChoiceNorm[j])

    # Sort result by similarities score and get index
    simiResultIndx = np.argsort(simiResultCopy, axis=1)
    simiResultIndx = np.flip(simiResultIndx)

    return simiResultIndx[0][0:numTop]

def GetRecommendGames(gameIndexArr):
    GameList = list()
    numGame = len(gameIndexArr)
    df = pd.read_csv('refine_output_ign.csv', header=None, usecols=[2],delimiter = ',')
    # print(df.loc[selectGame,2])
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

def getAllgenre():
    dfGenre = pd.read_csv('refine_output_ign.csv', header=None, usecols=[6],delimiter = ',')
    dfScore = pd.read_csv('refine_output_ign.csv', header=None, usecols=[5],delimiter = ',')
    dfEchoice = pd.read_csv('refine_output_ign.csv', header=None, usecols=[7],delimiter = ',')
    numofGame = dfGenre.size
    genreList = list()
    scoreArr = list()
    edChoice = list()

    for i in range(numofGame):
        curGenre = dfGenre.loc[i,6]
        curGenre =str(curGenre)
        genreList.extend(curGenre.split(','))

        curScore = float(dfScore.loc[i,5])
        scoreArr.append(curScore)
        
        curEC = dfEchoice.loc[i,7]
        if curEC == "Y":
            isChoice = 1
        else:
            isChoice =0
        edChoice.append(isChoice)

    uniqueGenre = set(genreList)
    return uniqueGenre,scoreArr,edChoice




def getGameList(ind):
    suggest_gameIdex = GetGameInfo(ind)
    return GetRecommendGames(suggest_gameIdex)

def deduplicate(res):
    n = len(res)
    dedup_res = [res[0]]
    for i in range(1, n):
        if res[i] == res[i - 1]:
            continue
        else:
            dedup_res.append(res[i])
    return dedup_res
# # # np.set_printoptions(threshold=sys.maxsize)
# suggest_gameIdex = GetGameInfo(selectGame)
# print(GetRecommendGames(suggest_gameIdex))
ind = 15756
res = getGameList(ind)
print(deduplicate(res))

# print(getGameList(1100))
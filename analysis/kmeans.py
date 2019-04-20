# web scraping script
# rewrite in Python 3
# Author: Andy Yao
# Version 1.4
# Date 04/19/2019
# 
# encoding=utf8
#  
from numpy import *
import time
import matplotlib.pyplot as plt
import os
 
 
# calculate Euclidean distance
def euclDistance(vector1, vector2):
	return sqrt(sum(power(vector2 - vector1, 2)))
 
# init centroids with random samples
def initCentroids(dataSet, k):
	numSamples, dim = dataSet.shape
	centroids = zeros((k, dim))
	for i in range(k):
		index = int(random.uniform(0, numSamples))
		centroids[i, :] = dataSet[index, :]
	return centroids
 
# k-means cluster
def kmeans(dataSet, k, MAX_ITR = 30):
	numSamples = dataSet.shape[0]
	# first column stores which cluster this sample belongs to,
	# second column stores the error between this sample and its centroid
	clusterAssment = mat(zeros((numSamples, 2)))
	clusterChanged = True
 
	## step 1: init centroids
	centroids = initCentroids(dataSet, k)

	itr = 0
 
	while clusterChanged:
		itr += 1
		print('iteration:')
		print(itr)
		count = 0
		clusterChanged = False
		## for each sample
		for i in range(numSamples):
			minDist  = 100000.0
			minIndex = 0
			## for each centroid
			## step 2: find the centroid who is closest
			for j in range(k):
				distance = euclDistance(centroids[j, :], dataSet[i, :])
				if distance < minDist:
					minDist  = distance
					minIndex = j
			
			## step 3: update its cluster
			if clusterAssment[i, 0] != minIndex:
				count += 1
				clusterChanged = True
				clusterAssment[i, :] = minIndex, minDist**2
 
		## step 4: update centroids
		for j in range(k):
			pointsInCluster = dataSet[nonzero(clusterAssment[:, 0].A == j)[0]]
			centroids[j, :] = mean(pointsInCluster, axis = 0)

		print('No of changes:' + str(count))
		if (count <= numSamples * 0.005 or itr >= MAX_ITR):
			break
 
	print('Congratulations, cluster complete!')
	return centroids, clusterAssment
 
# show your cluster only available with 2-D data
def showCluster(dataSet, k, centroids, clusterAssment):
	numSamples, dim = dataSet.shape
	if dim != 2:
		print("Sorry! I can not draw because the dimension of your data is not 2!")
		return 1
 
	mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
	if k > len(mark):
		print("Sorry! Your k is too large! please contact Zouxy")
		return 1
 
	# draw all samples
	for i in xrange(numSamples):
		markIndex = int(clusterAssment[i, 0])
		plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])
 
	mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
	# draw the centroids
	for i in range(k):
		plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize = 12)
 
	plt.show()


def read_tfidf_matrix(filename):
	# f = open ( '../tfidf/tfidf_matrix_test.txt' , 'r')
	f = open (filename , 'r')
	matrix = []
	for line in f:
		if len(line) != 1:
			features = []
			# print(line)
			for item in line.strip().split('\t'):
				features.append(float(item))
			# print(features)
			matrix.append(features)
	# print(matrix)
	
	return matrix

filename = '../tfidf/tfidf_matrix_float.txt'
matrixr = read_tfidf_matrix(filename)
# print(matrixr[0])

dataSet = mat(matrixr)
k = 20
centroids, clusterAssment = kmeans(dataSet, k)
# print(centroids)
print(clusterAssment)

with open('kmeans_centroids.txt', 'w') as output_file:
	for i in range(len(centroids)):
		for j in range(len(centroids[i])):
			print(centroids[i][j], end = '\t', file = output_file)
		print('\n', file = output_file)



with open('kmeans_clusters.txt', 'w') as output_file2:
	for i in range(len(clusterAssment)):
		print(int(clusterAssment[i, 0]), end = '\t', file = output_file2)
		print('\n', file = output_file2)
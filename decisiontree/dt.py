## Decision Tree sample code
## version: python 3.7
## conda install python-graphviz
from sklearn import tree
import graphviz
from sklearn.model_selection import train_test_split
import numpy


# # visualize
# dot_data = tree.export_graphviz(clf, out_file=None) 
# graph = graphviz.Source(dot_data)
# graph.render("iris")

def readFeatureFromMatrix(matrixFileName):
    ## return X, look like [[0, 0], [1, 1]]
    f = open (matrixFileName, 'r')
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


def readLabelFromVector(vectorFileName):
    ## return Y, look like [0, 1, 5, 19]
    



if __name__ == '__main__':
    X = readFeatureFromMatrix('tfidf_matrix_float.txt')
    Y = readLabelFromVector('kmeans_clusters.txt')
    X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=n_test, random_state=2)
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X_train, Y_train)



    



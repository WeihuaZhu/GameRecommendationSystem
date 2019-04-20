## Decision Tree sample code
## version: python 3.7
## conda install python-graphviz
from sklearn import tree
import graphviz
from sklearn.model_selection import train_test_split


# # visualize
# dot_data = tree.export_graphviz(clf, out_file=None) 
# graph = graphviz.Source(dot_data)
# graph.render("iris")

def readFeatureFromMatrix(matrixFileName):
    ## return X, look like [[0, 0], [1, 1]]


def readLabelFromVector(vectorFileName):
    ## return Y, look like [0, 1, 5, 19]



if __name__ == '__main__':
    X = readFeatureFromMatrix('tfidf_matrix_float.txt')
    Y = readLabelFromVector('kmeans_clusters.txt')
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X, Y)



    



## Decision Tree sample code
## version: python 3.7
## conda install python-graphviz
from sklearn import tree
import graphviz
from sklearn.model_selection import train_test_split
from numpy import *




def readFeatureFromMatrix(matrixFileName):
    ## return X, look like [[0, 0], [1, 1]]
    f = open(matrixFileName, 'r')
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
    return mat(matrix)


def readLabelFromVector(vectorFileName):
    ## return Y, look like [0, 1, 5, 19]
    f = open(vectorFileName, 'r')
    Y = []
    for line in f:
        if len(line) > 0:
            Y.append(int(line))
    return Y
    



if __name__ == '__main__':
    X = readFeatureFromMatrix('tfidf_matrix_float.txt')
    Y = readLabelFromVector('kmeans_clusters.txt')
    n = len(Y)
    n_train = int(n/2)
    n_test = n - n_train
    
    X_train,X_test,Y_train,Y_test = train_test_split(X, Y, test_size=n_test, random_state=2)
    
    criterion = 'entropy'
    training_mode = 'all' # 'all'/'half'
    if training_mode == 'half':
        for max_depth in range(15,30):
            clf = tree.DecisionTreeClassifier(max_depth=max_depth,criterion=criterion)
            clf = clf.fit(X_train, Y_train)

        # # visualize
        # dot_data = tree.export_graphviz(clf, out_file=None) 
        # graph = graphviz.Source(dot_data)
        # graph.render("game")
            count = 0
            for i in range(n_test):
                x = X_test[i,:]
                y = clf.predict(x)
                if y == Y_test[i]:
                    count = count + 1
            accuracy = count/n_test
            print("The accuracy when max_depth=", max_depth, "is: ", accuracy)
    elif training_mode == 'all':
        for max_depth in range(30,50):
            clf = tree.DecisionTreeClassifier(max_depth=max_depth,criterion=criterion)
            clf = clf.fit(X, Y)

            count = 0
            for i in range(n):
                x = X[i,:]
                y = clf.predict(x)
                if y == Y[i]:
                    count = count + 1
            accuracy = count/n
            print("The accuracy when max_depth=", max_depth, "is: ", accuracy)
    else:
        print("Invalid Training Mode!")
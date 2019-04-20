## Decision Tree sample code
## version: python 3.7
## conda install python-graphviz
from sklearn import tree
import graphviz
from sklearn.datasets import load_iris

iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)

dot_data = tree.export_graphviz(clf, out_file=None) 
graph = graphviz.Source(dot_data) 
graph.render("iris")
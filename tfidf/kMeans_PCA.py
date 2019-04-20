# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 23:41:11 2019

@author: shaxi
"""
#TODO: read tfidf matrix as tfidf_matrix
# In[2]
print('Start Kmeans:')    
from sklearn.cluster import KMeans    
num_of_cluster = 15
clf = KMeans(n_clusters=num_of_cluster) 
s = clf.fit(tfidf_matrix)  
#中心点    
print(clf.cluster_centers_)        
#每个样本所属的簇    
label = []               #存储1000个类标 4个类    
print(clf.labels_)    
#用来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数  958.137281791    
print(clf.inertia_)

# In[3]
from sklearn.decomposition import PCA
pca = PCA(n_components = 3)
pca_out = pca.fit_transform(tfidf_matrix)
x = [[] for i in range(num_of_cluster)]
y = [[] for i in range(num_of_cluster)]
z = [[] for i in range(num_of_cluster)]
for i in range(len(pca_out)):
    x[clf.labels_[i]].append(pca_out[i][0])
    y[clf.labels_[i]].append(pca_out[i][1])
    z[clf.labels_[i]].append(pca_out[i][2])
for i in range(num_of_cluster):
    plt.plot(y[i], z[i], 'o')
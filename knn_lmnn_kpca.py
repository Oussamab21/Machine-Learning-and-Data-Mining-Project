#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 16:35:03 2017

@author: dell1
"""

import pandas as pd
import random
import numpy as np
import numpy as np
from metric_learn import LMNN
#import metric_learn
import pandas as pd
from sklearn.cross_validation import train_test_split 
import random
from sklearn.neighbors import KNeighborsClassifier
#from sklearn.cross_validation import cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.grid_search import GridSearchCV




from sklearn.neighbors import KNeighborsClassifier
def pause():
    programPause = input("Press the <ENTER> key to continue...")
    
    
    
def rbf_kernel(X, gamma, n_components):
    
    # Calculating the squared Euclidean distances for every pair of points
    # in the MxN dimensional dataset.
    sqdists = pdist(X, 'sqeuclidean')

    # Converting the pairwise distances into a symmetric MxM matrix.
    mat_sqdists = squareform(sqdists)

    # Computing the MxM kernel matrix.
    K = exp(-gamma * mat_sqdists)

    # Centering the symmetric NxN kernel matrix.
    N = K.shape[0]
    one_n = np.ones((N,N)) / N
    K = K - one_n.dot(K) - K.dot(one_n) + one_n.dot(K).dot(one_n)

    # Obtaining eigenvalues in descending order with corresponding
    # eigenvectors from the symmetric matrix.
    eigenvals, eigenvecs = eigh(K)

    # Obtaining the i eigenvectors that corresponds to the i highest eigenvalues.
    X_pc = np.column_stack((eigenvecs[:,-i] for i in range(1,n_components+1)))

    return X_pc    
    
    
def poly_kernel(X,n_components,P):
    #K = X.dot(X.T)## change
    A=1
    B=1
    K=((X.dot(X.T))+1)**P
    #K=(A<X, X> + B)**P
    N = K.shape[0]
    one_n = np.ones((N,N)) / N
    K = K - one_n.dot(K) - K.dot(one_n) + one_n.dot(K).dot(one_n)

    # Obtaining eigenvalues in descending order with corresponding
    # eigenvectors from the symmetric matrix.
    eigenvals, eigenvecs = eigh(K)

    # Obtaining the i eigenvectors that corresponds to the i highest eigenvalues.
    X_pc = np.column_stack((eigenvecs[:,-i] for i in range(1,n_components+1)))
 
    return X_pc
    
    
#############################################################################    
    
    
#df=df.to_csv(filename ,  index_col = None)
df = pd.read_csv('/home/dell1/Desktop/MLpr/feature_new.csv',index_col=False)
df2=df


from sklearn.utils import shuffle
df2 = shuffle(df2)
print("data shuffled")

msk = np.random.rand(len(df2)) < 0.7
train = df[msk]
test = df[~msk]

#Y=np.asarray(df2.ix[:,-1])
#Y=Y.T
#X=np.asarray(df2.iloc[:,1:-1])

#X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=random.seed())

train = shuffle(train)
print(" train set shuffled")


t_split=np.array_split(train, 2)

s1=t_split[0]
s2=t_split[1]

x1=s1.ix[:,0:8]
y1=s1.ix[:,8]

x2=s2.ix[:,0:8]
y2=s2.ix[:,8]

x1new=x1
y1new=y1
s1new=s1
x2new=x2
y2new=y2
s2new=s2

#######################get rid of outliers#########################

while True: 
 #print("oui")   
 x1=x1new 
 y1=y1new
 x2=x2new
 y2=y2new
 s1=s1new
 s2=s2new
  
 knn = KNeighborsClassifier(n_neighbors=1)
 knn.fit(x1, y1)
 y2_pred = knn.predict(x2)
#print(metrics.accuracy_score(y2, y2_pred))
 cond=(y2==y2_pred)
 #print(cond)
 s2res=s2.where(cond)
 s2new=s2res.dropna(how='all')
 x2new=s2new.ix[:,0:8]
 y2new=s2new.ix[:,8]


 knn2 = KNeighborsClassifier(n_neighbors=1)
 #knn.fit(x1, y1)
 knn2.fit(x2new,y2new)
 y1_pred = knn2.predict(x1)
 #print(metrics.accuracy_score(y2, y2_pred))
 cond2=(y1==y1_pred)
 #print(cond)
 s1res=s1.where(cond2)
 s1new=s1res.dropna(how='all')
 x1new=s1new.ix[:,0:8]
 y1new=s1new.ix[:,8]
 if (x1.shape[0]==x1new.shape[0] or x2.shape[0]==x2new.shape[0]):
     break

frames = [s1new, s2new]
s=pd.concat(frames)
#######################################get rid of irrelevat example#############



storage=pd.DataFrame()
dustbin=pd.DataFrame()

sample=s.sample(1)
storage=storage.append(sample)
newstorage=storage


while True:
    storage=newstorage
    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(storage.ix[:,0:8],storage.ix[:,8])
    for index, row in s.iterrows():
        #print("row is  ",row )
        #print()
        x=row[0:8]
        #print("x is ",x)
        pred=knn.predict(x.reshape(1,-1))
        #print(pred)
        #pause()
        if pred==row[8]:
           #print("correctly")
           dustbin=dustbin.append(row)
        else:
            #print("wrong")
            newstorage=newstorage.append(row)
    if(storage.shape[0]==newstorage.shape[0]):        
            break
#print("the final cleaned data is ",newstorage)   

newstorage.to_csv('/home/dell1/Desktop/MLpr/cleanedknn.csv', sep='\t')

X_train=newstorage.ix[:,0:8]
Y_train=newstorage.ix[:,8]
X_test=test.ix[:,0:8]
Y_test=test.ix[:,8]
         
#%%
from sklearn.neighbors import KNeighborsClassifier as knn
kn = knn(n_neighbors=40)   ## the best is 0.5757 with k=40
kn.fit(X_train, Y_train)
#ac1=kn.score(X_test,Y_test)
predict = kn.predict(X_test)
normal_knn = accuracy_score(Y_test,predict)
print("the normal knn accuracy is ",normal_knn)
################################################
#%%
print("here")
import numpy as np
X_train = np.array(X_train)
Y_train = np.array(Y_train)
X_test= np.array(X_test)
Y_test= np.array(Y_test)


## tuning here ... 

scores=[]
#for i in range(1,5):
#print("current k is ",i)   
lmnn2 =LMNN(k=5, learn_rate=1e-6)#.fit(X_train,Y_train)
print("here2")
print(lmnn2)
lmnn2=lmnn2.fit(X_train, Y_train)
print("hi")
X_train2 = lmnn2.transform(X_train)
X_test2 = lmnn2.transform(X_test)
kn2 = KNeighborsClassifier(n_neighbors=40).fit(X_train2, Y_train)
predict = kn2.predict(X_test2)
lmnn_acc = accuracy_score(Y_test,predict)
print("lmnn accuracy is ",lmnn_acc)
#scores.append(lmnn_acc)
#print("the scores are ",scores)
#k=np.argmax(scores)+1


#%%using kernal pca
from scipy.spatial.distance import pdist, squareform
from scipy import exp
from scipy.linalg import eigh
import numpy as np
from sklearn.preprocessing import StandardScaler
#import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

import time

import os








def rbf_kernel(X, gamma, n_components):
    
    # Calculating the squared Euclidean distances for every pair of points
    # in the MxN dimensional dataset.
    sqdists = pdist(X, 'sqeuclidean')

    # Converting the pairwise distances into a symmetric MxM matrix.
    mat_sqdists = squareform(sqdists)

    # Computing the MxM kernel matrix.
    K = exp(-gamma * mat_sqdists)

    # Centering the symmetric NxN kernel matrix.
    N = K.shape[0]
    one_n = np.ones((N,N)) / N
    K = K - one_n.dot(K) - K.dot(one_n) + one_n.dot(K).dot(one_n)

    # Obtaining eigenvalues in descending order with corresponding
    # eigenvectors from the symmetric matrix.
    eigenvals, eigenvecs = eigh(K)

    # Obtaining the i eigenvectors that corresponds to the i highest eigenvalues.
    X_pc = np.column_stack((eigenvecs[:,-i] for i in range(1,n_components+1)))

    return X_pc    
    







X_train_kpca=rbf_kernel(X_train, gamma=2, n_components=2)
X_test_kpca=rbf_kernel(X_test, gamma=2, n_components=2)
print("passed PCA")
lmnn3 =LMNN(k=2, learn_rate=1e-6)#.fit(X_train,Y_train)
print("here2")
print(lmnn3)
lmnn3=lmnn3.fit(X_train_kpca, Y_train)
print("hi")
X_train2 = lmnn3.transform(X_train_kpca)
X_test2 = lmnn3.transform(X_test_kpca)
kn2 = KNeighborsClassifier(n_neighbors=40).fit(X_train2, Y_train)
predict = kn2.predict(X_test2)
lmnn_acc = accuracy_score(Y_test,predict)
print("kernelpca lmnn accuracy is ",lmnn_acc)
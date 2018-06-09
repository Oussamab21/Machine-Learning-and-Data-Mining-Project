# -*- coding: utf-8 -*-
"""
Author: Arunava MAULIK
"""

import Levenshtein as edit_distance

import pandas as pd
import numpy as np

    
df1=pd.read_csv("C:/Users/Administrateur/Desktop/ML/myseq_train_set02_200_12.csv").values
df=pd.read_csv("C:/Users/Administrateur/Desktop/ML/my_labels_200_12.csv").values
   
   
def get_neighbors(train_set,labels,test_instance,k):
    distances = []
    for i in range(len(train_set)):
        dist = edit_distance.distance(str(test_instance), str(train_set[i]))
        distances.append((train_set[i], dist,  labels[i],i))
    distances.sort(key=lambda x: x[1])
    neighbors = distances[:k]
    digit=distances[0][2]
    train=distances[0][0]
    dist1=distances[0][1]
    example=distances[0][3] 
    return neighbors,digit,train,dist1,example
a= "0, 7, 7, 7, 7, 7, 7, 7, 7, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 0, 7, 7, 7, 7, 7, 7, 7, 0, 7, 7, 0, 1, 1, 1, 1, 1, 2, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 5, 4, 5, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7, 7, 6, 7, 7"
df2=np.array(a)

algo,digit,train,dist1,example=get_neighbors(df1,df,df2,1)
digit


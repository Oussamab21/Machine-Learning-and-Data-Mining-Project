# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 01:21:42 2017

@author: Arunava
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from collections import Counter
import linecache

class FeatureExtract:
    def __init__(self,path,label):
        self.path=path
        self.label=label

    def CreateDataframe(self):
        line = linecache.getline(self.path,1)
        line = list(line)
        d = dict(Counter(line))
        del d['\n']
        df=pd.DataFrame([d])
        num_lines = sum(1 for line in open(self.path))
        for i in range(2,num_lines):
            line = linecache.getline(self.path,i)
            line = list(line)
            e = dict(Counter(line))
            del e['\n']
            df1=pd.DataFrame([e])
            f=[df,df1]
            df=pd.concat(f)
            df=df.fillna(0)
        df.columns=['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven']
        df['label']=self.label    
            
        return df       
    
class FinalOutput:
    def __init__(self,zero,one,two,three,four,five,six,seven,eight,nine):
        self.zero=zero
        self.one=one
        self.two=two
        self.three=three
        self.four=four
        self.five=five
        self.six=six
        self.seven=seven
        self.eight=eight
        self.nine=nine
        
    def DFtoCSV(self):
        m=[self.zero,self.one,self.two,self.three,self.four,self.five,self.six,self.seven,self.eight,self.nine,]
        new_df=pd.concat(m)
        new_df.to_csv('D:/UJM/mldm project/feature_new.csv')
 ######Zero######       
digit_zero=FeatureExtract('D:/UJM/mldm project/freeman_codes/Output/vipul00.txt',0)
#digit_zero.create_dataframe()
dataframe_0=FeatureExtract.CreateDataframe(digit_zero)
dataframe_0.head(10)
######One######
digit_One=FeatureExtract('D:/UJM/mldm project/freeman_codes/Output/vipul01.txt',1)
dataframe_1=FeatureExtract.CreateDataframe(digit_One)
dataframe_1.head(10)
######Two######
digit_Two=FeatureExtract('D:/UJM/mldm project/freeman_codes/Output/vipul02.txt',2)
dataframe_2=FeatureExtract.CreateDataframe(digit_Two)
dataframe_2.head(10)
######Three######
digit_Three=FeatureExtract('D:/UJM/mldm project/freeman_codes/Output/vipul03.txt',3)
dataframe_3=FeatureExtract.CreateDataframe(digit_Three)
dataframe_3.head(10)
######four######
digit_Four=FeatureExtract('D:/UJM/mldm project/freeman_codes/Output/vipul04.txt',4)
dataframe_4=FeatureExtract.CreateDataframe(digit_Four)
dataframe_4.head(10)
######Five######
digit_Five=FeatureExtract('D:/UJM/mldm project/freeman_codes/Output/vipul05.txt',5)
dataframe_5=FeatureExtract.CreateDataframe(digit_Five)
dataframe_5.head(10)
######Six######
digit_Six=FeatureExtract('D:/UJM/mldm project/freeman_codes/Output/vipul06.txt',6)
dataframe_6=FeatureExtract.CreateDataframe(digit_Six)
dataframe_6.head(10)
######Seven######
digit_Seven=FeatureExtract('D:/UJM/mldm project/freeman_codes/Output/vipul07.txt',7)
dataframe_7=FeatureExtract.CreateDataframe(digit_Seven)
dataframe_7.head(10)
######Eight######
digit_Eight=FeatureExtract('D:/UJM/mldm project/freeman_codes/Output/vipul08.txt',8)
dataframe_8=FeatureExtract.CreateDataframe(digit_Eight)
dataframe_8.head(10)
######Nine######
digit_Nine=FeatureExtract('D:/UJM/mldm project/freeman_codes/Output/vipul09.txt',9)
dataframe_9=FeatureExtract.CreateDataframe(digit_Nine)
dataframe_9.head(10)

######Merge and write to CSV####
features=FinalOutput(dataframe_0,dataframe_1,dataframe_2,dataframe_3,dataframe_4,dataframe_5,dataframe_6,dataframe_7,dataframe_8,dataframe_9)
features.DFtoCSV()
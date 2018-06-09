
# coding: utf-8

# In[53]:


from PIL import Image
import numpy as np 
import cv2
import matplotlib.pyplot as plt
import glob
import pandas as pd
final=[]
for image in glob.glob("/Users/vipulvijigiri/Movies/MLDM-2017/AML/AML_Project/Data/mnist_png/training/8/*.png"):

    #print(image)
    image =  cv2.imread(image,0)
    #image = cv2.dilate(image,np.ones((3,3),np.uint8),iterations=1)
    resized = cv2.resize(image, (28,28), interpolation = cv2.INTER_AREA)
    ret,img = cv2.threshold(resized,127,255,0)
    image = cv2.dilate(img,np.ones((3,3),np.uint8),iterations=1)
    for i  in range(len(image)):
        image[i, 0] = 0
        image[i, len(image)-1] = 0
        image[0, i] = 0
        image[len(image)-1,i] = 0
    connectivity = 4  
    output = cv2.connectedComponentsWithStats(image, connectivity, cv2.CV_32S)
    num_labels = output[0]
    labels = output[1]
    stats = output[2]
    max_area = np.argmax(stats[1:].max(axis=1)) + 1
    for i in range(1,num_labels):
        if (max_area == i):
            labels[labels == i] = 255
        else:
            labels[labels == i] = 0
    for i, row in enumerate(labels):
        for j, value in enumerate(row):
            if value == 255 or value == 1 :
                start_point = (i, j)
                break
        else:
                 continue
                 break
    directions = [ 0,  1,  2,
                   7,      3,
                   6,  5,  4]
    dir2idx = dict(zip(directions, range(len(directions))))

    change_j =   [-1,  0,  1, # x or columns
                  -1,      1,
                  -1,  0,  1]

    change_i =   [-1, -1, -1, # y or rows
                   0,      0,
                   1,  1,  1]

    border = []
    chain = []
    curr_point = start_point
    for direction in directions:
        idx = dir2idx[direction]
        new_point = (start_point[0]+change_i[idx], start_point[1]+change_j[idx])
        if labels[new_point] != 0: # if is ROI
            border.append(new_point)
            chain.append(direction)
            curr_point = new_point
            break

    count = 0
    while curr_point != start_point:
        b_direction = (direction + 5) % 8 
        dirs_1 = range(b_direction, 8)
        dirs_2 = range(0, b_direction)
        dirs = []
        dirs.extend(dirs_1)
        dirs.extend(dirs_2)
        for direction in dirs:
            idx = dir2idx[direction]
            new_point = (curr_point[0]+change_i[idx], curr_point[1]+change_j[idx])
            if labels[new_point] != 0:
                border.append(new_point)
                chain.append(direction)
                curr_point = new_point
                break
        if count == 1000: break
        count += 1
    print(chain)
    final.append(chain)
    np.save("train_08",final)
    

    


# In[50]:


len(final)


# In[79]:


import pandas as pd


# In[80]:


data=np.load("train_00.npy")


# In[81]:



df0=pd.DataFrame(data)


# In[82]:


data=np.load("train_01.npy")


# In[83]:


df1=pd.DataFrame(data)


# In[84]:


data=np.load("train_02.npy")


# In[85]:


df2=pd.DataFrame(data)


# In[86]:


data=np.load("train_03.npy")


# In[87]:


df3=pd.DataFrame(data)


# In[88]:


data=np.load("train_04.npy")


# In[89]:


df4=pd.DataFrame(data)


# In[90]:


data=np.load("train_05.npy")


# In[91]:


df5=pd.DataFrame(data)


# In[92]:


data=np.load("train_06.npy")


# In[93]:


df6=pd.DataFrame(data)


# In[94]:


data=np.load("train_07.npy")


# In[95]:


df7=pd.DataFrame(data)


# In[96]:


data=np.load("train_08.npy")


# In[97]:


df8=pd.DataFrame(data)


# In[98]:


data=np.load("train_09.npy")


# In[99]:


df9=pd.DataFrame(data)


# In[100]:


m=[df0,df1,df2,df3,df4,df5,df6,df7,df8,df9]


# In[101]:


new_df=pd.concat(m)


# In[102]:


new_df.to_csv("sequence_train.csv",index=False,header=False)


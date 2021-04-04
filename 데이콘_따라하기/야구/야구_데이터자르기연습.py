#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


pre_season=pd.read_csv("C:/Users/Jang/Desktop/python/Data/야구/Pre_Season_Batter.csv")
regular=pd.read_csv("C:/Users/Jang/Desktop/python/Data/야구/Regular_Season_Batter.csv")
regular_Day=pd.read_csv("C:/Users/Jang/Desktop/python/Data/야구/Regular_Season_Batter_Day_by_Day_b4.csv")
sub=pd.read_csv("C:/Users/Jang/Desktop/python/Data/야구/submission.csv")


# 1. ops 0.9 넘는 row
# 2. batter_name 박석민인 row
# 3. 이름이 박석민이면서 year가 2009

# In[3]:


regular.loc[regular['OPS']>0.9]


# In[4]:


regular.loc[regular['batter_name']=='박석민']


# In[5]:


regular.loc[(regular['batter_name']=='박석민')&(regular['year']==2009)]


# for 문

# In[7]:


for i in ['박석민','채태인','최형우','박해민']:
    print(regular.loc[regular['batter_name']==i]['OPS'].mean())


# In[10]:


for i in [0,1,2,3]:
    print(regular['OPS'].iloc[i])


# In[ ]:





# In[ ]:





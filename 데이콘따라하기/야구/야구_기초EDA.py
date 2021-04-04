#!/usr/bin/env python
# coding: utf-8

# In[22]:


import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[14]:


pre_season=pd.read_csv("C:/Users/Jang/Desktop/python/Data/야구/Pre_Season_Batter.csv")
regular=pd.read_csv("C:/Users/Jang/Desktop/python/Data/야구/Regular_Season_Batter.csv")
regular_Day=pd.read_csv("C:/Users/Jang/Desktop/python/Data/야구/Regular_Season_Batter_Day_by_Day_b4.csv")
sub=pd.read_csv("C:/Users/Jang/Desktop/python/Data/야구/submission.csv")


# In[16]:


regular.columns


# In[17]:


regular=regular[['batter_name','year','AB','position','OPS']]


# In[18]:


regular


# In[21]:


regular['batter_name'].nunique() #선수가 345명 있다.


# In[23]:


sns.distplot(regular['year'])


# year이 늘어날 수록 숫자가 늘어난다.

# In[26]:


regular['year'].describe()


# In[27]:


sns.distplot(regular['AB'])


# 백타석 미만의 선수가 많다

# In[30]:


regular['AB'].describe()


# In[31]:


regular['position'].value_counts()


# 양타 포지션 빈도수가 매우 적다

# In[33]:


sns.distplot(regular['OPS'])


# na값이 있을시 displot이 그려지지 않는다
# sns.distplot(regular["OPS"].dropna()) 하면 자동으로 na 삭제하고 그려진다.

# In[35]:


regular['OPS'].describe()


# In[36]:


regular.head()


# In[38]:


plt.scatter(regular['AB'],regular["OPS"])
plt.xlabel('AB')
plt.ylabel('OPS')


# AB가 올라감에 따라 OPS도 올라가는 경향을 보인다.

# In[39]:


plt.scatter(regular['AB'],regular["year"])
plt.xlabel('AB')
plt.ylabel('year')


# In[ ]:


plt.scatter(regular['AB'],regular["OPS"])
plt.xlabel('AB')
plt.ylabel('OPS')


# In[40]:


regular.groupby(['position'])['OPS'].mean()


# In[41]:


regular.groupby(['position'])['AB'].mean()


# In[ ]:





# In[ ]:





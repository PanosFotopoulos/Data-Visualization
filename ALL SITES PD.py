#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as pn
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df3=pd.read_csv('all_sites_scores.csv')


# In[3]:


df3.info()


# In[4]:


df3.describe()


# In[5]:


plt.figure(figsize=(10,4))
sns.scatterplot(data=df3,x='RottenTomatoes',y='RottenTomatoes_User')
plt.ylim(0,100)
plt.xlim(0,100)
plt.show()


# In[6]:


df3


# In[7]:


df3['RTomatoesDiff'] = df3['RottenTomatoes'] - df3['RottenTomatoes_User']


# In[8]:


plt.figure(figsize=(10,4),dpi=150)
plt.title('RT Critics Score Minus RT User Score')
sns.histplot(x=df3['RTomatoesDiff'],kde=True,bins=25)


# In[9]:


plt.figure(figsize=(10,4),dpi=150)
plt.title('Abs Difference Between RT Critics Score Minus RT User Score')
sns.histplot(x=df3['RTomatoesDiff'].abs(),kde=True,bins=25)
plt.show()


# In[10]:


df3.sort_values('RTomatoesDiff',ascending=False)[:5]


# In[11]:


df3.nsmallest(5,'RTomatoesDiff')[['FILM','RTomatoesDiff']]


# In[12]:


df3.nlargest(5,'RTomatoesDiff')[['FILM','RTomatoesDiff']]


# In[13]:


plt.figure(figsize=(10,4),dpi=150)
sns.scatterplot(df3,x='Metacritic',y='Metacritic_User')


# In[14]:


df3.info()


# In[15]:


plt.figure(figsize=(10,4),dpi=150)
sns.scatterplot(df3,y='IMDB_user_vote_count',x='Metacritic_user_vote_count')


# In[16]:


df3[df3['IMDB_user_vote_count']==334164]


# In[17]:


df3['Metacritic_user_vote_count'].nlargest()


# In[18]:


df3[df3['Metacritic_user_vote_count']==2375]


# In[ ]:





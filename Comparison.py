#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df1 = pd.read_csv('fandango_scrape.csv')#import my csv


# In[3]:


df1['YEAR']=df1['FILM'].apply(lambda film_name:film_name.split('(')[-1].replace(')',''))


# In[4]:


df2 = df1[df1['VOTES']>0]


# In[5]:


df2['STARS_DIF']= df2['STARS']-df2['RATING']
df2['STARS_DIF'] = df2['STARS_DIF'].round(2)


# In[6]:


df3=pd.read_csv('all_sites_scores.csv')


# In[7]:


df3['RTomatoesDiff'] = df3['RottenTomatoes'] - df3['RottenTomatoes_User']


# In[8]:


df4=pd.merge(df1,df3,on='FILM',how='inner')


# In[9]:


df4.info()


# In[10]:


df4['IMDB'].max()


# In[11]:


df4['RT_NORMAL'] = np.round(df4['RottenTomatoes']/20,1)
df4['RTU_NORMAL'] = np.round(df4['RottenTomatoes']/20,1)

df4['Meta_NORMAL'] = np.round(df4['Metacritic']/20,1)
df4['METAU_NORMAL']= np.round(df4['Metacritic_User']/2,1)

df4['IDBM_NORMAL']= np.round(df4['IMDB']/2)


# In[12]:


df4


# In[13]:


df5= df4[['STARS','RATING','RT_NORMAL','RTU_NORMAL','Meta_NORMAL','METAU_NORMAL','IDBM_NORMAL']]


# In[14]:


df5.head()


# In[15]:


def move_legend(ax, new_loc, **kws):
    old_legend = ax.legend_
    handles = old_legend.legendHandles
    labels = [t.get_text() for t in old_legend.get_texts()]
    title = old_legend.get_title().get_text()
    ax.legend(handles, labels, loc=new_loc, title=title, **kws)



# In[16]:


fig, ax = plt.subplots(figsize=(15,6),dpi=150)
sns.kdeplot(data=df5,clip=[0,5],shade=True,palette='Set1',ax=ax)
move_legend(ax, "upper left")
plt.show()


# In[17]:


fig, ax = plt.subplots(figsize=(15,6),dpi=150)
sns.kdeplot(data=df5[['RT_NORMAL','STARS']],clip=[0,5],fill=True,ax=ax)
move_legend(ax, "upper left")


# In[18]:


fig = plt.subplots(figsize=(15,6),dpi=150)
sns.histplot(data=df5[['RT_NORMAL','Meta_NORMAL','METAU_NORMAL','IDBM_NORMAL']],bins=50)
plt.show()


# In[19]:


fig = plt.subplots(figsize=(15,6),dpi=150)
sns.histplot(data=df5,bins=50)
plt.show()


# In[20]:


sns.clustermap(data=df5,cmap='magma',col_cluster=False)


# In[21]:


df6=df4[['STARS','RATING','RT_NORMAL','RTU_NORMAL','Meta_NORMAL','METAU_NORMAL','IDBM_NORMAL','FILM']]


# In[22]:


top10worstmovies = df6.nsmallest(10,'RT_NORMAL')


# In[23]:


plt.figure(figsize=(15,6),dpi=150)
sns.kdeplot(data=top10worstmovies,clip=[0,10],fill=True,palette='Set1')
plt.title("Ratings for RT Critic's 10 Worst Reviewed Films")
plt.show()


# In[ ]:





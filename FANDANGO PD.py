#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import numpy as pn
import matplotlib.pyplot as plt
import seaborn as sns


# In[15]:


df1 = pd.read_csv('fandango_scrape.csv')#import my csv


# In[16]:


df1.head()#top 5


# In[17]:


df1.info()
#Index information(range of the index+ data type and memory usage.)
#Column information(The column name,The number of non-null (non-missing) values
#The data type of the column and The memory usage of the column)
#General Information provides you overall the Dataframe otal number of columns, 
#the number of non-null values in each column and the data types used.


# In[41]:


df1.describe()
#Count: The number of non-null (non-missing) values for each column.
#Mean: The mean (average) value of each column.
#Std: The standard deviation, which measures the amount of variation or dispersion of each column's values.
#Min: The minimum value in each column.
#25%, 50%, 75%: The quartiles of each column. The 50% is the median,
#representing the middle value when the data is sorted in ascending order.
#Max: The maximum value in each column.


# In[20]:


plt.figure(figsize=(10,4))
sns.scatterplot(data=df1,x='RATING',y='VOTES')
plt.show()


# In[23]:


df1.corr(numeric_only=True)
#counting the corraletion between the colums 


# In[27]:


#split year from the FILM column name and create a new column to assign the year in
df1['YEAR']=df1['FILM'].apply(lambda film_name:film_name.split('(')[-1].replace(')',''))

#lamda expretion to split the year from the film column


# In[28]:


#plotting the amount of the movies per year
sns.countplot(df1,x='YEAR')
plt.show()


# In[29]:


df1.sort_values('VOTES',ascending=False)[:10]
#sorting my values on the votes columns to get the top 10 voted movies


# In[30]:


df2 = df1[df1['VOTES']>0]


# In[31]:


plt.figure(figsize=(10,4),dpi=150)
sns.kdeplot(df2,x='STARS',fill=True,clip=[0,5],label='Stars Displayed')
sns.kdeplot(df2,x='RATING',fill=True,clip=[0,5],label='True Rating')
plt.legend(loc=(1.05,0.5))


# In[32]:


df2['STARS_DIF']= df2['STARS']-df2['RATING']
df2['STARS_DIF'] = df2['STARS_DIF'].round(2)


# In[33]:


plt.figure(figsize=(10,4),dpi=150)
sns.countplot(data=df2,x='STARS_DIF')


# In[36]:


df2[df2['STARS_DIF'] == 1]


# In[37]:


df1


# In[39]:


sns.kdeplot(df2,x='STARS',fill=True,clip=[0,5],label='Stars Displayed')


# In[40]:


sns.kdeplot(df2,x='RATING',fill=True,clip=[0,5],label='True Rating')


# In[ ]:





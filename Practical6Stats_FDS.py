#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df=pd.read_csv(r'C:\Users\LENOVO\Downloads\stats.csv')
print(df)


# In[2]:


mean1=df['Salary'].mean
mean1


# In[3]:


mean1=df['Salary'].mean()
mean1


# In[10]:


sum1=df['Salary'].sum()
sum1


# In[11]:



max1=df['Salary'].max()
max1


# In[12]:



min1=df['Salary'].min()
min1


# In[13]:



count1=df['Salary'].count()
count1


# In[14]:



mode1=df['Salary'].mode()
mode1


# In[15]:



median1=df['Salary'].median()
median1


# In[16]:



std1=df['Salary'].std()
std1


# In[17]:



var1=df['Salary'].var()
var1


# In[19]:



groupbysum1=df.groupby(['Country']).sum()
groupbysum1

groupbycount1=df.groupby(['Country']).count()
groupbycount1


# In[20]:


skew1=df.skew(axis=0,skipna=True)
skew1


# In[ ]:





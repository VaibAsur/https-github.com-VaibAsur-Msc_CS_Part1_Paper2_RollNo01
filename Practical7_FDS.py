#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
iris=pd.read_csv(r'C:\Users\LENOVO\Downloads\Iris.csv', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
print(iris.head())


# In[12]:


import pandas as pd
wine_reviews = pd.read_csv(r'C:\Users\LENOVO\Downloads\winemag-data-130k-v2.csv', index_col=0)
wine_reviews.head()


# In[14]:


import matplotlib.pyplot as plt
# create a figure and axis
fig, ax = plt.subplots()

# scatter the sepal_length against the sepal_width
ax.scatter(iris['sepal_length'], iris['sepal_width'])
# set a title and labels
ax.set_title('Iris Dataset')
ax.set_xlabel('sepal_length')
ax.set_ylabel('sepal_width')


# In[15]:


columns=iris.columns.drop(['class'])

x_data=range(0, iris.shape[0])

fig, ax= plt.subplots()

for column in columns:
    ax.plot(x_data, iris[column], label=column)
    
ax.set_title('Iris dataset')
ax.legend()


# In[18]:


# create figure and axis
fig, ax = plt.subplots()
# plot histogram
ax.hist(iris['sepal_length'])
# set title and labels
ax.set_title('iris')
ax.set_xlabel('sepal_length')
ax.set_ylabel('Frequency')


# In[20]:


import matplotlib.pyplot as plt

fig, ax= plt.subplots()

data=wine_reviews['points'].value_counts()
points=data.index
frequency=data.values
ax.bar(points, frequency)
ax.set_title('Wine review data set')
ax.set_xlabel('points')
ax.set_ylabel('Frequency')


# In[22]:


wine_reviews['points'].value_counts().sort_index().plot.bar()


# In[23]:


wine_reviews['points'].value_counts().sort_index().plot.barh()


# In[ ]:


wine_reviews.groupby("country").price.mean().sort_values(ascending=False)[:5].plot.bar()


# In[ ]:


wine_reviews.groupby("country").price.mean().sort_values(ascending=False)[:5].plot.bar()


# In[ ]:





# In[ ]:





# In[ ]:





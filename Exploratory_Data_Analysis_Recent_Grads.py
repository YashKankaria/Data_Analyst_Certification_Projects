
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib as mpl
get_ipython().magic('matplotlib inline')
recent_grads=pd.read_csv("recent-grads.csv")
recent_grads.iloc[0]


# In[41]:


recent_grads.head(173)


# In[7]:


recent_grads.tail(2)


# In[8]:


recent_grads.describe()


# In[11]:


raw_data_count=len(recent_grads)
raw_data_count


# In[14]:


recent_grads=recent_grads.dropna()
clean_data_count=len(recent_grads)
clean_data_count


# In[15]:


recent_grads.plot(x="Sample_size",y="Median",kind="scatter",title="Sample Size vs. Median")


# In[16]:


recent_grads.plot(x="Sample_size",y="Unemployment_rate",kind="scatter")


# In[17]:


recent_grads.plot(x="Full_time",y="Median",kind="scatter")


# In[18]:


recent_grads.plot(x="ShareWomen",y="Unemployment_rate",kind="scatter")


# In[19]:


recent_grads.plot(x="Men",y="Median",kind="scatter")


# In[20]:


recent_grads.plot(x="Women",y="Median",kind="scatter")


# In[37]:


recent_grads["Sample_size"].hist(bins=50, range=(0,500))


# In[38]:


recent_grads["Median"].hist()


# In[40]:


recent_grads["Employed"].hist(bins=33)


# In[42]:


recent_grads["Full_time"].hist()


# In[43]:


recent_grads["ShareWomen"].hist()


# In[45]:


recent_grads["Unemployment_rate"].hist()


# In[46]:


recent_grads["Men"].hist()


# In[47]:


recent_grads["Women"].hist()


# In[48]:


from pandas.tools.plotting import scatter_matrix


# In[49]:


scatter_matrix(recent_grads[["Sample_size","Median"]])


# In[50]:


scatter_matrix(recent_grads[["Sample_size","Median","Unemployment_rate"]])


# In[68]:


recent_grads[0:10].plot(kind="bar",x="Major",y="ShareWomen")
recent_grads[163:].plot(kind="bar",x="Major",y="ShareWomen")


# In[70]:


recent_grads[0:10].plot(kind="bar",x="Major",y=["Women","Men"])


# In[ ]:





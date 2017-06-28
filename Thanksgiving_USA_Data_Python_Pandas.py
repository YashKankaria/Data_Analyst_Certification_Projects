
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


data=pd.read_csv("thanksgiving.csv",encoding="Latin-1")
data.head(3)


# In[5]:


data.head(0)


# In[7]:


counts=pd.Series.value_counts(data["Do you celebrate Thanksgiving?"])
counts


# In[9]:


data=data[data["Do you celebrate Thanksgiving?"]=="Yes"]
data.shape


# In[10]:


counts_dishes=pd.Series.value_counts(data["What is typically the main dish at your Thanksgiving dinner?"])
counts_dishes


# In[15]:


main_tofurkey=data[data["What is typically the main dish at your Thanksgiving dinner?"]=="Tofurkey"]
gravy_tofurkey=main_tofurkey["Do you typically have gravy?"]
gravy_tofurkey


# In[28]:


apple_isnull=pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple"])
pumpkin_isnull=pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin"])
pecan_isnull=pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan"])
ate_pies_count=(apple_isnull & pumpkin_isnull & pecan_isnull)
ate_pies=data[apple_isnull & pumpkin_isnull & pecan_isnull]
ate_pies_unique=pd.Series.value_counts(ate_pies_count)
ate_pies_unique


# In[31]:


def age_assign(column):
    if pd.isnull(column):
        return None
    column=column.split(" ")[0]
    column=column.replace("+"," ")
    return int(column)
data["int_age"]=data["Age"].apply(age_assign)
print(data["int_age"].describe())
    
    
    
    


# By default, the program shows the age of 60 as max.

# Not a true depiction of the ages of the participants
# The methodology could be used for exploratory analysis only

# In[32]:


def extract_income(income_str):
    if pd.isnull(income_str):
        return None
    income_str = income_str.split(" ")[0]
    if income_str == "Prefer":
        return None
    income_str = income_str.replace(",", "")
    income_str = income_str.replace("$", "")
    return int(income_str)

data["int_income"] = data["How much total combined money did all members of your HOUSEHOLD earn last year?"].apply(extract_income)
data["int_income"].describe()


# **FINDINGS**
# Although we only have a rough approximation of income, and it skews downward because we took the first value in each string (the lower bound), the average income seems to be fairly high, although there is also a large standard deviation.
# 

# In[36]:


income_less_150000=data[data["int_income"]<150000]["How far will you travel for Thanksgiving?"].value_counts()
income_less_150000


# In[37]:


income_greater_150000=data[data["int_income"]>150000]["How far will you travel for Thanksgiving?"].value_counts()
income_greater_150000


# ***FINDINGS***
# It will be easy to report substantial evidence if we take ratio of these different groups. The numbers themselves do not speak much

# In[39]:


friend_correlation=data.pivot_table(index="Have you ever tried to meet up with hometown friends on Thanksgiving night?",columns='Have you ever attended a "Friendsgiving?"',values="int_age")
friend_correlation


# In[40]:


friend_correlation_income=data.pivot_table(index="Have you ever tried to meet up with hometown friends on Thanksgiving night?",columns='Have you ever attended a "Friendsgiving?"',values="int_income")
friend_correlation_income


# **FINDINGS**
# 
# The ones with lower income and lower age seem to have attended Friendsgiving and tried to meet friends on Thanksgiving.
# The ones who havent done either have a higher income and belong to a higher age demographic.

# In[ ]:





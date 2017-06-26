
# coding: utf-8

# In[1]:


import csv


# In[2]:


f=open("guns.csv","r")
raw_data=csv.reader(f)
data=list(raw_data)


# In[3]:


data[0:5]


# In[4]:


headers=data[0]
data=data[1:len(data)]


# In[5]:


headers


# In[6]:


data[0:5]


# In[7]:


years=[year[1] for year in data]
year_counts={}
for year in years:
    if year in year_counts:
        year_counts[year]+=1
    else:
        year_counts[year]=1
print(year_counts)


# In[8]:


import datetime
dates=[datetime.datetime(year=int(date[1]),month=int(date[2]),day=1) for date in data]
dates[0:5]                         


# In[9]:


date_counts={}
for date in dates:
    if date not in date_counts:
        date_counts[date]=0
    date_counts[date]+=1
date_counts


# In[10]:


sexes=[sex[5] for sex in data]
sex_counts={}
for sex in sexes:
    if sex in sex_counts:
        sex_counts[sex]+=1
    else:
        sex_counts[sex]=1
sex_counts


# In[11]:


races=[race[7] for race in data]
race_counts={}
for race in races:
    if race in race_counts:
        race_counts[race]+=1
    else:
        race_counts[race]=1
race_counts


# **Learned so far**: Number of male victim is about 6 times higher compared to females Frequency of gun related occurences is in the range of 2200-3100/month and there is not much change YoY in gun related crimes/incidents

# In[12]:


g=open("census.csv","r")
raw_census=csv.reader(g)
census=list(raw_census)
census


# In[13]:


mapping={"Asian/Pacific Islander": 15159516 + 674625,
    "Native American/Native Alaskan": 3739506,
    "Black": 40250635,
    "Hispanic": 44618105,
    "White": 197318956}
race_per_hundredk={}
for race in race_counts:
    race_per_hundredk[race]=(race_counts[race]/mapping[race])*100000
print(race_per_hundredk)


# In[16]:


intents=[intent[3] for intent in data]
races=[race[7] for race in data]
homicide_race_counts={}
for i, race in enumerate(races):
    if intents[i]=="Homicide":
        if race in homicide_race_counts:
            homicide_race_counts[race]+=1
        else:
            homicide_race_counts[race]=1
homicide_race_counts


# In[24]:


race_per_hundredk={}
for race,j in homicide_race_counts.items():
    race_per_hundredk[race]=(j/mapping[race])*100000
race_per_hundredk


# **FINDINGS**
# Black community in the US disproportionately leads homicide related deaths in the US. Asian/Pacific Islander community has the lowest rate of being a target in a homicide related incident
# 
# **NEXT STEPS**
# Would like to further explore this disproportionate finding in southern US states for the black community as well as find the police involvement in the matter
# Another step is to use those findings and compare countries with the highest number of government killings to understand the plight of the black community

# In[ ]:





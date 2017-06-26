
# coding: utf-8

# In[1]:


f=open("US_births_1994-2003_CDC_NCHS.csv","r")
data=f.read()
data_split1=data.split("\n")
print(data_split1[0:10])


# In[5]:


def read_csv(file_name):
    f=open(file_name).read()
    info=f.split("\n")
    string_list=info[1:len(info)]
    final_list=[]
    for string in string_list:
        int_fields=[]
        string_fields=string.split(",")
        for val in string_fields:
            a=int(val)
            int_fields.append(a)
        final_list.append(int_fields)
    return(final_list)
cdc_list=read_csv("US_births_1994-2003_CDC_NCHS.csv")
print(cdc_list[0:10])    


# In[11]:


def month_births(list_lists):
    births_per_month={}
    for list in list_lists:
        month=list[1]
        births=list[4]
        if month in births_per_month:
            births_per_month[month]=births_per_month[month]+births
        else:
            births_per_month[month]=births
    return(births_per_month)
cdc_month_births=month_births(cdc_list)
print(cdc_month_births)               


# In[12]:


cdc_month_births


# In[15]:


def dow_births(list_list):
    births_ac_days={}
    for list in list_list:
        day_of_week=list[3]
        births=list[4]
        if day_of_week in births_ac_days:
            births_ac_days[day_of_week]=births_ac_days[day_of_week]+births
        else:
            births_ac_days[day_of_week]=births
    return(births_ac_days)
cdc_day_births=dow_births(cdc_list)
cdc_day_births


# In[20]:


def calc_counts(list_list,col):
    uni_dict={}
    for list in list_list:
        para=list[col]
        births=list[4]
        if para in uni_dict:
            uni_dict[para]=uni_dict[para]+births
        else:
            uni_dict[para]=births
    return(uni_dict)
cdc_year_births=calc_counts(cdc_list,0)
cdc_month_births=calc_counts(cdc_list,1)
cdc_dom_births=calc_counts(cdc_list,2)
cdc_dow_births=calc_counts(cdc_list,3)
cdc_year_births


# In[ ]:





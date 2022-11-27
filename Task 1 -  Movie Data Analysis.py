#!/usr/bin/env python
# coding: utf-8

# # Movie Data Analysis
# 

# In[ ]:





# # Importing Libraries

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# # Exploring dataset

# In[2]:


films=pd.read_csv("IMDB-Movie-Data.csv")
films


# In[3]:


#Display Top 5 Rows of The Dataset


films.head()


# In[4]:


#Check Last 10 Rows of The Dataset

films.tail()


# In[5]:


#Shape of Our Dataset

films.shape
print("Number of rows",films.shape[0])
print("Columns of number",films.shape[1])


# In[6]:


#Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement

films.info


# # Cleaning the Data

# In[7]:


#Check Missing Values In The Dataset

dataisnull=films.isnull().sum().sum()
print("Number of null values",dataisnull) 
dataisnullpercent=films.isnull().sum()*100/ len(films)
print("Number of null values in percent",dataisnullpercent)


# In[8]:


#map of dataset

sns.heatmap(films.isnull())


# In[9]:


#Droping null Values


films.dropna(axis=0)


# In[11]:


#Check For Duplicate Data


films_dup=films.duplicated().any()
print("Duplicate values: ",films_dup)


# In[12]:


films.drop_duplicates()


# # Getting the overall figures and basic statistics with their interpretation

# In[ ]:





# In[13]:


#Overall Statistics About The DataFrame


films.describe()


# In[16]:


#Display Title of The Movie Having Runtime Greater Than or equal to 180 Minutes

films[films["Runtime (Minutes)"]>=120]["Title"]


# In[17]:


#In Which Year There Was The Highest Average Voting?

films.groupby("Year")["Votes"].mean().sort_values(ascending=False)


# In[18]:


# Preparing the data for visualization


highestvote=films.groupby("Year")["Votes"].mean().sort_values(ascending=False).reset_index()
highestvoteyear=highestvote["Year"].tolist()
highestvotes=highestvote["Votes"].tolist()


# In[22]:


# Pie Chart 


plt.figure(figsize=(15,6))
plt.subplot(1,2,1)
colors=sns.color_palette('hls')[0:8]
explode=(0.2,0,0,0,0,0,0,0,0,0,0)
plt.pie(highestvotes,labels=highestvoteyear,autopct='%1.1f%%',explode=explode,shadow=True,colors=colors)
plt.title("The highest average voting over the years")


# In[24]:


#Which Year There Was The Highest Average Revenue?

films.groupby("Year")['Revenue (Millions)'].mean().sort_values(ascending=False)


# In[25]:


# Preparing the data for visualization

datarevenue=films.groupby("Year")['Revenue (Millions)'].mean().sort_values(ascending=False).reset_index()
datarevenuelabel=datarevenue['Year'].tolist()
datarevenuere=datarevenue["Revenue (Millions)"].tolist()


# In[30]:


# Barplot for data


plt.subplot(1,1,1)
sns.barplot(x="Year",y="Revenue (Millions)",data=datarevenue,palette=colors)
plt.title("Revenue (Millions)")
plt.show()


# In[31]:


#Number of films by years


datayears=films["Year"].value_counts().reset_index()
datayears=datayears.rename(columns={"index":"Year","Year":"Count"})
datayears


# In[32]:


datafyears=datayears["Year"].tolist()
datafmin=datayears["Count"].tolist()


# Pie

plt.figure(figsize=(15,6))
plt.subplot(1,2,1)
colors=sns.color_palette('hls')
explode=(0.2,0,0,0,0,0,0,0,0,0,0)
plt.pie(datafmin,labels=datafyears,data=datayears,colors=colors,shadow=True,explode=explode,autopct='%1.1f%%')
plt.title("Number of films by years")


# In[33]:


#Most Popular Movie  with Highest Revenue

films[films["Revenue (Millions)"].max()==films['Revenue (Millions)']]


# In[34]:


#Top 10 Highest Rated Movie Titles And its Directors


titdirector=films.nlargest(10,"Rating")[["Title","Rating","Director"]]
titdirector


# In[35]:


plt.figure(figsize=(13,6))

sns.barplot(y="Title",x="Rating",data=titdirector,hue="Director",dodge=False,palette=colors)
plt.title(" Display Top 10 Highest Rated Movie Titles And its Directors")
plt.legend(bbox_to_anchor=(1.05,1),loc=2)
plt.show()


# In[43]:


#genres of films

films.columns


# In[44]:


#spliting the movies
list1=[]
for item in films["Genre"]:
    list1.append(item.split(","))  
    
    
#we separate the genres
list2=[]
for item2 in list1:
    for item3 in item2:
        list2.append(item3)

        
# Number of genres
datagenree=pd.DataFrame(list2,columns=["Genre"]).reset_index()
datagenree=datagenree.drop(["index"],axis=1) 
datagenree.value_counts()


# In[45]:


#Efect of rating on revenue

plt.figure(figsize=(15,6))
sns.scatterplot(x="Rating",y="Revenue (Millions)",data=films)
plt.title("Rating & profit relationship")
plt.show()


# In[37]:


#classification of the movies by rating

def rating(movie):
    if movie.Rating>=7.0:
        return "High"
    elif movie.Rating<=6.0:
        return "Good"
    else:
        return "Average"

films["Rating words"]=films.apply(rating,axis="columns") 
films["Rating words"].value_counts()


# In[47]:


datawords=films["Rating words"].value_counts().reset_index()
datawords=datawords.rename(columns={"index":"Rating Words","Rating words":"Count"})
datawords=datawords.set_index("Rating Words")


plt.figure(figsize=(15,6))
plt.subplot(1,2,1)
colors=sns.color_palette('hls')
sns.barplot(x=datawords.index,y="Count",data=datawords,palette=colors)
plt.title("Rating number information")


plt.subplot(1,2,2)
sns.countplot(x="Year",hue="Rating words",data=films,palette=colors)
plt.title("Rating indicators by years")
plt.show()


# In[ ]:





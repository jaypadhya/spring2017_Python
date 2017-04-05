
# coding: utf-8

# # Movie awards analysis

# In[ ]:

import pandas as pd
import numpy as np
import os
import calendar


# In[3]:

currentWD = os.getcwd()
# Read the data from csv
movie_awards = pd.read_csv(currentWD+"/"+'movies_awards.csv')
#movie_awards To read the movie awards and understand the data


# In[6]:

movie_awards_lines = movie_awards['Awards'] # to fetch the awards columns and fetch the text from the columns


# In[7]:

movie_awards_lines = movie_awards_lines.dropna(axis=0,how='any') # To hide all the empty values 
movie_awards_lines=pd.DataFrame(movie_awards_lines)  
#movie_awards_lines to get the single column of awards with entire text


# In[8]:

movie_awards_lines['Awards_won'] = movie_awards['Awards'].str.extract("(\d+) win")
movie_awards_lines['Awards_nominated'] =  movie_awards['Awards'].str.extract("(\d+) nomination")
movie_awards_lines['Prime_Awards_won'] = movie_awards['Awards'].str.extract("Won (\d+) Primetime Emmy")
movie_awards_lines['Prime_Awards_nominated'] = movie_awards['Awards'].str.extract("Nominated for (\d+) Primetime Emmy")
movie_awards_lines['Oscar_Awards_nominated'] = movie_awards['Awards'].str.extract("Nominated for (\d+) Oscar")
movie_awards_lines['Oscar_Awards_won'] = movie_awards['Awards'].str.extract("Won (\d+) Oscar")
movie_awards_lines['Golden_Globe_Awards_nominated'] = movie_awards['Awards'].str.extract("Nominated for (\d+) Golden Globe")
movie_awards_lines['Golden_Globe_Awards_won'] = movie_awards['Awards'].str.extract("Won (\d+) Golden Globe")
movie_awards_lines['BAFTA_nominated'] = movie_awards['Awards'].str.extract("Nominated for (\d+) BAFTA")
movie_awards_lines['BAFTA_won'] = movie_awards['Awards'].str.extract("Won (\d+) BAFTA")


# In[9]:

final= movie_awards_lines.fillna(0)


# In[10]:

final['Awards_won'] = final['Awards_won'].astype(str).astype(int)
final['Prime_Awards_won'] = final['Prime_Awards_won'].astype(str).astype(int)
final['Oscar_Awards_won'] = final['Oscar_Awards_won'].astype(str).astype(int)
final['Golden_Globe_Awards_won'] = final['Golden_Globe_Awards_won'].astype(str).astype(int)
final['BAFTA_won'] = final['BAFTA_won'].astype(str).astype(int)


# In[11]:

final['Awards_nominated'] = final['Awards_nominated'].astype(str).astype(int)
final['Prime_Awards_nominated'] = final['Prime_Awards_nominated'].astype(str).astype(int)
final['Oscar_Awards_nominated'] = final['Oscar_Awards_nominated'].astype(str).astype(int)
final['Golden_Globe_Awards_nominated'] = final['Golden_Globe_Awards_nominated'].astype(str).astype(int)
final['BAFTA_nominated'] = final['BAFTA_nominated'].astype(str).astype(int)


# In[12]:

final['Total_Won'] = final['Awards_won'] + final['Prime_Awards_won'] + final['Oscar_Awards_won'] + final['Golden_Globe_Awards_won']+final['BAFTA_won']


# In[13]:

final['Total_Nominated'] = final['Awards_nominated'] + final['Prime_Awards_nominated']+ final['Oscar_Awards_nominated'] + final['Golden_Globe_Awards_nominated'] + final['BAFTA_nominated'] 


# In[14]:

final.head()


# In[37]:

final.to_csv("solution4_movie_analysis.csv",index = False, sep=',')


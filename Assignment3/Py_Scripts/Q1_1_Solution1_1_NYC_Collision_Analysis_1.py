
# coding: utf-8

# # NYC VEHICLE COLLISION ANALYSIS - Part 1

# In[34]:

import pandas as pd
import numpy as np
import os
import calendar
#Importing all the required libraries


# In[47]:

# get current working directory
currentWD = os.getcwd()
# read csv from the Current working directory
vehicle_collision = pd.read_csv(currentWD+"/"+"vehicle_collisions.csv")


# In[48]:

vehicle_collision.head() #how it looks


# In[49]:

vehicle_collision['DATE'] = pd.to_datetime(vehicle_collision['DATE']) # We convert the Date column in Date Time using function so we can fetch month name and date from the same


# In[4]:

vehicle_collision['MONTH'] = pd.DatetimeIndex(vehicle_collision['DATE']).month #We add the month and year column to understand month and year
vehicle_collision['YEAR'] = pd.DatetimeIndex(vehicle_collision['DATE']).year


# In[6]:

vehicle_collision_2016 = vehicle_collision[(vehicle_collision['YEAR']==2016)] #ONly 2016 data is needed


# In[21]:

vehicle_collision_2016_Manhattan = vehicle_collision_2016[(vehicle_collision_2016['BOROUGH']=='MANHATTAN')] #When Borough is manhattan


# In[24]:

vehicle_collision_2016_Manhattan.head()     #This shows how the frames loook like


# In[8]:

df_manhattan = vehicle_collision_2016_Manhattan.groupby([vehicle_collision_2016_Manhattan['MONTH']]).count() #We groupby on monthly basis to get a count


# In[9]:

df_manh_2016 = df_manhattan['UNIQUE KEY'] # To get instances of the accidents by unique keys in Manhattan


# In[10]:

df_newYork = vehicle_collision_2016.groupby([vehicle_collision_2016['MONTH']]).agg('count') #Creates index column with aggregating count


# In[25]:

df_newYork_2016 = df_newYork['UNIQUE KEY'] #To get instances of the accidents by unique keys in New York Overall


# In[26]:

result = pd.concat([df_manh_2016,df_newYork_2016],axis=1)
result.columns.values[0]= "MANHATTAN"
result.columns.values[1]= "NYC"
#result This will show month index, Manhattan and NYC


# In[27]:

result['PERCENTAGE']=result[['MANHATTAN']].div(result['NYC'],axis=0)
#result This will add the percentage column after dividing the first two columns


# In[28]:

result['PERCENTAGE']=result['PERCENTAGE'].apply(lambda x:x*100) #TO Calculate % we need to multiple 100 to last row


# In[29]:

result['MONTH'] = result.index.get_level_values('MONTH') #Adding the value of index from 1,2,3.. to Jan, Feb, March...etc


# In[30]:

finalresult = result[['MONTH','MANHATTAN','NYC','PERCENTAGE']]
finalresult.head()


# In[216]:

finalresult.to_csv('Q1_Solution1_1',index=False,sep=',') #No indexing to get get csv without csv



# coding: utf-8

#  # NYC VEHICLE COLLISION ANALYSIS - Part 2

# In[49]:

import pandas as pd
import numpy as np
import os
import calendar


# In[50]:

# get current working directory
currentWD = os.getcwd()
# read csv from the Current working directory
vehicle_collision = pd.read_csv(currentWD+"/"+"vehicle_collisions.csv")


# In[51]:

df_vehicle_collison = vehicle_collision[['UNIQUE KEY','BOROUGH','VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE',]] # seletcing only the required columns


# In[52]:

df_location = df_vehicle_collison[['UNIQUE KEY','BOROUGH']]
df_vehicletype = df_vehicle_collison[['VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE']]
df_vehicletype = df_vehicletype.notnull()
df_vehicletype = df_vehicletype.applymap(lambda x:1 if x else 0) #Applying lambda for 0 or 1 as per Null or Not null


# In[53]:

result = pd.concat([df_location,df_vehicletype],axis=1) #Concat on rows as per location and vehicle type


# In[54]:

result = result.groupby('BOROUGH').sum() #Summing up over the group by over Borogh


# In[55]:

result['ONE_VEHICLE_INVOLVED'] =  result['VEHICLE 1 TYPE']-result['VEHICLE 2 TYPE'] #Substract one from two to get only one


# In[56]:

result['TWO_VEHICLES_INVOLVED'] =  result['VEHICLE 2 TYPE']-result['VEHICLE 3 TYPE'] #Substract three from two to get only two


# In[57]:

result['THREE_VEHICLES_INVOLVED'] =  result['VEHICLE 3 TYPE']-result['VEHICLE 4 TYPE'] #Substract three from four to get only three


# In[58]:

result['MORE_VEHICLES_INVOLVED'] = result['VEHICLE 4 TYPE']  #To get 3+ vehicles, only 4 or 5 vehicles


# In[59]:

final_result = result[['ONE_VEHICLE_INVOLVED','TWO_VEHICLES_INVOLVED','THREE_VEHICLES_INVOLVED','MORE_VEHICLES_INVOLVED']]
final_result.head()# We wanted to show all the top 5 rows


# In[33]:

final_result.to_csv("Q1_Solution1_2.csv",index=True,sep=',')# indexing to get get csv without csv


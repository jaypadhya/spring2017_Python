
# coding: utf-8

# # Employee Compensation Part 1

# In[2]:

import pandas as pd
import numpy as np
import os
import calendar


# In[27]:

# get current working directory
currentWD = os.getcwd()

# read csv
employee_compensation = pd.read_csv(currentWD+"/"+"employee_compensation.csv")
employee_compensation.head()


# In[28]:

result = employee_compensation.groupby(['Organization Group','Department']).mean().reset_index()
#result to see how it looks like


# In[29]:

final_result = result[['Organization Group','Department','Total Compensation']] # In order to only have selective columns


# In[34]:

final= final_result.sort(['Organization Group','Total Compensation'],ascending=False).groupby(['Organization Group'])


# In[41]:

final_result = final.head(100)
final_result.head() # To have headers for final result


# In[40]:

final_result.to_csv('Q2_Solution2_1_Employee_Compensation.csv') # write to csv


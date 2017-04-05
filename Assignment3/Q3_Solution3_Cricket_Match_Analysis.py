
# coding: utf-8

# # Cricket Match Analysis 

# In[4]:

import pandas as pd
import numpy as np
import os
import calendar


# In[6]:

currentWD = os.getcwd()
# Read the data from csv
crcket_data =  pd.read_csv(currentWD+"/"+'cricket_matches.csv') 


# In[7]:

crcket_data['is_in']  = crcket_data['home'].str.strip().str.lower() == crcket_data['winner'].str.strip().str.lower() # we compare home and winner on same lines as we need to find home and winner team 


# In[8]:

cric_home_winner = crcket_data[(crcket_data['is_in'])]
#cric_home_winner this will provide with 


# In[10]:

cric_home_winner['is_inning_1'] = cric_home_winner['home'].str.strip().str.lower() == cric_home_winner['innings1'].str.strip().str.lower()


# In[11]:

cric_home_winner_inning1 = cric_home_winner[(cric_home_winner['is_inning_1'])]
#cric_home_winner_inning1


# In[12]:

cric_runs_inning1 = cric_home_winner_inning1.groupby('home').sum() # grouping by home and summing over for calculating runs


# In[14]:

cric_inning_df = cric_runs_inning1.reset_index() # To make columns as index


# In[15]:

final_inning1 = cric_inning_df[['home','innings1_runs','is_inning_1']] 
# final_inning1


# In[16]:

cric_home_winner['is_inning_2'] = cric_home_winner['home'].str.strip().str.lower() == cric_home_winner['innings2'].str.strip().str.lower()


# In[17]:

cric_home_winner_inning2 = cric_home_winner[(cric_home_winner['is_inning_2'])] # Similarly for innings 2


# In[18]:

cric_runs_inning2 = cric_home_winner_inning2.groupby('home').sum() # Like innings 1


# In[19]:

cric_inning_df2 = cric_runs_inning2.reset_index() # index as columns


# In[20]:

final_inning2 = cric_inning_df2[['home','innings2_runs','is_inning_2']] 
#final_inning2


# In[27]:

result = pd.merge(final_inning1,final_inning2, on='home', how='outer') # Outer merge for combining both of them
result.head()


# In[29]:

result['innings2_runs'] = result['innings2_runs'].fillna(0)
result['innings1_runs'] = result['innings1_runs'].fillna(0)
result['is_inning_1'] = result['is_inning_1'].fillna(0)
result['is_inning_2'] = result['is_inning_2'].fillna(0)
# Filling up results with NA values
result.head()


# In[38]:

result['Total_innings'] = result['is_inning_1'] + result['is_inning_2']
result['Total_runs'] = result['innings1_runs'] + result['innings2_runs']
result['Average'] = result['Total_runs']/result['Total_innings']
final_result = result[['home','Average']]
final_result.head()


# In[37]:

final_result.to_csv('Q3_Solution3_cricket_analysis.csv', sep=',')


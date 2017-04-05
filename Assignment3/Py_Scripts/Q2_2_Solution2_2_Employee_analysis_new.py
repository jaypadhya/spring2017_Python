
# coding: utf-8

# # Solution2_2 Employee_analysis

# In[ ]:

import pandas as pd
import os


# In[11]:

# get current working directory
currentWD = os.getcwd()
# read csv
df = pd.read_csv(currentWD+"/"+"employee_compensation.csv")
df.head()


# In[18]:

job_comp=df[(df['Year Type']=='Calendar')] # Only seetcing the calendar and then group by emploee and family later
job_comp=pd.DataFrame(job_comp.groupby(['Employee Identifier','Job Family']).mean())

job_comp.drop(['Year', 'Organization Group Code','Union Code'], axis=1, inplace=True)
job_comp.head()


# In[13]:

overtime=job_comp[(job_comp['Overtime']>(.05*job_comp['Salaries']))]
overtime.head()


# In[14]:

top_family=overtime
top_family=top_family.groupby([top_family.index.get_level_values(1)]).mean()


# In[16]:

top_family=top_family[['Total Benefits','Total Compensation']]
top_family['Percent_Total_Benefit']=100*(top_family['Total Benefits']/top_family['Total Compensation'])
top_family=top_family.sort_values(['Percent_Total_Benefit'], ascending=[False])
top_family.head(5)


# In[17]:

top_family.to_csv('Q2_Part_2_Output.csv')


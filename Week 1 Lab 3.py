# Pandas is a software library written for the Python programming language for data manipulation and analysis.
import pandas as pd
#NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays
import numpy as np

df=pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_1.csv")

# %%
df.head(10)

# %%
df.isnull().sum()/len(df)*100

# %%
df.dtypes

# %%
# Apply value_counts() on column LaunchSite
df.value_counts(['LaunchSite'])

# %%
# Apply value_counts on Orbit column
df.value_counts(['Orbit'])

# %%
# landing_outcomes = values on Outcome column
landing_outcomes = df.value_counts(['Outcome'])

# %%
for i,outcome in enumerate(landing_outcomes.keys()):
    print(i,outcome)
    
# %%
bad_outcomes=set(landing_outcomes.keys()[[1,3,5,6,7]])
bad_outcomes

# %%
# landing_class = 0 if bad_outcome
# landing_class = 1 otherwise
bad_outcomes=set(landing_outcomes.keys()[[1,3,5,6,7]])

landing_class = []
for index, row in df.iterrows():
    Outcome = row['Outcome']
    if Outcome == 'False ASDS' or Outcome == 'False Ocean' or Outcome == 'None ASDS' or Outcome == 'False RTLS' or Outcome == 'None None':
        landing_class.append(0)
    else:
        landing_class.append(1)
        
# %%
df['Class']=landing_class
df[['Class']].head(8)
df.value_counts(['Outcome'])

# %%
df["Class"].mean()

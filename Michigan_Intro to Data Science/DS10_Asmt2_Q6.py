# Include Pandas and set up the file setup

import pandas as pd
import numpy as np
census_df = pd.read_csv('census.csv')

# Question 6 - What are the three most populous states - in order, using only 3 most populous counties
columns_to_keep = ['SUMLEV', 'STNAME', 'CTYNAME', 'CENSUS2010POP']
df = census_df[columns_to_keep]
state_names = df[df['SUMLEV'] == 40]
state_list = pd.Series(state_names['STNAME'])
all_states = pd.Series({}, dtype='float')
for state in state_list:
    counties = df[df['STNAME'] == state]
    counties = counties.sort_values(by='CENSUS2010POP', ascending=False)
    top_3_array = counties[['CENSUS2010POP']].to_numpy()
    top_3_pop = sum(top_3_array[1:4])
    s = pd.Series({state: top_3_pop})
    all_states = all_states.append(s)
all_states = all_states.sort_values(ascending=False)
top_3_states = all_states.iloc[0:3]
print('The three most populous states in order (using the 3 most populous counties) are:')
print(top_3_states)
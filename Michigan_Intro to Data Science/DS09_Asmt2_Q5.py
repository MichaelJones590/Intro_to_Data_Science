# Include Pandas, Numpy, and set up the file setup

import pandas as pd
census_df = pd.read_csv('census.csv')

# Question 5 - Which state has the most counties in it?
columns_to_keep = ['SUMLEV', 'STNAME', 'CTYNAME']
df = census_df[columns_to_keep]
states = df[df['SUMLEV'] == 40]
state_list = pd.Series(states['STNAME'])
all_states = pd.Series({})
for state in state_list:
    counties = df[df['STNAME'] == state]
    county_total = len(counties.index) - 1
    s = pd.Series({state: county_total})
    all_states = all_states.append(s)
all_states = all_states.sort_values()
last = all_states.size - 1
largest_state = all_states.index[last]
largest_st_counties = all_states.values[last]
#print(all_states)
#print()
print('The state with the most counties is:', largest_state, 'with', largest_st_counties)
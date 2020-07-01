# Include Pandas and set up the file setup

import pandas as pd
import numpy as np
census_df = pd.read_csv('census.csv')

# Question 7 - Which county has had the largest absolute change in population within the period 2010-2015?
# Select 2010-2015 population columns and keep only the county records (i.e. eliminate state summary records)
# Note:  There is a LOT of missing data in the POPESTIMATE20xx columns

columns_to_keep = ['SUMLEV', 'STNAME', 'CTYNAME', 'POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015']
df = census_df[columns_to_keep]

# Set up state and county name lists for loops
state_names = df[df['SUMLEV'] == 40]
state_list = pd.Series(state_names['STNAME'])
all_counties = pd.Series({}, dtype='int')
for state in state_list:
    county_df = df[df['STNAME'] == state]
    county_names = county_df[county_df['SUMLEV'] == 50]
    county_list = pd.Series(county_names['CTYNAME'])
    for county in county_list:
        county_df = county_df[county_df['CTYNAME'] == county]
        if county_df.empty == False:
            county_pop_array = []
            county_pop_array.append(county_df.iloc[0]['POPESTIMATE2010'])
            county_pop_array.append(county_df.iloc[0]['POPESTIMATE2011'])
            county_pop_array.append(county_df.iloc[0]['POPESTIMATE2012'])
            county_pop_array.append(county_df.iloc[0]['POPESTIMATE2013'])
            county_pop_array.append(county_df.iloc[0]['POPESTIMATE2014'])
            county_pop_array.append(county_df.iloc[0]['POPESTIMATE2015'])
            county_pop_array = np.sort(county_pop_array)
            county_change = county_pop_array[5] - county_pop_array[0]
            s = pd.Series({county: county_change})
            all_counties = all_counties.append(s)
        else:
            pass

all_counties = all_counties.sort_values(ascending=False)
print('The county with the largest absolute change in population within the period 2010-2015 is:', all_counties.iloc[[0]])

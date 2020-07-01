# Include Pandas and set up the file setup

import pandas as pd
census_df = pd.read_csv('census.csv')

# Question 8 - Create a query thatfinds the countie that belong to regions 1 or 2, whose name starts with 'Washington', and whose POPESTIMATE2015
# was greater than their POPESTIMATE 2014. 

columns_1 = ['SUMLEV', 'STNAME', 'CTYNAME', 'REGION', 'POPESTIMATE2014', 'POPESTIMATE2015']
df = census_df[columns_1]

wcdf = df[(df['REGION'] == 1) | (df['REGION'] == 2)]
wcdf = wcdf[wcdf['CTYNAME'].str.startswith('Washington')]
wcdf = wcdf[wcdf['POPESTIMATE2015'] > wcdf['POPESTIMATE2014']]
columns_2 = ['STNAME', 'CTYNAME']
wcdf = wcdf[columns_2]
wcdf.sort_index()
print(wcdf)
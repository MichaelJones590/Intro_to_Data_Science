# Include the file setup

import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')

# Question 4 - Create a series called "Points" which is a weighted value across gold (3 pts), silver (2 pts), bronze (1 pt).
# The series should include country names as indices.

columns_to_keep = ['Gold.2', 'Silver.2', 'Bronze.2']
print(df[columns_to_keep])
print()
gold_points = pd.Series(df['Gold.2'] * 3)
silver_points = pd.Series(df['Silver.2'] * 2)
bronze_points = pd.Series(df['Bronze.2'])
points = gold_points + silver_points + bronze_points
print(points)
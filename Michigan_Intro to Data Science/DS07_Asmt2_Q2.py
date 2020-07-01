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

# Question 2 - Which country had the biggest difference between their summer and winter gold medal counts?

summer_gold = pd.Series(df['Gold'])
winter_gold = pd.Series(df['Gold.1'])
gold_diff = summer_gold - winter_gold
gold_diff = gold_diff.sort_values()
last = gold_diff.size - 1
last_value = int(gold_diff.values[last])
first_value = int(gold_diff.values[0])
if first_value < 0:
    first_value *= -1
if first_value > last_value:
    largest_diff_country = gold_diff.index[0]
    largest_diff_medals = gold_diff.values[0]
else:
    largest_diff_country = gold_diff.index[last]
    largest_diff_medals = gold_diff.values[last]
print('The country with the biggest difference between summer and winter gold medal counts is:', largest_diff_country, 'with', largest_diff_medals)

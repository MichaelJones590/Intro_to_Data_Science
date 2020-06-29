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

# Question 3 - Which country has the biggest difference between their summer and winter gold medal counts relative to their total gold medal count?
# Only include countries that have won at least 1 gold in both summer and winter.

df_gt1 = df.where(df['Gold'] > 0)
df_gt1 = df_gt1.where(df['Gold.1'] > 0)
df_gt1 = df_gt1.dropna()
summer_gold = pd.Series(df_gt1['Gold'])
winter_gold = pd.Series(df_gt1['Gold.1'])
gold_diff = ((summer_gold - winter_gold) / (summer_gold + winter_gold))
gold_diff = gold_diff.sort_values()
last = gold_diff.size - 1
last_value = gold_diff.values[last]
first_value = gold_diff.values[0]
if first_value < 0:
    first_value *= -1
if first_value > last_value:
    largest_diff_country = gold_diff.index[0]
    largest_diff_medals = gold_diff.values[0]
else:
    largest_diff_country = gold_diff.index[last]
    largest_diff_medals = gold_diff.values[last]
largest_diff_medals *= 100
print('The country with the biggest difference between summer and winter gold medal counts relative to total is:', largest_diff_country, 'with', largest_diff_medals, 'percent.')

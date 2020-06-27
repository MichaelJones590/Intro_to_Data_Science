import pandas as pd
import numpy as np
sports = {'Archery': 'Bhutan', 'Golf': 'Scotland', 'Sumo': 'Japan', 'Taekwondo': 'South Korea'}
s = pd.Series(sports)
print(s)
print()
print(s.iloc[2])
print(s.loc['Archery'])
print()
#
s = pd.Series([100.00, 120.00, 101.00, 3.00])
print(s)
print()
total = np.sum(s)
print(total)
#
s = pd.Series(np.random.randint(0, 50, 15))
print('Length is', len(s))
print(s.head())
print()
#
original_sports = pd.Series({'Archery': 'Bhutan', 'Golf': 'Scotland', 'Sumo': 'Japan', 'Taekwondo': 'South Korea'})
cricket_loving_countries = pd.Series(['Australia', 'Barbados', 'Pakistan', 'England'], index=['Cricket', 'Cricket', 'Cricket', 'Cricket'])
all_countries = original_sports.append(cricket_loving_countries)
print('Original\n', original_sports)
print()
print('Cricket\n', cricket_loving_countries)
print()
print('All countries\n', all_countries)
print()
print('Cricket from all\n', all_countries.loc['Cricket'])

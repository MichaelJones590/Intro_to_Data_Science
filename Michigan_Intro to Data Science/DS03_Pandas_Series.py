import pandas as pd
import numpy as np
sports = {'Archery': 'Bhutan', 'Golf': 'Scotland', 'Sumo': 'Japan', 'Taekwondo': 'Japan'}
s = pd.Series(sports)
print(s)
print()
print(s.index)
print()
new_series = pd.Series(['Tiger', 'Bear', 'Moose'], index=['India', 'America', 'Canada'])
print(new_series)
print()
print(new_series.index)
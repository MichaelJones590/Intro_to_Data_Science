import pandas as pd
import numpy as np
purchase_1 = pd.Series({'Name': 'Chris', 'Item Purchased': 'Dog Food', 'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn', 'Item Purchased': 'Kitty Litter', 'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod', 'Item Purchased': 'Bird Seed', 'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
#print(df.loc[:,['Name', 'Item Purchased']])
#print()
#print(df.drop('Store 2'))
copy_df = df.copy()
copy_df = copy_df.drop('Store 1')
print(copy_df)
print()
print(df)
print()
df['Location'] = None
df['Cost'] *= .8
print(df)
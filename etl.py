import pandas as pd
import math

#Extract
df = pd.read_csv('sample_products.csv')

#Transform
df['unit_price'] = df['unit_price'].apply(math.ceil)

#Load
df.to_csv('output/clean_products.csv', index=False)

print('ok2')
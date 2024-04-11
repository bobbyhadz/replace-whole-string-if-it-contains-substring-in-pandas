# Replace whole String if it contains Substring in Pandas

import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl', 'Dan'],
    'job': ['dev', 'web dev', 'accountant', 'dev']
})

print(df)

df.loc[df['job'].str.contains('dev'), 'job'] = 'developer'

print('-' * 50)

print(df)
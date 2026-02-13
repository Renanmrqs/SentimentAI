import pandas as pd

df = pd.read_csv('data/IMDB Dataset.csv')
print('dataset shape: ', df.shape)
print('colums: ', df.columns.tolist())
print('\nfirst 5 rows: ', df.head(5))
print('\nsentiment distribution: ', df['sentiment'].value_counts())
print(f'\nAverage words per review: {df['review'].apply(lambda x: len(x.split())).mean():.0f}')
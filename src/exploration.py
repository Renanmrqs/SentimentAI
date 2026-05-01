import pandas as pd

# df = pd.read_csv('data/IMDB Dataset.csv')
# print('dataset shape: ', df.shape)
# print('colums: ', df.columns.tolist())
# print('\nfirst 5 rows: ', df.head(5))
# print('\nsentiment distribution: ', df['sentiment'].value_counts())
# print(f'\nAverage words per review: {df['review'].apply(lambda x: len(x.split())).mean():.0f}')
columns = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']


df = pd.read_csv('data/2018_train_data.csv')
df['label'] = df[columns].any(axis=1).astype(int)

# print('dataset shape: ', df.shape)
# print('colums: ', df.columns.tolist())
# print('\nfirst 5 rows: ', df.head(5))
# print('\nsentiment distribution: ', df['label'].value_counts())
# print(f'\nAverage words per review: {df['comment_text'].apply(lambda x: len(x.split())).mean():.0f}')
toxics = df[df['label'] == 1] 
normals = df[df['label'] == 0].sample(n=len(toxics), random_state=42) 
df_balanced = pd.concat([toxics, normals]).reset_index(drop=True)
print(df_balanced)
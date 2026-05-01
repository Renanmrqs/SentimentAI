import pandas as pd
from utils import cleaning_text


print('\n' + '='*60)
print('aplicando a limpeza no dataset completo')
print('\n' + '='*60)




df = pd.read_csv('data/2018_train_data.csv')
columns = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']
df['label'] = df[columns].any(axis=1).astype(int)

toxics = df[df['label'] == 1] 
normals = df[df['label'] == 0].sample(n=len(toxics), random_state=42) 

df_balanced = pd.concat([toxics, normals]).reset_index(drop=True)

print(f'\nProcessando {len(df_balanced)} reviws...')

df_balanced['comments_cleaned'] = df_balanced['comment_text'].apply(cleaning_text)

# analise dos dados limpos
for i in range(3):
    print(f'\n--- comments {i+1} ---')
    print(f'normal {len(df.iloc[i]['comment_text'].split())} palavras):')
    print(df.iloc[i]['comment_text'][:200], '...')
    #print(f'\nLimpa ({len(df.iloc[i]['comments_cleaned'].split())} palavras):')
    #print(df.iloc[i]['comments_cleaned'][:200])

df_balanced.to_csv('data/toxic_comments_cleaned.csv', index=False)
print('data/toxic_comments_cleaned.csv')

# df = pd.read_csv('data/IMDB Dataset.csv')

# print(f'\nProcessando {len(df)} reviws...')

# df['review_cleaned'] = df['review'].apply(cleaning_text)

# for i in range(3):
#     print(f'\n--- review {i+1} ---')
#     print(f'normal {len(df.iloc[i]['review'].split())} palavras):')
#     print(df.iloc[i]['review'][:200], '...')
#     print(f'\nLimpa ({len(df.iloc[i]['review_cleaned'].split())} palavras):')
#     print(df.iloc[i]['review_cleaned'][:200])

# df.to_csv('data/IMDB_Cleaned.csv', index=False)
# print('salvo em: data/IMDB_Clened.csv')

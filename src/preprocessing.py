import pandas as pd
from utils import cleaning_text


print('\n' + '='*60)
print('aplicando a limpeza no dataset completo')
print('\n' + '='*60)

df = pd.read_csv('data/IMDB Dataset.csv')

print(f'\nProcessando {len(df)} reviws...')

df['review_cleaned'] = df['review'].apply(cleaning_text)

for i in range(3):
    print(f'\n--- review {i+1} ---')
    print(f'normal {len(df.iloc[i]['review'].split())} palavras):')
    print(df.iloc[i]['review'][:200], '...')
    print(f'\nLimpa ({len(df.iloc[i]['review_cleaned'].split())} palavras):')
    print(df.iloc[i]['review_cleaned'][:200])

df.to_csv('data/IMDB_Cleaned.csv', index=False)
print('salvo em: data/IMDB_Clened.csv')
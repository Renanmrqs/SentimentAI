import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from src.utils import predict_sentiment
import pickle

df = pd.read_csv('data/IMDB_Cleaned.csv')
print(f'review loaded: {len(df)}')

x = df['review_cleaned']
y = df['sentiment']
print(x)
print(y)
print(f'size x: {x.shape}')
print(f'size y: {y.shape}')



x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print(f'training: {len(x_train)} reviews')
print(f'test: {len(x_test)} reviews')
vectorizer = TfidfVectorizer(max_features=5000)
x_train_tfidf = vectorizer.fit_transform(x_train)
x_test_tfidf = vectorizer.transform(x_test)
print(f'vocabulary: {len(vectorizer.get_feature_names_out())} words')


model = LogisticRegression(max_iter=1000)
model.fit(x_train_tfidf, y_train)


print('testing model')
y_pred = model.predict(x_test_tfidf)


accuracy = accuracy_score(y_test, y_pred)
print(f'acuracy: {accuracy*100:.2f}%')
print(classification_report(y_test, y_pred))


with open('models/sentiment_model.pkl', 'wb') as f:
    pickle.dump(model, f)
with open('models/vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)
    
exemple = [
    'This movie was absolutely amazing! I loved every minute.',
    'Terrible waste of time. Worst film I`ve ever seen',
    'It was okay, nothing special',
]

for text in exemple:
    sentiment, trust = predict_sentiment(text)
    print(f'n/text: {text}')
    print(f'predict: {sentiment.upper()} ({trust*100:.1f}% confiance)')
    





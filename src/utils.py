import re
import nltk
import os
import pickle
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', quiet=True)

with open('models/sentiment_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('models/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

def cleaning_text(text):
    from nltk.corpus import stopwords
    text = text.lower()
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    stop_words = set(stopwords.words('english'))
    words = text.split()
    words_filtred = [word for word in words if word not in stop_words]
    text_cleaned = ' '.join(words_filtred)
    return text_cleaned

def predict_sentiment(text):
    from nltk.corpus import stopwords
    
    text_cleaned = cleaning_text(text)
    
    text_tfidf = vectorizer.transform([text_cleaned])
    prediction = model.predict(text_tfidf)[0]
    trust = model.predict_proba(text_tfidf)[0]
    
    return prediction, max(trust)


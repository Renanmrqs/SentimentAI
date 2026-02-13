import streamlit as st
from src.utils import cleaning_text, predict_sentiment
from deep_translator import GoogleTranslator

st.title('SentimentAI')
send_message = st.text_area('Escreva sua review (Em qualquer idioma):')
send_message_button = st.button('Enviar review')
if send_message_button:
    if send_message:
        translator = GoogleTranslator(source='auto', target='en')
        text_en = translator.translate(send_message)
        
        if send_message != text_en:
            st.info(f'Tradução: {text_en}')
        
        text_cleaned = cleaning_text(text_en)
        sentiment, trust = predict_sentiment(text_cleaned)
        st.subheader('Sua review: ')
        if sentiment == 'positive':
            st.info(f'Review positiva! {trust*100:.1f}% de confiança.')
        else:
            st.info(f'Review negativa! {trust*100:.1f}% de confiança.')
    
    
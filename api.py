from fastapi import FastAPI
from src.utils import cleaning_text, predict_sentiment,predict_comments
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from deep_translator import GoogleTranslator
from langdetect import detect

class Text(BaseModel):
    text: str

def translator(text):
    if detect(text) != 'en':
        translator = GoogleTranslator(source='auto', target='en')
        text_translated = translator.translate(text)
        return text_translated 
    else:
        return text


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

@app.post("/predict")
def input_user(item: Text): 
    text_cleaned = cleaning_text(item.text)
    sentiment, trust = predict_sentiment(text_cleaned)
    return {'sentiment': sentiment, 'trust': trust}

@app.post("/toxic_predict")
def input_toxic_comment(item: Text): 
    text_translated = translator(item.text)
    result, trust = predict_comments(text_translated)
    
    if result == 1:
        result = "toxic" 
    else:
        result = "safe"
    return {'toxic': result, 'trust': (trust)}

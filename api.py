from fastapi import FastAPI
from src.utils import cleaning_text, predict_sentiment
from pydantic import BaseModel


class Text(BaseModel):
    text: str


app = FastAPI()

@app.post("/predict")
def input_user(item: Text): 
    text_cleaned = cleaning_text(item.text)
    sentiment, trust = predict_sentiment(text_cleaned)
    return {'sentiment': sentiment, 'trust': trust}


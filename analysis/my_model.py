import pandas as pd
import joblib

v=joblib.load("vectorizer.pkl")
model=joblib.load("sentiment_analysis_model.pkl")

def prediction(text):
    t=v.transform([text])
    res=model.predict(t)
    if res[0]==1:
        return "postive"
    else: return "negative"



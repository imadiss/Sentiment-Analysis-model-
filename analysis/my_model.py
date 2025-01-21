import pandas as pd
import joblib

v=joblib.load("vectorizer2.pkl")
model=joblib.load("sentiment_analysis_model2.pkl")





def prediction(text):
    t=v.transform([text])
    res=model.predict(t)
    if res[0]==1:
        return "Postive"
    elif res[0]==0:
        return "Neutral"
    else: return "Negative"



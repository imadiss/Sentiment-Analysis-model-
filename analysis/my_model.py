import pandas as pd
import joblib

v=joblib.load("vectorizer3.pkl")
model=joblib.load("sentiment_analysis_model3.pkl")





def prediction(text):
    t=v.transform([text])
    res=model.predict(t)
    if res[0]==1:
        return "Postive"
    elif res[0]==0:
        return "Neutral"
    else: return "Negative"



import pandas as pd

df=pd.read_csv('Dataset/Train.csv')
df=df.dropna()
df['text']=df['text'].str.lower()

df_test=pd.read_csv('Dataset/Train.csv')
df=df.dropna()
df_test['text']=df_test['text'].str.lower()


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression


model=LogisticRegression()



x=df['text']
v=CountVectorizer()
x=v.fit_transform(x)
y=df['label'].to_numpy()

model.fit(x,y)

x_test=v.transform(df_test['text'])
y_test=df_test['label'].to_numpy()
y_predict=model.predict(x_test)

def prediction(text):
    t=v.transform([text])
    res=model.predict(t)
    if res[0]==1:
        return "postive"
    else: return "negative"
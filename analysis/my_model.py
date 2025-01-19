import pandas as pd

df=pd.read_csv("C:\\Users\\asus\\Downloads\\archive (3)\\Train.csv")
df=df.dropna()
df['text']=df['text'].str.lower()

df_test=pd.read_csv("C:\\Users\\asus\\Downloads\\archive (3)\\Test.csv")
df=df.dropna()
df_test['text']=df_test['text'].str.lower()

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier


model1=svm.SVC(kernel='linear')
model2=RandomForestClassifier(n_estimators=100)
model3=MultinomialNB()
model4=LogisticRegression()
model5=DecisionTreeClassifier()

model=model4



x=df['text']
v=CountVectorizer()
x=v.fit_transform(x)
y=df['label'].to_numpy()
#x_train,x_test,y_train,y_test=train_test_split(x_num,y,random_state=1,test_size=0.2)
model.fit(x,y)

x_test=v.transform(df_test['text'])
y_test=df_test['label'].to_numpy()
y_predict=model.predict(x_test)
print('Accuracy: ',str(accuracy_score(y_test,y_predict)*100)+'%')
print('Report:\n',classification_report(y_test, y_predict))

def prediction(text):
    t=v.transform([text])
    res=model.predict(t)
    if res[0]==1:
        return "postive"
    else: return "negative"
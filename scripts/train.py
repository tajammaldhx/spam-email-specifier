import json, sys
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score
root=Path(__file__).resolve().parents[1]
df=pd.read_csv(sys.argv[1],encoding='latin-1')[['v1','v2']].drop_duplicates()
xtr,xte,ytr,yte=train_test_split(df.v2,df.v1.map({'ham':0,'spam':1}),test_size=.2,random_state=42,stratify=df.v1.map({'ham':0,'spam':1}))
v=TfidfVectorizer(); a=v.fit_transform(xtr); m=MultinomialNB().fit(a,ytr); pred=m.predict(v.transform(xte))
metrics={'accuracy':accuracy_score(yte,pred),'precision':precision_score(yte,pred),'recall':recall_score(yte,pred),'records':len(df),'train':len(xtr),'test':len(xte)}
model={'vocabulary':{k:int(i) for k,i in v.vocabulary_.items()},'idf':v.idf_.tolist(),'logProb':m.feature_log_prob_.tolist(),'prior':m.class_log_prior_.tolist(),'metrics':metrics}
(root/'dist/model.json').write_text(json.dumps(model,separators=(',',':')))
print(metrics)

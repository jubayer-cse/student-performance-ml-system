import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

data = {
'attendance':[80,60,90,40,70,85],
'study_hours':[3,1,4,1,2,3],
'previous_score':[75,50,85,40,65,80],
'internal_marks':[70,45,80,35,60,75],
'participation':[7,4,8,3,6,7],
'result':[1,0,1,0,1,1]
}

df = pd.DataFrame(data)
X = df.drop('result',axis=1)
y = df['result']

model = RandomForestClassifier()
model.fit(X,y)

pickle.dump(model, open("model.pkl","wb"))

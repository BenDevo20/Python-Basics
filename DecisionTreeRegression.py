import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score

dataset = pd.read_csv('Startups_Invest.csv')
X = dataset.iloc[:,:-1]
Y = dataset.iloc[:, 4]

state = pd.get_dummies(X.iloc[:,3],drop_first=True)
X.drop('State',axis=1,inplace=True)
X = pd.concat([X,state],axis=1)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=0)
decisionregressor = DecisionTreeRegressor()
decisionregressor.fit(X_train,Y_train)
Y_pred = decisionregressor.predict(X_test)

score = r2_score(Y_test,Y_pred)
print(score)

import  pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data=pd.read_csv("C:\\Users\\Jang\\Desktop\\Coding Program\\pyton\\서울특별시 전월세가 정보_2019.\\서울특별시 전월세가 정보_2019.csv",encoding='CP949',sep=";")
data.head()
data.info()

df=data
df=df[["자치구명","층","임대면적","전월세구분","보증금","임대료"]]



df.isna().sum()
df=df.dropna(axis=0,how='any')

X=df[["층","임대면적","보증금"]]
y=df["임대료"]
X.shape
y.shape


X_train,x_test,y_train,y_test=train_test_split(X,y,train_size=0.8,test_size=0.2)

mlr=LinearRegression()
mlr.fit(X_train,y_train)


my_predict=mlr.predict(x_test)
my_predict


import matplotlib.pyplot as plt
plt.scatter(y_test,my_predict,alpha=0.4)
#예상하던 그림이 아니다.


mlr.score(X_train,y_train)
#모델 정확도 0.2392로 적합도가 낮다

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from statsmodels.formula.api import ols
from sklearn.linear_model import LinearRegression

data=pd.read_csv("C:\\Users\\jang\\Desktop\\python\\toluca_Company\\toluca_company_dataset.csv")
df=data

#데이터 살펴보기
df.info()



#statsmodels 사용

fit=ols("Work_hours ~ Lot_size",data=df).fit()
fit.summary()

fit.predict(exog=dict(Lot_size=[80]))


fig=plt.figure(figsize=(8,8))
plt.scatter(df['Lot_size'],df['Work_hours'])
plt.plot(df['Lot_size'],fit.fittedvalues,color='red')
plt.xlabel("Lot size")
plt.ylabel("Work hours")
plt.show()


#skleran 사용
X=df['Lot_size'].values.reshape(-1,1)
y=df['Work_hours']
fit=LinearRegression().fit(X,y)

fit.intercept_#절편
fit.coef_#기울기


fit.predict([[80]])
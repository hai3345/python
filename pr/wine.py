import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats
pd.set_option('display.max_columns', 500)
wine=pd.read_csv("C:\\Users\\Jang\\Desktop\\python\\Data\\와인\\train.csv")

wine.shape
wine.info()
wine.head()

#컬럼명 스페이스바 _로 바꿔주기
wine.columns=wine.columns.str.replace(" ","_")
wine.head()

#연속형 데이터에 대한 요약통계량
wine.describe()

#개별 요약통계 Series
wine.quality.describe()

sorted(wine.quality.unique())
wine.quality.value_counts()

#와인 종류별 품질 기술통계량
wine.groupby("type")["quality"].describe()

#종류별 품질의 사분위수
wine.groupby("type")["quality"].quantile([0,0.25,0.5,0.75,1]).unstack("type")

#그래프
red_q=wine.loc[wine["type"]=='red']["quality"]
white_q=wine.loc[wine["type"]=='white']["quality"]

sns.set_style("darkgrid")
sns.distplot(red_q,norm_hist=True,kde=False,color="red",label="Red Wine")
sns.distplot(white_q,norm_hist=True,kde=False,color="blue",label="White Wine")
plt.title("Wine Quality")
plt.xlabel("Quality Score")
plt.ylabel("Density")

#통계적 유의성 검정

wine.groupby("type")["quality"].aggregate(["std","mean"])

scipy.stats.ttest_ind(red_q,white_q,equal_var=False)

#상관분석


wine_corr=wine.corr()
wine_corr.loc[wine_corr["quality"]>0.]["quality"]

sns.heatmap(wine_corr,annot=True)

#산점도 그리기
red_s=wine.loc[wine["type"]=='red']
white_s=wine.loc[wine["type"]=='white']

red_idx=np.random.choice(red_s.index, replace=True, size=200)
white_idx=np.random.choice(white_s.index, replace=True, size=200)

wine_sample=red_s.loc[red_idx].append(white_s.loc[white_idx])
wine_sample.head()

sns.set_style("dark")
sns.pairplot(wine_sample, vars=["quality","alcohol","residual_sugar"],
             kind="reg",plot_kws={"ci":False,"x_jitter":0.35,"y_jitter":0.25},
             diag_kind="hist",diag_kws={"bins":10,"alpha":1},
             hue="type",palette=dict(red="red",white="blue",markers=["o","s"]))

########################################################################
#다중선형회귀
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

#fit_intetcept = 상수항을 사용 할 거냐
#y=a+bX 에서 a가 상수항

X=wine.drop(["index","type","quality"],axis=1)
y=wine.quality


X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.8,random_state=1)


model=LinearRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
#성능 측정
#RMSE
np.round(np.sqrt(mean_squared_error(y_test,y_pred)),5)

#######################################################
from sklearn.linear_model import Ridge
ridge=Ridge(alpha=0.05)
ridge.fit(X_train,y_train)
y_pred = ridge.predict(X_test)
np.round(np.sqrt(mean_squared_error(y_test,y_pred)),5)

fig = plt.figure(figsize=(6,3))
ax=fig.add_subplot(111)
alpha=5
ridge=Ridge(alpha=alpha)
ridge.fit(X_train,y_train)
coef=pd.Series(ridge.coef_,index=X_train.columns).sort_values()
ax.bar(coef.index,coef.values)
#글자 돌리기
ax.set_xticklabels(coef.index,rotation=90)
ax.set_title("alpha={}".format(alpha))

Ridge_Result=[]

for alpha in range(1,100):
    ridge=Ridge(alpha=alpha)
    ridge.fit(X_train,y_train)
    y_pred = ridge.predict(X_test)
    Ridge_Result=np.append(Ridge_Result,np.round(np.sqrt(mean_squared_error(y_test,y_pred)),5))

index_value=[]
for i in range(1,100):
    index_value.append(i)
col_names=['alpha','ridge_value']
Result_df=pd.DataFrame(Ridge_Result,index_value)
Result_df.rename=["Ridge_value"]
Result_df

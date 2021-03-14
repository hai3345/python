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


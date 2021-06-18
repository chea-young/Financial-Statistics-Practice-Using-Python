""""""""""""""""""""""""""" 파이썬 기초 """"""""""""""""""""""""""""""""""""""" 
#%% 참고 교재: 데이터 분석을 위한 판다스 입문 p.226 ~ p.229
#%% 1. 표준점수 계산하기
# 앞서 agg메서드의 경우 자료로 부터 집계 및 요약하여 원자료보다는 크기가 작은 데이터 생성
import pandas as pd
df=pd.read_csv('gapminder.tsv', sep='\t')

def my_mean(values):
 n=len(values)
 sum=0
 for value in values:
    sum+=value
 return sum/n
agg_my_mean=df.groupby('year').lifeExp.agg(my_mean)
print(agg_my_mean)

#%% 이번에는 transform()메서드를 사용하여 비슷한 작업을 할텐데, 
# transform()메서드의 경우 원자료의 크기는 변하지 않는 특성
# 예를 봅시다. 
def my_zscore(x):
 return (x-x.mean())/x.std()
transform_z=df.groupby('year').lifeExp.transform(my_zscore)
print(transform_z)

# 1952년도 아프가니스탄 기대수명 표준점수 = (1952년도 아프가니스탄 기대수명 - 1952년도 모든 나라의 기대수명 평균)/1952년도 모든 나라의 기대수명의 표준편차
#%% 2. 누락값을 평균값으로 처리하기
import seaborn as sns
import numpy as np
# 연습을 위해 임의로 데이터에 누락값을 4개 생성
np.random.seed(42)
tips_10=sns.load_dataset('tips').sample(10) # 10개의 data를 뽑고
miss_index=np.random.permutation(tips_10.index)
print(miss_index)
miss_index=np.random.permutation(tips_10.index)[:4]
print(miss_index)

#print(tips_10)
tips_10.loc[miss_index,'total_bill']=np.NaN # 누락값 4개를 성별에 따른 평균으로 대체
#print(tips_10)
count_sex=tips_10.groupby('sex').count() # 누락값 4개 때문에 total_bill의 count만 다름
print(count_sex) # NOTE total_bill 에서 총 10인데 4개가 부족함
#%%
def fill_na_mean(x):
 avg=x.mean()
 return x.fillna(avg)

total_bill_group_mean=tips_10.groupby('sex').total_bill.transform(fill_na_mean)
print(total_bill_group_mean)
print(tips_10)

tips_10['fill_total_bill']=total_bill_group_mean
print(tips_10)
# %%

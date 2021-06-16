#%% 참고 교재: 데이터 분석을 위한 판다스 입문 p.137 ~ p.151
#%% 1. 누락값?
# 누락값은 값이 존재하지 않는 상태를 의미로서 NaN, NAN, nan과 같은 방법으로 표기
# 누락값을 사용하려면 numpy라이브러리가 필요
from numpy import NaN, NAN, nan

print(NaN==True)
print(NaN==False)
print(NaN==0)
print(NaN=='')
print(NaN==NaN)
print(NaN==nan)
print(NaN==NAN)
print(nan==NAN)

print("===============================")
# 판다스에서 누락값 확인방법
import pandas as pd
print(pd.isnull(NaN)) # isnul(): nul이지? 응, nul이야
print(pd.isnull(nan)) # isnul(): nul이지? 응, nul이야
print(pd.isnull(NAN)) # isnul(): nul이지? 응, nul이야
# 판다스에서 누락값이 아닌 것 확인방법
print(pd.notnull(NaN)) # notnul(): nul 아니지? 아니야, nul이야
print(pd.notnull(42)) # notnul(): nul 아니지? 응, nul아니야
print(pd.notnull('mising'))# notnul(): nul 아니지? 응, nul아니야

#%% 2. 누락값이 생기는 이유

#%% 2-1. 누락값이 있는 데이터를 연결하는 경우
visited=pd.read_csv('survey_visited.csv')
survey=pd.read_csv('survey_survey.csv')
vs=visited.merge(survey,left_on='ident',right_on='taken')

#%% 2-2. 데이터 입력시 누락값을 입력한 경우
num_legs=pd.Series({'goat': 4, 'amoeba':nan})

#%% 2-3. 법위를 지정하여 데이터를 추출할 때 누락값이 생기는 경우
gapminder=pd.read_csv('gapminder.tsv', sep='\t')
life_exp=gapminder.groupby(['year'])['lifeExp'].mean()
life_exp2=life_exp.loc[range(200,2010),]
life_exp3=life_exp[life_exp.index>200]

#%% 3. 누락값의 갯수 세기
ebola=pd.read_csv('country_timeseries.csv')
# 누락값이 아닌 개수 세기
print(ebola.count()) # 변수별로 누락값을 제외하고 몇 개의 값이 있는지 세기
# 누락값 세기 1
num_rows=ebola.shape[0]
num_mising=num_rows-ebola.count() # 브로드캐스팅
# 누락값 세기 2: numpy의 count_nonzero()메서드와 판다스 isnul()메서드 사용
import numpy as np
ebola_nan=ebola.isnul()
print(np.count_nonzero(ebola_nan))
# 누락값 세기 3: 판다스 value_counts 메서드 사용
ebola_Guinea_value_counts=ebola.Cases_Guinea.value_counts(dropna=False)

#%% 4. 누락값 처리하기
#%% 4-1. 누락값 변경하기
# filna()메서드 사용해서 누락값을 0으로 변경
ebola_subset=ebola.iloc[0:10,0:5]
ebola_subset_0=ebola_subset.filna(0) # 0이외의 다른 숫자도 가능
# filna()메서드 사용해서 누락값이 나타나기 바로 이전의 값으로 변경
ebola_subset_fil=ebola_subset.filna(method='fil') # forward fil
# filna()메서드 사용해서 누락값이 나타난 바로 이후의 값으로 변경
ebola_subset_bfil=ebola_subset.filna(method='bfil') # backward fil
# interpolate()메서드 사용해서 누락값이 바로 이전과 이후 값의 중간값으로 변경
ebola_subset_interpolate=ebola_subset.interpolate() # backward fil

#%% 4-2. 누락값 삭제하기
ebola_dropna=ebola.dropna() # 누락값 하나라도 있는 행은 모두 삭제

#%% 5. 누락값이 포함된 데이터 계산하기
# 누락값 + 숫자 = 누락값
ebola_subset['Cases_multiple']=ebola_subset['Cases_Guinea']+ebola_subset['Cases_Liberia']+ebola_subset['Cases_SieraLeone']
ebola_subset['Cases_multiple_sum']=ebola_subset.sum(axis=1)
ebola_subset['Cases_multiple_sum2']=ebola_subset['Cases_Guinea','Cases_SieraLeone'].sum(axis=1)
sum_by_country=ebola_subset.sum()
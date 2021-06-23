""" ----------------------- 파이썬 금융통계 실습 ---------------------------"""
# 야후로 부터 주가데이터를 다운받아 주가 그래프를 간단히 그려보고, 
# 로그수익률, 기대수익률, 가격지수화, 변동성, 공분산, 상관계수를 구해보도록 합시다.
#%% 아래 두가지 패키지 인스톨(Console창에 복사하여 붙여넣기)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
# ============================================================================= 
# 1. 야후로 부터 데이터 불러오기 및 그림 그리기
# =============================================================================
import pandas_datareader as dr
start = datetime(2018,1,1)
end = datetime(2019,12,31)
help(dr.DataReader)
# 삼성전자
samsung_elec = dr.DataReader('005930.KS','yahoo',start,end)
print(samsung_elec[:10])

#야후로 부터 데이터를 불러오는 또다른 방법. 
#국내 주식 데이터 불러오기.
import yfinance as yf
samsung_elec = yf.download("005930.KS", start="2017-01-01", end="2020-05-31")
help(yf.download)
print(samsung_elec.head())
print(samsung_elec.tail())

# 삼성
start_date = '2019-01-01'
tickers = ['005930.KS', '068270.KS','^KS11'] #1 삼성전자 셀트리온 ticker(종목코드)
samsung_elec = yf.download(tickers[0], start_date)
samsung_elec['Adj Close'].plot()
plt.plot(samsung_elec['Adj Close'])

# 셀트리온
celtrion = yf.download(tickers[1], start_date)
celtrion['Adj Close'].plot()
kospi = yf.download(tickers[2], start_date)
kospi['Adj Close'].plot()

#데이터 합치기
stock_data = pd.DataFrame({'KOSPI': kospi['Adj Close'],'SAMSUNG':
samsung_elec['Adj Close'],'Celtrion': celtrion['Adj Close']})

#%% ============================================================================= 
# 2. 수익률 및 지수화를 통한 비교
# =============================================================================
# 주가 그래프 보기
stock_data.plot()

#%% 위의 주식가격 그래프는 주가 자체의 크기가 너무 달라 상호 비교하기가 어려움
# 따라서 다음과 같이 지수화를 통하여 상호비교가 용이
# 가격 지수화를 통한 가격의 비교
z=stock_data / stock_data.iloc[0] * 100
(stock_data / stock_data.iloc[0] * 100).plot(figsize=(8, 5), grid=True)

#%% 로그 수익률 구하기
# 통게적 방법론을 활용하여 주가같은 금융데이터를 분석하기 위해서는
# 통계적 방법론에서 가정하고 있는 자료의 성질을 만족할 필요가 있음
# 이러한 대표적인 성질이 "정상성(Stationary)" 이라고 함
# "정상성"을 만족하기 위해서는 다음과 같은 세가지 성질을 만족해야 함

# i) 시계열 데이터의 평균이 일정
# ii) 시계열 데이터의 분산이 일정
# iii) 두 시점간의 데이터의 관계는 두 시점간의 거리에만 의존
# 일반적으로 처음 2가지 성질은 눈으로도 확인하기 매우 쉬우나 3번째 성질은 눈으로
# 확인하기는 어려움. 따라서 여기서는 처음 2가지 성질을 위주로 논의합시다. 
# 첫번째 성질 확인해봅시다. 
stock_data['SAMSUNG'].plot()
stock_data['Celtrion'].plot()
stock_data['KOSPI'].plot()
plt.legend()
#%%
mv_avg_samsung=[]
mv_var_samsung=[]
s_idx=0
for i in range(0,2):
 mv_avg_samsung.append(stock_data.iloc[s_idx:s_idx+293,1].mean())
 mv_var_samsung.append(stock_data.iloc[s_idx:s_idx+293,1].var())
 s_idx=s_idx+293
plt.plot(mv_avg_samsung)
plt.plot(mv_var_samsung)
plt.legend()

#%% 시간이 흘러감에 따라 평균과 분산이 일정하지 않음을 확인할 수 있습니다. 
# 따라서, 주가 데이터로 부터 무엇인가 의미있는 통계적 성질을 알기 위해서는
# 위의 2가지 성격에 맞는 자료로 변형할 필요가 있습니다. 
# 어떻게 변형할까요? 가장 많이 사용하는 변환이 "로그 수익률"입니다. 
# 로그수익률 게산하기
z=stock_data.shift(1)
logret = np.log(stock_data / stock_data.shift(1)) # 로그수익률=log(price_{t} /price_{t-1})
#temp=stock_data.shift(1)

#%% 로그수익률 그래프 보기
logret['SAMSUNG'].plot()
logret['Celtrion'].plot()
logret['KOSPI'].plot()
#%%
mv_avg_samsung_2=[]
mv_var_samsung_2=[]
s_idx=0
for i in range(0,2):
 mv_avg_samsung_2.append(logret.iloc[s_idx:s_idx+293,1].mean())
 mv_var_samsung_2.append(logret.iloc[s_idx:s_idx+293,1].var())
 s_idx=s_idx+293
plt.plot(mv_avg_samsung_2)
plt.plot(mv_var_samsung_2)
# 로그수익률의 그래프를 보니 앞서 주가자체의 그래프보다는 상대적으로 평균과 분산이
# 일정함을 확인할 수 있습니다. 
# 물론, 2개의 나누어진 표본에 대하여 평균이 동일한지(평균검정) 분산이 동일한지(분산검정)
# 통계적으로 검증해야 하지만 여기서는 생략
# 결측데이터의 처리
logret=logret.dropna()

#%% ============================================================================= 
# 3. 기대수익률, 변동성, 공분산, 상관계수 구하기
# ============================================================================= 
# 기대 수익률 구하기
expected_return = logret.mean() # 일별수익률의 평균
print(expected_return)
#%% 연간 기대수익률
annual_expected_return=expected_return*250
print(annual_expected_return)
#%% 연간 변동성 구하기
variance=logret.var()*250
print(variance)
#%% 연간 표준편차 구하기
std=np.sqrt(variance)
print(std)
std2=logret.std() * np.sqrt(250)
print(std2)
#%% 공분산 구하기 => 공분산은 단위에 의존
cov=logret.cov()
print(cov)
cov2=logret.cov()*250 #연간 공분산. 
print(cov2)
# 상관계수 구하기
corr=logret.corr()
# 상관관계의 시각화
sns.heatmap(corr)
plt.show()

#%% [과제 44-1] 삼성전자, 셀트리온, 코스피의 주가와 로그수익률 각각에 대하여 전/후반부
# 2개의 표본으로 나누고 각각의 표본에 대한 Box plot을 그리고 평균과
# 분산이 동일한지 다른지에 대하여 적절한 해석을 해보시오.
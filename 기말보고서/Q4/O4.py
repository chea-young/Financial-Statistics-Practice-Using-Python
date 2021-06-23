#%%
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import yfinance as yf
import numpy as np
import pandas as pd
import datetime as dt
import seaborn as sns

# data 불러오기
samsung_elec = yf.download('005930.KS', start="2018-01-01", end="2018-12-31")
celtrion = yf.download('068270.KS', start="2018-01-02", end="2018-12-31")
hyundai_M = yf.download('005380.KS', start="2018-01-02", end="2018-12-31")

stock_data = pd.DataFrame({'Samsung': samsung_elec['Adj Close'], 
'Celtrion': celtrion['Adj Close'], 'Hyundai': hyundai_M['Adj Close']})

#로그수익률 계산
logret = np.log(stock_data / stock_data.shift(1))

# 개별 기대 수익률(평균) 구하기
expected_return = logret.mean()
# 연간 기대수익률(평균)
annual_expected_return=expected_return*250
print(expected_return)
print(annual_expected_return)

#%%일별분산
variance=logret.var()
print(variance)
# 연간 분산
variance_y=logret.var()*250
print(variance_y)

#공분산 구하기
cov=logret.cov()
print(cov)
#년간 공분산 구하기
cov2=logret.cov()*250
print(cov2)

# %%

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

#  포트폴리오 기대수익률과 분산 구하기
weight = np.array([1/3, 1/3, 1/3])

#로그수익률 계산
logret = np.log(stock_data / stock_data.shift(1))

# 포트폴리오 기대수익률 구하기
# 개별 기대 수익률(평균) 구하기
expected_return = logret.mean()
# 연간 기대수익률(평균)
annual_expected_return=expected_return*250

logret_np = logret.iloc[:,0:4].to_numpy()
portfolio_log_returns = np.dot(logret_np,weight.T)
portfolio_log_returns = portfolio_log_returns[~np.isnan(portfolio_log_returns)]
day_expected_portfilio_log_return = portfolio_log_returns.mean()
expected_portfilio_log_return = day_expected_portfilio_log_return*250

print(day_expected_portfilio_log_return)
print(expected_portfilio_log_return)

#포트폴리오 변동성 구하기
portfolio_variance = portfolio_log_returns.var()
print(portfolio_variance)
portfolio_variance_y = portfolio_log_returns.var()*250
print(portfolio_variance_y)
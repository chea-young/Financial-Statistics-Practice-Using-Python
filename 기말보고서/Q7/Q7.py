#%%
import matplotlib.pyplot as plt
import matplotlib
import yfinance as yf
import numpy as np
import pandas as pd
import datetime as dt
import seaborn as sns
matplotlib.rcParams['axes.unicode_minus'] = False

# data 불러오기
samsung_elec = yf.download('005930.KS', start="2018-01-01", end="2018-12-31")
celtrion = yf.download('068270.KS', start="2018-01-02", end="2018-12-31")
hyundai_M = yf.download('005380.KS', start="2018-01-02", end="2018-12-31")

stock_data = pd.DataFrame({'Samsung': samsung_elec['Adj Close'], 
'Celtrion': celtrion['Adj Close'], 'Hyundai': hyundai_M['Adj Close']})

#로그수익률 계산
logret = np.log(stock_data / stock_data.shift(1))
logret_np = logret.iloc[:,0:3].to_numpy() #NOTE 계산이 쉽도록 numpy로 만들어줌

portfolio_expected_returns = [] # NOTE 변하는 기대수익률을 저장하는 list
portfolio_variance = []# NOTE 변하는 변동성을 저장하는 list

weight_list = np.zeros(shape=(1000,3)) # NOTE 바뀌는 list에 대한 array
for sim in range (1000):
    # weight 시뮬레이션
    weight_temp = np.random.random(3)
    weight = weight_temp / np.sum(weight_temp)
    #%% 포트폴리오 기대수익률 구하기
    portfolio_log_returns = np.dot(logret_np,weight.T)
    portfolio_log_returns = portfolio_log_returns[~np.isnan(portfolio_log_returns)]
    expected_portfilio_log_return = portfolio_log_returns.mean()*250
    portfolio_expected_returns.append(expected_portfilio_log_return)
    #%% 포트폴리오 변동성 구하기
    portfolio_variance.append(portfolio_log_returns.var()*250)
    #%% weight list로 저장하기
    weight_list[sim,:]=weight

portfolio_expected_returns = np.array(portfolio_expected_returns)
portfolio_variance = np.array(portfolio_variance)

#NOTE 변동위험 대비 수익률 -> 클수록 좋다.
sharpe_ratio = portfolio_expected_returns/portfolio_variance

# i) 최소변동성 포트폴리오: NOTE 분산이 제일 작은 것
min_var_weight = weight_list[portfolio_variance==portfolio_variance.min()]
print("===========최소변동성 포트폴리오==============")
print(min_var_weight)
# ii) 최대 기대 수익률 포트폴리오
max_return_weight = weight_list[portfolio_expected_returns==portfolio_expected_returns.max()]
print("===========최대 기대 수익률 포트폴리오==============")
print(max_return_weight)
# iii) 최대 샤프비율 포트폴리오
max_sharpe_weight = weight_list[sharpe_ratio==sharpe_ratio.max()]
print("===========최대 샤프비율 포트폴리오==============")
print(max_sharpe_weight)
""" ----------------------- 파이썬 금융통계 실습 ---------------------------"""
# 위험과 수익률은 비례적인 관계, 즉 위험이 크면 수익률도 크다는 관계를 가지고 있습니다. 
# 재무적인 위험은 체계적 위험과 비체계적 위험으로 구분되는데
# 비체계적 위험은 분산투자를 통해서 제거할 수 있지만
# 체계적 위험은 아무리 분산투자를 해도 제거할 수 없는 위험입니다. 
# 따라서 분산투자를 위한 포트폴리오를 구성하는 것은 매우 중요한 주제입니다. 
# 여기서는 2개의 주가 종목을 대상으로 투자 비중을 조정하면서 어떻게 포트폴리오의
# 수익률과 변동성을 구하고, 그들간의 관계는 어떻게 되며, 재무적으로 의미를 가지는
# 몇가지 포트폴리오에 대해 살펴보도록 합시다.
#%%국내 주식 데이터 불러오기.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
start_date = '2019-01-01'
tickers = ['005930.KS', '068270.KS','^KS11'] #1 삼성전자 셀트리온 ticker(종목코드)
samsung_elec = yf.download(tickers[0], start_date)
celtrion = yf.download(tickers[1], start_date)
kospi = yf.download(tickers[2], start_date)

#데이터 합치기
stock_data = pd.DataFrame({'KOSPI': kospi['Adj Close'],'SAMSUNG':
samsung_elec['Adj Close'],'Celtrion': celtrion['Adj Close']})
print(stock_data[:10])
logret = np.log(stock_data / stock_data.shift(1)) # 로그수익률=log(price_{t} /price_{t-1}) NOTE 정상성을 위해서
print(logret[:10])
# 1. 개별 주식 종목의 기대수익률, 변동성, 공분산, 상관계수 구하기
# 1.1 개별 기대 수익률(평균) 구하기
# 일별수익률의 평균
expected_return = logret.mean() 
print(expected_return)
# 연간 기대수익률(평균)
annual_expected_return=expected_return*250

# 1.2 개별 연간 변동성(분산) 구하기
# 통계학에서 분산과 표준편차는 데이터의 흩어진 정도를 의미하며, 
# 금융에서 분산(variance)과 표준편차(standard deviation)는 위험의 크기를 재는 척도입니다. 
# 다음과 같은 2가지 주식종목의 내년 수익률 예상자료를 봅시다. 
# -------------------------------------------------------------
# | 경기 | bad | normal | good | 평균 | 분산 |
# ------------------------------------------------------------ 
# | 종목1 | -0.02 | 0.05 | 0.12 | 0.05 | 0.0049 |
# | 종목2 | -0.1 | 0.1 | 0.3 | 0.1 | 0.0400 |
# ------------------------------------------------------------ 
# 위의 두 종목의 평균값(기대수익률)은 종목2가 종목1보다 큽니다. 
# 하지만, 자료가 평균을 중심으로
# 흩어져 있는 정도는 종목2가 종목1보다 훨씬 큽니다. 
# 즉, 경기가 안 좋은 경우 종목2는
# 종목1 보다 훨씬 안 좋은 결과를 주고, 
# 좋은 경우 종목2는 종목1보다 훨씬 좋은 결과를 줍니다. 
# 즉, 종목1은 변동이 적으나 종목2는 변동의 폭이 큽니다. 
# 이러한 변동의 크기는 분산 또는 표준편차를 이용하여 측정합니다. 
# 종목1과 종목2의 분산을 계산해 봅시다. 
# 종목1의 분산 = ((-0.02 - 0.05)**2 + (0.05 - 0.05)**2 + (0.12 - 0.05)**2 ) / 2 = 0.0049
# 종목2의 분산 = ((-0.1 - 0.1)**2 + (0.1 - 0.1)**2 + (0.3 - 0.1)**2 ) / 2 = 0.0400
# 종목2의 분산이 종목1의 분산보다 큽니다. 
# 일반적으로 우리는 내년의 경기가 good일지, normal일지, 
# bad일지 정확하게 알 수는 없습니다. 
# 그럼 종목을 둘 중에 하나 선택해야 한다면 어떤 것을 선택하는 것이 좋을까요?
# 이것은 투자자의 위험에 대한 선호도에 따라 결정이 됩니다. 
# 위험(변동)을 선호하는 투자자는 종목2를, 
# 위험회피 성향이 강한 투자자는 종목1을 선택합니다. 
variance=logret.var()*250 # 연간변동성(분산)=일별변동성(분산)*250

# 연간 표준편차 구하기 - 표준편차는 분산의 제곱근
std=np.sqrt(variance)
std2=logret.std() * np.sqrt(250) # 연간 표준편차 = 일별 표준편차*sqrt(250)

# 공분산 구하기 - 공분산은 2개의 자료가 같은 방향으로 움직이는 정도를 측정하는 척도(단위에 의존)
# 종목1과 종목2의 공분산 = ((-0.02 - 0.05)*(-0.1 - 0.1) + (0.05 - 0.05)*(0.1 - 0.1) + (0.12 - 0.05)*(0.3 - 0.1)) / 2
cov=logret.cov()
cov2=logret.cov()*250 #연간 공분산 = 일별 공분산*250

# 상관계수 구하기 - 공분산이 단위에 의존하는 단점을 없애기 위한 척도
# 종목1과 종목2의 상관계수 = 종목1과 종목2의 공분산 / 종목1의 표준편차 / 종목2의 표준편차
corr=logret.corr() #NOTE 상관계수

#%% 2. 포트폴리오 기대수익률과 변동성
# 삼성전자 50%, 셀트리온 50%를 가정한 포트폴리오 기대수익률을 계산해 봅시다. 
weight = np.array([0.5, 0.5])

# 2-1. 포트폴리오 기대수익률 구하기
# 포트폴리오 기대수익률 구하는 법 1
logret_np = logret.iloc[:,1:3].to_numpy() #NOTE 계산이 쉽도록 numpy로 만들어줌
print(logret[:10])
portfolio_log_returns = np.dot(logret_np,weight.T)
portfolio_log_returns = portfolio_log_returns[~np.isnan(portfolio_log_returns)] # NOTE 자료가 있는 것들만 뽑는다. NAN이 사라짐.
expected_portfilio_log_return = portfolio_log_returns.mean()*250 # NOTE 연간을 위해서 205을 곱함.
print(expected_portfilio_log_return)

# 포트폴리오 기대수익률 구하는 법 2
# port_return: 포트폴리오의 기대수익률 = w1*삼성전자기대수익률 + w2*셀트리온기대수익률
annual_expected_return_np=annual_expected_return.iloc[1:3].to_numpy() # 행렬구조로 저장합니다
expected_portfilio_log_return2 = np.dot(weight,annual_expected_return_np) #numpy의 inner product 활용
print(expected_portfilio_log_return2)
# 2-2. 포트폴리오 변동성 구하기
# 포트폴리오 변동성 구하는 법 1
portfolio_variance = portfolio_log_returns.var()*250 # NOTE 연간 포트폴리오의 변동성
# 포트폴리오 변동성 구하는 법 2
cov=logret.cov()
cov2=logret.cov()*250 #연간 공분산

# 공분산 행렬(Covariance Matrix)
cov_np = cov2.iloc[1:3,1:3].to_numpy() # 행렬구조로 저장합니다
# 포트폴리오 수익률의 분산을 계산합니다. 
portfolio_variance2 = np.dot(np.dot(weight, cov_np), weight.T)
# 위의 portfolio_variance와 portfolio_variance2를 비교해보면 값이 소수5째자리에서
# 조금 차이가 나는데, # 이것은 계산하는 공식에 있어 약간의 차이로 무시할 수 있으며, 
# 자료의 길이가 무한히 길어지면 2개의 값은 동일하게 수렴합니다.
#%% 3. 가중치에 따른 포트폴리오 수익률 시뮬레이션
# 이제 두 종목에 투자하는 가중치를 다양하게 변동시키면서 포트폴리오 수익률을 생성해 봅시다. 
# NOTE 아까는 5:5였지만 지금은 랜덤으로 돌려서 포트폴리오릐 수익률이 어떻게 변하는지 보려고 하는거
portfolio_expected_returns = [] # NOTE 변하는 기대수익률을 저장하는 list
portfolio_variance = []# NOTE 변하는 변동성을 저장하는 list

weight_list = np.zeros(shape=(1000,2)) # NOTE 바뀌는 list에 대한 array
for sim in range (1000):
    # weight 시뮬레이션
    weight_temp = np.random.random(2)
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
# 샤프비율 구하기 = 기대수익률 / 변동성
#NOTE 변동위험 대비 수익률 -> 클수록 좋다.
sharpe_ratio = portfolio_expected_returns/portfolio_variance

# 수익률 대비 변동성 그림그리기
plt.scatter(portfolio_variance, portfolio_expected_returns, c=sharpe_ratio, marker='.')
plt.grid(True)
plt.xlabel('expected volatility')
plt.ylabel('expected return')
plt.colorbar(label='Sharpe ratio')
plt.show()
#NOTE 위험대비 수익률이 높은 구간이 노랑색, 위험대비 수익률이 낮은 구간이 보라색

# 위의 그래프는 x축에 포트폴리오 기대 변동성, y축에 포트폴리오 기대 수익률을 그린 것으로
# 점의 색깔은 샤프비율(기대수익률/기대변동성)을 나타냅니다. 
# 그래프에서 의미가 있는 점은 3군데 입니다. 
# i) 최소변동성 포트폴리오: 변동성이 가장 작은 포트폴리오
# ii) 최대 기대 수익률 포트폴리오: 기대수익률이 가장 높은 포트폴리오
# iii) 최대 사프 비율 포트폴리오: 샤프비율이 가장 높은 포트폴리오

#%% 그럼 위의 의미기 있는 3군데를 찾아 봅시다. 
# i) 최소변동성 포트폴리오: NOTE 분산이 제일 작은 것
min_var_weight = weight_list[portfolio_variance==portfolio_variance.min()]
# ii) 최대 기대 수익률 포트폴리오
max_return_weight = weight_list[portfolio_expected_returns==portfolio_expected_returns.max()]
# iii) 최대 샤프비율 포트폴리오
max_sharpe_weight = weight_list[sharpe_ratio==sharpe_ratio.max()]
# %%

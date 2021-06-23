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

# 수익률 대비 변동성 그림그리기
plt.figure(figsize=(12, 10))
plt.scatter(portfolio_variance, portfolio_expected_returns, c=sharpe_ratio, marker='.', cmap='jet')
plt.rcParams["font.family"] = 'Malgun Gothic'
plt.grid(True)
plt.xlabel('expected volatility(변동성[분산])',fontsize=18 )
plt.ylabel('expected return(기대수익률[평균])', fontsize = 18)
plt.rc('xtick', labelsize=15) 
plt.rc('ytick', labelsize=15)
xticks = np.array([0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35])
yticks = np.array([-0.250, -0.225, -0.200, -0.175, -0.150, -0.125, -0.100])
plt.xticks(xticks, xticks*250)
plt.yticks(yticks, yticks*250)
plt.colorbar(label='Sharpe ratio')
plt.style.use('ggplot')
plt.rc('font',family='Malgun Gothic')
plt.title("""삼성전자, 셀트리온, 현대차의 
변동성, 기대수익률 및 샤프비율 관계""", fontsize=35)
plt.savefig('Q6.png')
plt.show()
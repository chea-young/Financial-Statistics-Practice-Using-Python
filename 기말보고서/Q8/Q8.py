#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import yfinance as yf
matplotlib.rcParams['axes.unicode_minus'] = False

# data 불러오기
samsung_elec = yf.download('005930.KS', start="2019-01-02")
celtrion = yf.download('068270.KS', start="2019-01-02")
hyundai_M = yf.download('005380.KS', start="2019-01-02")

#10일 이전의 data
s_pre = yf.download('005930.KS', start='2018-12-14')
c_pre = yf.download('068270.KS', start='2018-12-14')
h_pre = yf.download('005380.KS', start='2018-12-14')

stock_data = pd.DataFrame({'Samsung': samsung_elec['Adj Close'], 
'Celtrion': celtrion['Adj Close'], 'Hyundai': hyundai_M['Adj Close']})
stock_data['Date'] = stock_data.index

pre_stock_data = pd.DataFrame({'Samsung': s_pre['Adj Close'], 
'Celtrion': c_pre['Adj Close'], 'Hyundai': h_pre['Adj Close']})

#최대샤프비율구하기
max_sharpe=pd.DataFrame([], columns = ['Date' , 'S', 'C', 'H'])
now = 10
index = 0

while(True):
    #로그수익률 계산
    logret = np.log(pre_stock_data[now-10:now] /pre_stock_data[now-10:now] .shift(1))
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
    sharpe_ratio = portfolio_expected_returns/portfolio_variance 
    max_sharpe_ratio = weight_list[sharpe_ratio==sharpe_ratio.max()]
    try:
        max_sharpe.loc[index] = [stock_data['Date'][index], 
        max_sharpe_ratio[0][0], max_sharpe_ratio[0][1], max_sharpe_ratio[0][2]]
    except Exception as e:
        print(e)
    if(now == 619):
        print(stock_data[now:now+1])
        break
    now +=1
    index +=1

max_sharpe = max_sharpe.set_index('Date')
data = pd.DataFrame({'Samsung': samsung_elec['Adj Close'], 
'Celtrion': celtrion['Adj Close'], 'Hyundai': hyundai_M['Adj Close'], 
'S':max_sharpe['S'], 'C':max_sharpe['C'], 'H':max_sharpe['H']})
data['Portfolio_after'] = data['Samsung'].shift(-1)*data['S']+data['Celtrion'].shift(-1)*data['C'] + data['Hyundai'].shift(-1)*data['H']
data['Portfolio_before'] = data['Samsung']*data['S']+data['Celtrion']*data['C'] + data['Hyundai']*data['H']

stock_data = pd.DataFrame({'Samsung': samsung_elec['Adj Close'], 
'Celtrion': celtrion['Adj Close'], 'Hyundai': hyundai_M['Adj Close']})

#누적로그수익률 계산
logret = np.log(stock_data / stock_data.shift(1))
d_logret = logret.cumsum()
logret_p = np.log(data['Portfolio_after']/data['Portfolio_before'])
d_logret_p = logret_p.cumsum()
fig = plt.figure(figsize=(15, 10))
d_logret_p.plot(linewidth=2.0, color='red')
d_logret['Samsung'].plot(linewidth=2.0, color='blue')
d_logret['Celtrion'].plot(linewidth=2.0, color='#FFC300')
d_logret['Hyundai'].plot(linewidth=2.0, color='green')


plt.ylabel('Cumulative log-return(누적 로그수익률)',fontsize=18 )
plt.xlabel('Time(년도)', fontsize = 18)
plt.rc('xtick', labelsize=15) 
plt.rc('ytick', labelsize=15)
plt.style.use('ggplot')
plt.rc('font',family='Malgun Gothic')
plt.title("Cumulative log-return", fontsize=30)
plt.legend(loc='upper left', fontsize=15, frameon=True, shadow=True)
plt.rcParams["font.family"] = 'Malgun Gothic'
plt.savefig('Q8.png')
# %%

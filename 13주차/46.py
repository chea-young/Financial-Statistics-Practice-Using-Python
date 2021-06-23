""" ----------------------- 파이썬 금융통계 실습 ---------------------------"""
# 우리는 내일의 주가가 오를지 내를지를 확률적으로 판단하기 위하여
# 얼마정도의 과거 데이터를 보아야 할까요?
# 하루? 1개월? 3개월? 6개월? 1년? 3년? ... 10년?
# 이러한 문제를 푸는 것이 가장 간단한 데이터사이언스 기반 투자전략이면서
# 금융공학(Financial Engineering), 파이낸스 어낼러틱스(Finance Analytics) 또는
# 파이낸스머신러닝(Finance Machine Learning)라고 한다.
# 우선 코스피주가를 불러와서 수익률을 구해봅시다. # 다만, 이번에는 연습을 위하여 최근 1개월 자료를 이용하여 주가가 오를 확률과 내릴
# 확률을 구하고 오를 확률이 내릴 확률보다 큰 경우 코스피지수 1계약을 매입하고, 
# 내릴 확률이 오를 학률보다 큰 경우 매입한 계약을 매도한다고 가정합시다. 
# 이런 조건하에서 2020년 1월 1일부터 2020년 12월 31일까지 1년 동안의 최종수익률을
#%% 구해 봅시다.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf
# 코스피 지수 불러오기 & 수익률 구하기
kospi = yf.download('^KS11', start="2019-10-01", end="2020-12-31")['Adj Close']
kospi_rtn = np.log(kospi / kospi.shift(1))
kospi_rtn.plot()

#%% 계산의 편의를 위해 index reset
kospi2=kospi.reset_index()
kospi_rtn2=kospi_rtn.reset_index()

# 최근 1개월 데이터를 통해 지수가 오를 확률과 내릴 확률을 구하고
prob=np.zeros(shape=(len(kospi),2))
for t in range(61,309): # 과거 1개월이 영업일 기준 20일이라고 가정
    past_1mon=kospi_rtn2[t-20:t-1]['Adj Close']
    prob[t,0]=sum(past_1mon>0)/len(past_1mon)
    prob[t,1]=1-prob[t,0]
#%% 오를 확률과 내릴 확률을 그림으로 그려 봅시다. 
prob_df=pd.DataFrame(prob)
kospi2_prob=pd.concat([kospi2,prob_df], axis=1)
fig, ax0=plt.subplots()
ax1=ax0.twinx()
kospi2_prob['Adj Close'].plot(kind='line', ax=ax0, color='black')
kospi2_prob.iloc[:,2].plot(kind='line', ax=ax1, color='red')
kospi2_prob.iloc[:,3].plot(kind='line', ax=ax1, color='blue')
ax0.legend()
ax1.legend(loc=3)

#%% 그림을 보니 코로나19충격이 시작되는 시점에서 내릴 확률이 더 크고
# 그 이후 지수가 회복하면서 오를 확률이 더 커짐을 확인할 수 있음
# 이제 위의 확률을 기반으로 코스피지수에 투자를 한다고 가정하고 성과를 확인해봅시다. 
balance=np.zeros(shape=(len(kospi),3)) 
buy=0 # 투자자가 매입을 했는지 나타내는 indicator: 0(비매수),1(매수)
for t in range(61,309):
    balance[t,0]=kospi[t]
    if prob[t,0]>prob[t,1]:
        if buy==0:
            balance[t,1]=1
            buy=1
        else:
            balance[t,1]=1
    else:
        if buy==1:
            balance[t,1]=1
            buy=0
        else:
            balance[t,1]=0
balance[:,2]=balance[:,0]*balance[:,1]

#%% 수익과 수익률을 계산해봅시다. 
payoff=np.zeros(shape=(len(kospi),2))
for t in range(61,309):
    if balance[t-1,1]==0 and balance[t,1]==1: # 신규 매입
        principal=balance[t,2]
        payoff[t,0]=balance[t,2]-principal 
        payoff[t,1]=np.log(balance[t,2]/principal)
    elif balance[t-1,1]==1 and balance[t,1]==1: # 매입 유지
        payoff[t,0]=balance[t,2]-principal 
        payoff[t,1]=np.log(balance[t,2]/principal)
    else: # 매도
        payoff[t,0]=np.nan
        payoff[t,1]=np.nan

#%% 수익을 그림으로 그려봅시다. 
payoff_df=pd.DataFrame(payoff)
fig, ax0=plt.subplots()
ax1=ax0.twinx()
kospi2_prob['Adj Close'].plot(kind='line', ax=ax0, color='black')
payoff_df.iloc[:,0].plot(kind='line', ax=ax1, color='blue')
ax0.legend()
ax1.legend(loc=3)
fig, ax0=plt.subplots()
ax1=ax0.twinx()
kospi2_prob['Adj Close'].plot(kind='line', ax=ax0, color='black')
payoff_df.iloc[:,1].plot(kind='line', ax=ax1, color='blue')
ax0.legend()
ax1.legend(loc=3)

# 방금 우리가 간단히 만든 투자모형에서 결정해야할 요소(모수; parameter)는 무엇일가요?
# i) 오를 확률과 내릴 확률을 구하기 위해서 어느 정도 길이의 과거 데이터를 바탕으로 해야하는가?
# ii) 매수와 매도 결정 기준인 P(오르는 경우)>P(내리는 경우)가 적절한가?
# iii) 투자종목이 1가지가 아니라 여러 가지인 경우는 어떻게 배분할 것인가?
# %%

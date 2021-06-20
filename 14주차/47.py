""" ------------ 파이썬 금융통계 실습 --------------"""
# 매일 매일 시장에서 제공되는 주가 관련 정보중에서 대표적인 것이 candlestick 그래프입니다. 
# Candlestick 그래프는 매일 매일 거래되는 주식의 시가(Open), 종가(Close), 고가(High), 
# 저가(Low)에 대한 정보와 함께 5일, 20일, 60일 이동평균을 함께 보여주는 주고, 
# 주가의 기술적인 분석에서 가장 기초가 되는 그래프입니다. 
# 우선 이동평균을 구하는 원리를 살펴 본 후 candlestick 그래프와 이동평균선을 함께
# 그려 봅시다.
#%% 1. 이동평균 구하기
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
import yfinance as yf

#%% 코스피 지수 불러오기 & 수익률 구하기
kospi = yf.download('^KS11', start="2019-10-01", end="2020-12-31")['Adj Close']
# 이동평균 구하기
# 5일 이동평균을 구해봅시다. 
n=5
T=len(kospi)
ma5=pd.DataFrame(columns=['Date','ma_5days'])
for start in range(0,T-5):
    ma5.loc[start+(n-1),['Date']]=kospi.index[start+(n-1)]
    ma5.loc[start+(n-1),['ma_5days']]=sum(kospi[start:start+n])/n
ma5.set_index('Date', inplace=True) 
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.plot(kospi)
ax.plot(ma5)
ax.legend(['KOSPI','5days moving average'])

#%%20일 이동편균을 구해봅시다. 
n=20
T=len(kospi)
ma20=pd.DataFrame(columns=['Date','ma_20days'])
for start in range(0,T-20):
    ma20.loc[start+(n-1),['Date']]=kospi.index[start+(n-1)]
    ma20.loc[start+(n-1),['ma_20days']]=sum(kospi[start:start+n])/n
ma20.set_index('Date', inplace=True) 
 
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.plot(kospi)
ax.plot(ma20)
ax.legend(['KOSPI','20days moving average'])
#%%60일 이동편균을 구해봅시다. 
n=60
T=len(kospi)
ma60=pd.DataFrame(columns=['Date','ma_60days'])
for start in range(0,T-60):
    ma60.loc[start+(n-1),['Date']]=kospi.index[start+(n-1)]
    ma60.loc[start+(n-1),['mv_20days']]=sum(kospi[start:start+n])/n
ma60.set_index('Date', inplace=True) 
 
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.plot(kospi)
ax.plot(ma60)
ax.legend(['KOSPI','60days moving average'])
#%% 2. Candlestick 그래프 그리기
# Candlestick 그래프(봉차트)는 주식을 비롯한 유가증권과 파생상품, 환율의 가격 움직임을 
# 보여주는 대표적인 금융차트
# 일반적으로 하나의 Candlestick은 "하루"의 가격 움직임을 요약
# Candlestick 그래프는 기술통계학에서 사용되는 Box plot과 유사
# 양봉: 주가가 오른 경우
"""
| 고가(High)
 
| 
 
------ 종가(Close)
 
|                |
    | 빨강 |
 
|               |
 
------ 시가(Open)
 |
 
| 저가(Low)
 음봉: 주가가 내린 경우
 
| 고가(High)
 |
 
------ 시가(Open)
 
|           |
 | 파랑     |
 
|           |
 
------ 종가(Close)
 |
 
| 저가(Low) """

#%%
import mplfinance as mpf 
kospi = yf.download('^KS11', start="2019-10-01", end="2020-12-31")
#%% 기본차트
mpf.plot(kospi) # type을 지정하지 않으면 OHLC형태의 차트가 출력
mpf.plot(kospi,type='candle',title='KOSPI', ylabel='Price')

mpf.available_styles()# mplfinance plot에서 가능한 스타일 확인
mpf.plot(kospi,type='candle',style='sas',title='KOSPI', ylabel='Price')

#%% 거래량(Volume) 추가
mpf.plot(kospi,type='candle',style='sas',title='KOSPI', ylabel='Price',volume=True) # NOTE 볼륨을 자동으로 가져와서 그려준다.
#%%
mpf.plot(kospi,type='candle',style='sas',title='KOSPI', ylabel='Price',volume=True, ylabel_lower='Vol.')

#%% 거래가 없는 날 추가
mpf.plot(kospi,type='candle',style='sas',title='KOSPI',ylabel='Price',volume=True,ylabel_lower='Vol.',show_nontrading=True)

#%% 사용자 정의 캔들챠트
mc = mpf.make_marketcolors(up='red')
s=mpf.make_mpf_style(marketcolors=mc)
mpf.plot(kospi,type='candle',style=s, title='KOSPI', ylabel='Price',volume=True,ylabel_lower='Vol.',show_nontrading=True)

#%% 이동평균 추가
mpf.plot(kospi,type='candle',style=s, title='KOSPI',ylabel='Price',volume=True,ylabel_lower='Vol.', show_nontrading=True,mav=(5,20,60))


#%% 그림저장
mpf.plot(kospi,type='candle',style=s, title='KOSPI', ylabel='Price',volume=True,ylabel_lower='Vol.',show_nontrading=True,mav=(5,20,60),savefig='KOSPI candle chart_1.png')

#%%
mpf.plot(kospi,type='candle',style=s, title='KOSPI', ylabel='Price',volume=True,ylabel_lower='Vol.', 
show_nontrading=True,mav=(5,20,60),savefig=dict(fname='KOSPI candle chart_2.png',dpi=100))

# %%

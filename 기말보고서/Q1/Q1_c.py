#%%1. 국내 주식 삼성전자, 셀트리온, 현대자동차의 2018년 1월 1일부터(휴일인 경우 2018년 첫 거래일부터)
#최근까지의 주가자료를 다운로드 받고, 우리나라 양식의 candlestick 그래프 를 그리시오.

#%%
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import yfinance as yf
import numpy as np
import pandas as pd

# data 불러오기
celtrion = yf.download('068270.KS', start="2018-01-02", end="2021-06-21")

# 이동평균선 데이터 구하기
celtrion['MA5'] = celtrion['Close'].rolling(5).mean()
celtrion['MA20'] = celtrion['Close'].rolling(20).mean()
celtrion['MA60'] = celtrion['Close'].rolling(60).mean()

#그래프 그리기
fig = plt.figure(figsize=(22, 10))
fig.set_facecolor('w')
fig.subplots_adjust(hspace=0)
plt.rcParams["font.family"] = 'Malgun Gothic'
gs = gridspec.GridSpec(2, 1, height_ratios=[2.5, 1.5])
axes = []
axes.append(plt.subplot(gs[0]))
axes.append(plt.subplot(gs[1], sharex=axes[0]))
axes[0].get_xaxis().set_visible(False)
index = np.arange(len(celtrion.index))
dohlc = np.hstack((np.reshape(index, (-1, 1)), celtrion))
axes[0].set_title('셀트리온', fontsize=35)

# 이동평균선 그리기
axes[0].plot(index, celtrion['MA5'], label='MA5', linewidth=0.7, color='#94EB3E')
axes[0].plot(index, celtrion['MA20'], label='MA20', linewidth=0.7, color='#FFC800')
axes[0].plot(index, celtrion['MA60'], label='MA60', linewidth=0.7, color='#D27328')
axes[0].legend(loc='upper left', fontsize=20, fancybox=True, shadow=True)

#candistrick 그리기
from mpl_finance import candlestick_ohlc

# 봉차트
candlestick_ohlc(axes[0], dohlc, width=0.9, colorup='r', colordown='b')

# 거래량 차트
axes[1].bar(index, celtrion['Volume'], color='green', width=0.9, align='center',label="Volume")
axes[1].legend(loc='upper left',fontsize=20, fancybox=True, shadow=True)

axes[0].set_ylabel("Price[가격] (원)",fontsize=18)
axes[1].set_ylabel("Volume[거래량] (K)", fontsize=18)

x_stick = [0, 101, 234, 344, 488, 590, 735, 837]
x_c_stick = ['2018-Jan-03', '2018-Jun-01',
'2019-Jan-03', '2019-Jun-03',
'2020-Jan-03', '2020-Jun-03',
'2021-Jan-04', '2021-Jun-03']

plt.rc('xtick', labelsize=18) 
plt.rc('ytick', labelsize=15)
plt.xticks(x_stick, x_c_stick, rotation=15)
plt.axis('on')
plt.grid()
plt.style.use('ggplot')
plt.rc('font',family='Malgun Gothic')
plt.savefig('Q1_c.png')
plt.show()


# %%


# %%

#%%
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import yfinance as yf
import numpy as np
import pandas as pd
import datetime as dt
import seaborn as sns

# data 불러오기
samsung_elec = yf.download('005930.KS', start="2018-01-01", end="2021-06-21")

#year 만들기
df = pd.DataFrame({'Date': pd.to_datetime(samsung_elec.index)})
df['Year'] = df['Date'].dt.year
data = samsung_elec.merge(df, left_on=['Date'], right_on=['Date'])
#data.rename(columns = {'Adj Close' : 'Adj_Close'}, inplace = True)

#  박스 그래프 그리기
ax=sns.boxplot(x='Year',y='Adj Close', data=data)
ax.set_title("Boxplot of Samsung Elec's stock price by period", fontsize=18)
ax.set_xlabel('period', fontsize=15)
ax.set_ylabel('stock price', fontsize=15)

# %%

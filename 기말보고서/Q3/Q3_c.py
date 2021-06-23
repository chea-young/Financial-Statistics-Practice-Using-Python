#%%
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import yfinance as yf
import numpy as np
import pandas as pd
import datetime as dt
import seaborn as sns

# data 불러오기
celtrion = yf.download('068270.KS', start="2018-01-02", end="2021-06-21")

#year 만들기
df = pd.DataFrame({'Date': pd.to_datetime(celtrion.index)})
df['Year'] = df['Date'].dt.year
data = celtrion.merge(df, left_on=['Date'], right_on=['Date'])
#data.rename(columns = {'Adj Close' : 'Adj_Close'}, inplace = True)

# 로그수익률 구하기
data['Logret'] = np.log(data['Adj Close'] /data['Adj Close'].shift(1))

#  박스 그래프 그리기
plt.figure(figsize=(10,6))
ax=sns.boxplot(x='Year',y='Logret', data=data, linewidth=2.5)
ax.set_title("Boxplot of Celtrion's stock return by period", fontsize=18)
ax.set_xlabel('period', fontsize=15)
ax.set_ylabel('stock return', fontsize=15)
plt.grid()
plt.savefig('Q3_c.png')
plt.show()

# %%

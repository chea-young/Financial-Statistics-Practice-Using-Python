""""""""""""""""""""""""""" 파이썬 기초 """"""""""""""""""""""""""""""""""""""" 
#%% 참고 교재: 데이터 분석을 위한 판다스 입문 p.251 ~ p.271
# 시계열 데이터를 가지고 몇 가지 사례별로 시계열 데이터를 다루는 연습을 해봅시다.

#%% 1. 에볼라 최초 발병일 계산하기
import pandas as pd
ebola=pd.read_csv('country_timeseries.csv')
print(ebola[:5])
print('-------------1-------------')
ebola['date_dt']=pd.to_datetime(ebola['Date']) # NOTE Date를 datetime type으로 추가
print(ebola[:5])

# 에볼라 최초발병일 구하기
ebola_outbreak_day=ebola['date_dt'].min() # 문자열이라면 불가능
ebola['ebola_elapsed_days']=ebola['date_dt']-ebola_outbreak_day

#%% 2. 파산한 은행의 개수 계산하기
# 파산한 은행 데이터 불러와서 분기별로 파산한 은행이 몇개 인지 계산하고, 시각화 해봅시다. 
banks=pd.read_csv('banklist.csv', parse_dates=[5,6])
print(banks.info())
banks=pd.read_csv('banklist.csv', parse_dates=['Closing Date','Updated Date'])
print(banks.info())

#%% dt접근자와 quarter속성을 이용하여 은행이 파산한 분기를 계산
banks['closing_quarter'], banks['closing_year']=(banks['Closing Date'].dt.quarter, banks['Closing Date'].dt.year)

# groupby메서드를 사용하여 연도별로 파산한 은행의 개수를 계산
closing_year=banks.groupby(['closing_year']).size()
closing_year_q=banks.groupby(['closing_year','closing_quarter']).size()

#%% 그래프로 그려 봅시다.
import matplotlib.pyplot as plt
fig, ax=plt.subplots()
ax=closing_year.plot()
fig, ax=plt.subplots()
ax=closing_year_q.plot()
plt.show()

#%% 3. 테슬라 주식 데이터로 시간 계산하기
import pandas as pd
tesla=pd.read_csv('tesla_stock_quandl.csv',parse_dates=[0])
# 2010년 6월 데이터만 추출해봅시다.
print('-------------1-------------')
print(tesla.loc[(tesla.Date.dt.year==2010) & (tesla.Date.dt.month==6)])

# datetime오브젝트를 데이터프레임의 index로 설정하면 원하는 시간의 데이터를 편리하게 추출
# 2010년 6월 데이터만 추출해봅시다. print(tesla.loc[(tesla.Date.dt.year==2010) & (tesla.Date.dt.month==6)])
# datetime오브젝트를 데이터프레임의 index로 설정하면 원하는 시간의 데이터를 편리하게 추출
tesla.index=tesla['Date']
tesla_2015=tesla.loc['2015']
tesla_201006=tesla.loc['2010-06']
tesla_20151231=tesla.loc['2015-12-31']
print('-------------2-------------')
print(tesla[:10])
print('-------------3-------------')
print(tesla_2015)
print('-------------4-------------')
print(tesla_201006)

#%% 4. 시간 범위와 인덱스
import pandas as pd
ebola=pd.read_csv('country_timeseries.csv',parse_dates=[0])
# date_range메서드를 사용하여 2014년 12월 31일부터 2015년 1월 5이 사이의 시간 인덱스 생성
head_range=pd.date_range(start='2014-12-31', end='2015-01-05')

# 시간 범위의 주기 설정할 수 있는 freq속성값은 p.263 참고
ebola_5=ebola.head()
ebola_5.index=ebola_5['Date']
ebola_5=ebola_5.reindex(head_range)

print('-------------1-------------')
print(ebola_5)
print('-------------2-------------')
print(ebola_5)
print('-------------3-------------')
print(ebola_5)
# %%

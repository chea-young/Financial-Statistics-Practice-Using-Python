#%%
import numpy as np
import csv
import matplotlib.pyplot as plt

# 1. 데이터를 읽어 온다
f=open('accident1.csv')
data=csv.reader(f)
next(data)
data=list(data) 

plt.style.use('ggplot')
plt.rc('font',family='Malgun Gothic')
plt.title('지역의 누적 교통 사고 건수 증감 그래프')

local = []
local_name = ""
for row in data:
    if(row[3] != ''):
        print(row[3])
        local.append(row[3])
    
plt.plot(local, label = '2019년와 2018년 비교')
plt.xticks([0,2,4,6,8,10,12,14,16], ['서울', '부산', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주', '대구', '인천', '광주', '대전', '울산', '세종'])
plt.legend()
plt.show()

# %%

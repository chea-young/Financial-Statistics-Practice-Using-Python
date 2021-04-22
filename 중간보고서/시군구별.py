#%%
import numpy as np
import csv
import matplotlib.pyplot as plt

# 1. 데이터를 읽어 온다
f=open('시군구별.csv')
data=csv.reader(f)
next(data)
data=list(data) 

plt.style.use('ggplot')
plt.rc('font',family='Malgun Gothic')
plt.title('상위 20위 지역의 시구군구별 월별 교통사고 통계')

higtest = [] # 1등에서 20위까지만 뽑아서 줄 예정
시도 = ''
시군별 = ''
accident_number = 0
for row in data:
    if(row[0] != ''):
        if(int(row[2]) == 1):
            시도 = row[0]
            시군별 = row[1]
            accident_number = 0
        accident_number += int(row[3])
        if(int(row[2]) == 12):
            higtest.append((accident_number, 시도+' '+시군별))

higtest = list(sorted(higtest, key=lambda x:x[0], reverse = True))
number = [tuple_data[0] for tuple_data in higtest[:21]]
name = [tuple_data[1] for tuple_data in higtest[:21] ]

plt.bar(name, number, color='blue')
plt.xticks(name, rotation=60)

for i, v in higtest[:20]:
    plt.text(v, i, i,                 # 좌표 (x축 = v, y축 = y[0]..y[1], 표시 = y[0]..y[1])
             fontsize = 12, 
             color='black',
             horizontalalignment='center',  # horizontalalignment (left, center, right)
             verticalalignment='bottom')    # verticalalignment (top, center, bottom)

plt.plot()
plt.legend()
plt.show()

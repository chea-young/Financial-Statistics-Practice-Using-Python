#%%
import numpy as np
import csv
import matplotlib.pyplot as plt

# 1. 데이터를 읽어 온다
f=open('충북청주시.CSV')
data=csv.reader(f)
next(data)
data=list(data) 
local = []

for row in data:
    local.append((float(row[16]), float(row[3]), row[13], row[2]))
print(local)

local = list(sorted(local, key=lambda x:x[0], reverse = True))
print(local)
통합지수 = [float(i[0]) for i in local[:11]]
건수 = [float(i[1]) for i in local[:11]]
치사율 = [float(i[2]) for i in local[:11]]
구간이름 = [i[3] for i in local[:11]]
x = np.arange(len(구간이름))

plt.rcParams["font.family"] = 'Malgun Gothic'
plt.rcParams["font.size"] = 20
plt.rcParams["figure.figsize"] = (20, 12)

plt.style.use('ggplot')
plt.rc('font',family='Malgun Gothic')
plt.title('충북 청주시 2019년 사고누적지 사고 지표')

plt.bar(x, 건수, label='건수',width=0.2, color='g')
plt.bar(x+0.2, 치사율,label='치사율',width=0.2, color='r')
plt.bar(x+0.4, 통합지수, label='통합지수',width=0.2, color='b')
plt.xticks(x, 구간이름, rotation=15)
plt.legend()
plt.show()
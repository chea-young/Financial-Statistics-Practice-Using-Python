#%%[과제10-1] 기온데이터에서 일교차를 모두 구하고 월별로 일교차를 보여주는 Boxplot을 그리시오.

import csv
import matplotlib.pyplot as plt

f=open('seoul.csv')
data=csv.reader(f)
next(data)

month=[]
for i in range(12):
    month.append([])

for row in data:
    if row[-1]!='':
        month[int(row[0].split('-')[1])-1].append(float(row[-1]) - float(row[-2]))

plt.rc('font',family='Malgun Gothic')
plt.style.use('ggplot')
plt.figure(figsize=(10,5))
plt.boxplot(month, labels=['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월']) 
plt.title('월별 일교차 그림')
plt.ylabel('일교차')
plt.show()
# %%

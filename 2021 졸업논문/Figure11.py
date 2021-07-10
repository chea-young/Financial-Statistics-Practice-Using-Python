#%%
"""
Edge: 1분 54초
Cloud(Korea): 2분 8초
Cloud(Califolina): 2분 32초
OBU: 4분 40초

"""
import numpy as np
import csv
import matplotlib.pyplot as plt


y = [60+54, 60*2+8, 60*2+32, 60*4+40]
y_h = ['1m54s', '2m8s', '2m32s', '4m40s']
x = [0, 1, 2, 3]
x1 = ['RSU(Edge)', 'AWS-Korea', 'AWS-California', 'OBU']
fig = plt.figure(figsize=(13, 10))
plt.rcParams["font.family"] = 'Malgun Gothic'
#plt.grid()

plt.style.use('ggplot')
plt.rc('font',family='Malgun Gothic')
plt.title('''응답시간 성능비교
''',fontsize = 28)

plt.bar(x, y, width=0.5, color = 'green')
for i in range(len(x)):
    ay = y_h[i]
    annotation = ay
    plt.annotate(annotation, xy=(x[i] - .2, y[i] + .1000), size=20)

 # x축 레이블 설정
plt.rc('xtick', labelsize=18) 
plt.rc('ytick', labelsize=18)
#plt.xlabel(fontsize=18) 
plt.ylabel('sec',fontsize=20)  # y축 레이블 설정

plt.xticks(x, x1)
plt.savefig('Figure11.png')
plt.show()
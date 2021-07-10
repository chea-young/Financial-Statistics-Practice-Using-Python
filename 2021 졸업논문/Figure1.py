#%%
import numpy as np
import csv
import matplotlib.pyplot as plt


ver3 = [64, 1235, 3456, 4905]
ver4 = [7, 314, 3109, 6299]
x = [0, 1, 2, 3]
x1 = ['2020F', '2025F', '2030F', '2035F']

fig = plt.figure(figsize=(13, 8))


plt.rcParams["font.family"] = 'Malgun Gothic'
#plt.grid()

plt.style.use('ggplot')
plt.rc('font',family='Malgun Gothic')
plt.title('''글로벌 자율주행 자동차 시장규모 전망
''',fontsize = 25)

plt.plot(x, ver3, label='제한 자율주행(Lv3)', marker='o', linestyle='solid', linewidth=5)
for i in range(len(x)):
    ay = str(int(ver3[i]))
    annotation = ay
    plt.annotate(annotation, xy=(x[i] - .1, ver3[i] + .7), size=20)

plt.plot(x, ver4,label='완전 자율주행(Lv4)', marker='s', linewidth=5)
for i in range(len(x)):
    ay = str(int(ver4[i]))
    annotation = ay
    plt.annotate(annotation, xy=(x[i] + .1, ver4[i] + .4), size=20 )


 # x축 레이블 설정
plt.rc('xtick', labelsize=18) 
plt.rc('ytick', labelsize=18)
#plt.xlabel(fontsize=18) 
plt.ylabel('(억달러)',fontsize=18)  # y축 레이블 설정

plt.xticks(x, x1)
plt.legend(fontsize=20, fancybox=True, shadow=True)
plt.savefig('Figure1.png')
plt.show()
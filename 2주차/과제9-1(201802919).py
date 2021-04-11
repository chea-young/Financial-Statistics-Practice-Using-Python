#%%
import csv
import matplotlib.pyplot as plt

f=open('seoul.csv')
data=csv.reader(f)
next(data)

daily_temp = [] #일교차를 담을 리스트
for row in data:
    if row[-1]!='' and row[-2]!='':                                
        if int(row[0].split('-')[0])>=1983:  
            if row[0].split('-')[1]=='08' and row[0].split('-')[2]=='15':
                daily_temp.append(float(row[-1]) - float(row[-2]))

plt.plot(daily_temp,'b.-', label='8월 15일 일교차')
                   
plt.rc('font',family='Malgun Gothic')     # 그래프 제목을 한글로 쓸 경우 깨지는 것을 방지하기 위해
plt.rcParams['axes.unicode_minus']=False  # 세로축의 음수 기호(-)가 깨지는 것을 방지

plt.legend()
plt.show()    
f.close()
# %%

#%% 참고 교재: 모두의 데이터 분석 with 파이썬 p.96 ~ p.108 
#%% 1. 인구 구조 시각화하기 
# www.mois.go.kr --> 정책자료 --> 통계 --> 주민등록 인구통계 
#%% 1-1. 인구 데이터 읽고 한 줄 씩 출력하기 
import csv 
f=open('age.csv') 
data=csv.reader(f) 
for row in data: 
    print(row)

#%% 특정 지역만 출력하기 
import csv 
f=open('age.csv') 
data=csv.reader(f) 
for row in data: 
    if '모현' in row[0]: # if A in B: A가 B에 있으면 True 아니면 False 
        print(row)

#%% 
import csv
f=open('age.csv') 
data=csv.reader(f) 
for row in data: 
    if '모현읍' in row[0]: 
        print(row) 


#%% 첫 2개의 값은 (row[1]과 row[2])에는 해당 지역의 '총인구수'와 '연령구간인구수'가 
# 저장되고, 우리가 필요로 하는 것은 그 이후에 있으므로 필요한 부분만 출력하려면 
import csv 
f=open('age.csv') 
data=csv.reader(f) 
for row in data: 
    if '모현읍' in row[0]: 
        for i in row[3:]: 
            print(i) 
import matplotlib.pyplot as plt 
plt.style.use('ggplot') 
plt.plot(result) 
plt.show() 

#%% 시각화를 위해 리스트에 저장하고 시각화 하기 
import csv 
f=open('age.csv') 
data=csv.reader(f) 
result=[] 

for row in data: 
    if '모현읍' in row[0]: 
        for i in row[3:]: 
            result.append(i)
import matplotlib.pyplot as plt 
plt.style.use('ggplot') 
plt.plot(result) 
plt.show() 
            
#%% result에 저장된 값이 문자로 저장 ==> 정수로 변환하여 저장 
import csv 
f=open('age.csv') 
data=csv.reader(f) 
result=[] 

for row in data: 
    if '모현읍' in row[0]: 
        for i in row[3:]: 
            result.append(int(i)) 

            
import matplotlib.pyplot as plt 
plt.style.use('ggplot') 
plt.plot(result) 
plt.show() 
# %%

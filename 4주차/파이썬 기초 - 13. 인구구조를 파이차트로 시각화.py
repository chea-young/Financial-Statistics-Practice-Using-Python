#%% 참고 교재: 모두의 데이터 분석 with 파이썬 p.124 ~ p.139
#%% 1. 제주도에는 여성의 비율이 더 높을까?
import csv
f=open('gender.csv')
data=csv.reader(f)
m=[]
f=[]
name=input('찾고 싶은 지역의 이름을 알려주세요: ')

for row in data:
    if name in row[0]:
        for i in row[3:104]: # row[3]: 남0세, row[103]: 남10세이상
            m.append(-int(i.replace(',','')))
        for i in row[106:]:
            f.append(int(i.replace(',','')))

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.figure(figsize=(3,2), dpi=150)
plt.rc('font',family='Malgun Gothic')
plt.rcParams['axes.unicode_minus']=False
plt.title(name+' 지역의 남녀 성별 인구 분포')
print(len(m), len(f), m, f)
plt.barh(range(101),m, label='남성')
plt.barh(range(101),f, label='여성')
plt.legend()
plt.show()


#%% ValueEror가 발생하고 그래프가 나타나지 않습니다. Variable explorer에서
# m과 f변수의 Size를 확인해 보세요. # 원하는 Size가 아닙니다. # 왜 이런 일이 발생했을까요?
# 다음과 같이 수정해 봅시다.
import csv
f=open('gender.csv')
data=csv.reader(f)
m=[]
f=[]

name=input('찾고 싶은 지역의 이름을 알려주세요: ')
for row in data:
    if name in row[0]:
        for i in row[3:104]: # row[3]: 남0세, row[103]: 남10세이상
            m.append(-int(i.replace(',','')))
        for i in row[106:]:
            f.append(int(i.replace(',','')))
        break
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.figure(figsize=(3,2), dpi=150)
plt.rc('font',family='Malgun Gothic')
plt.rcParams['axes.unicode_minus']=False
plt.title(name+' 지역의 남녀 성별 인구 분포')
plt.barh(range(101),m, label='남성')
plt.barh(range(101),f, label='여성')
plt.legend()
plt.show()

#%% break문 연습
for i in range(0,5):
    for j in range(0,5):
        print(i,j)
        break
 
for i in range(0,5):
    for j in range(0,5):
        print(i,j)
    break
 
for i in range(0,5):
    if i==3:
        for j in range(0,5):
            print(i,j)
            break
for i in range(0,5):
    if i==3:
        for j in range(0,5):
            print(i,j)
        break

#%% 2. pie()함수를 사용하여 파이차트 그리기
import matplotlib.pyplot as plt
plt.rc('font',family='Malgun Gothic')
size=[241, 2312, 1031, 123] # 데이터
label=['A형','B형','AB형','O형'] # 레이블
color=['darkmagenta','deeppink','hotpink','pink']
plt.axis('equal') # 파이차트 원을 동그랗게하고 스케일을 동일하게
plt.pie(size, labels=label,autopct='%.2f%%', colors=color, explode=(0.1,0,0,0), 
startangle=90)
# autopct -> # python format string 검색해보세요. # explode -> 데이터 순서대로
# startangle -> 파이차트가 시작하는 각도 (시작각도로 부터 반시계방향으로 그림)
plt.legend(loc=5)
plt.show()
 # 다양한 색상: htps:/matplotlib.org/galery/color/named_colors.html
#%% 3. 제주도 성별 인구 비율 표현하기
# gender.csv파일에서 '제주특별자치도'에서 남자와 여자의 총합을 구하고, # 파이차트를 그려 봅시다.
import csv
f=open('gender.csv')
data=csv.reader(f)
size=[]
name=input('찾고 싶은 지역의 이름을 알려주세요: ')

for row in data:
    if name in row[0]:
        m=0
        f=0
        for i in range(101):
            m+=int(row[i+3].replace(',','')) # m=m+int(row[i+3].replace(',',')
            f+=int(row[i+106].replace(',','')) # f=f+int(row[i+106].replace(',',')
        break
size.append(m)
size.append(f)

import matplotlib.pyplot as plt 
plt.rc('font',family='Malgun Gothic')
label=['남자','여자'] # 레이블
color=['darkmagenta','deeppink']
plt.axis('equal') # 파이차트 원을 동그랗게
plt.pie(size, labels=label,autopct='%.2f%%', colors=color, startangle=90)
# autopct -> # pythong format string 검색해보세요. # explode -> 데이터 순서대로
# startangle -> 파이차트가 시작하는 각도 (시작각도로 부터 반시계방향으로 그림)
plt.title(name+' 지역의 남녀 성별 비율')
plt.show()
# %%

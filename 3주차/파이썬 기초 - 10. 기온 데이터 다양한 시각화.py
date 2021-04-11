#%% 참고 교재: 모두의 데이터 분석 with 파이썬 p.54 ~ p.94


#%% 1. 히스토그램

#%% 1-1. hist()함수

import matplotlib.pyplot as plt
x=[1,1,2,3,4,5,6,6,7,8,10]
plt.hist(x)
plt.show()

#%% 1-2. 주사위 시뮬레이션
 
import random
print(random.randint(1,6)) 

#%% randint()함수를 사용하기 위해 random 모듈 import
# randint()함수를 사용하여 1 ~ 6 중 정수를 추출
# randint(a,b)함수를 함수 도움말에서 찾아 보세요.
# 여러번 난수(주사위 숫자) 추출: 난수 추출이므로 실행할때마다 다른 결과

import random

dice=[]
for i in range(5):
    dice.append(random.randint(1,6))
print(dice)


#%% 주사위 시뮬레이션 결과 히스토그램
import matplotlib.pyplot as plt
import random

dice=[]
for i in range(5):
    dice.append(random.randint(1,6))
    plt.hist(dice, bins=6, range=(1,6))
plt.show()

#%% bins: 히스토그램에서 구간의 개수 설정
# range: 히스토그램에서 구간의 최대 최소값 설정
# 난수가 정말 균등하게 생성되는지 확인
import matplotlib.pyplot as plt
import random

dice=[]
for i in range(100000):
    dice.append(random.randint(1,6))

plt.rc('font',family='Malgun Gothic') # 그래프 제목을 한글로 쓸 경우 깨지는 것을 방지하기 위해
plt.hist(dice, bins=6, range=(1,6), density=True) # density: 확률로 표시
plt.title('주사위 던지기')
plt.xlabel('주사위 던진 결과')
plt.ylabel('확률')
plt.grid(True)
plt.show()

# 히스토그램의 다양한 사용법
# https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.hist.html
# 에서 확인하고 연습해 보세요.
 

#%% 1-3. 기온 데이터 히스토그램 그리기
# 다음 코드를 봅시다.
import cs
import matplotlib.pyplot as plt

f=open('seoul.csv')
data=csv.reader(f)
next(data)
result=[]

for row in data: 
    if row[-1]!='':
        result.append(float(row[-1]))

#plt.rcParams['axes.unicode_minus']=False
# 세로축의 음수 기호(-)가 깨지는 것을 방지

plt.hist(result, bins=100, color='r')
plt.title('최고 기온 히스토그램')
plt.xlabel('최고 기온')
plt.ylabel('빈도')
plt.grid(True)
plt.show()


#%% 1-4. 8월 기온 데이터 히스토그램 그리기
# 앞서 split()함수를 활용하여 삼일절 최고 기온을 그린 코드를 활용하여
# 8월 최고 기온의 히스토그램을 그려보자.
import csv
import matplotlib.pyplot as plt

f=open('seoul.csv')
data=csv.reader(f)
next(data)
aug=[]

for row in data:
    month=row[0].split('-')[1]
    if row[-1]!='':
        if month=='08':
            aug.append(float(row[-1]))
plt.hist(aug, bins=100, color='r')
plt.show()


#%% 1-5. 1월과 8월 기온 데이터 히스토그램 그리기

import csv
import matplotlib.pyplot as plt

f=open('seoul.csv')
data=csv.reader(f)
next(data)
jan=[]
aug=[]

for row in data:
    month=row[0].split('-')[1]
    if row[-1]!='':
        if month=='08':
            aug.append(float(row[-1]))
        if month=='01':
            jan.append(float(row[-1])) 
plt.rcParams['axes.unicode_minus']=False
# 세로축의 음수 기호(-)가 깨지는 것을 방지
print(aug, jan)
plt.hist(aug, bins=100, color='r', label='8월')
plt.hist( jan, bins=100, color='b', label='1월')
plt.legend()
plt.title('최고 기온 히스토그램')
plt.xlabel('최고 기온')
plt.ylabel('빈도')
plt.grid(True)
plt.show()

#%% 1-6. 기온 데이터 상자 그림(Box plot)
# 다음 코드를 봅시다.

import matplotlib.pyplot as plt
import random
result=[]
for i in range(13):
    result.append(random.randint(1,1000))
print(sorted(result))
plt.boxplot(result)
plt.show()

# Boxplot에서
# 맨위 가로선: 최대값
# 상자의 윗선: 3/4값(3사분위수)
# 상자의 가운데 선: 2/4값(중앙값)
# 상자의 아래선: 1/4값(1사분위수)
# 맨아래 가로선: 최소값
# 동그라미: outlier(특이치)

#%% 기온데이터 상자그림

import csv
import matplotlib.pyplot as plt

f=open('seoul.csv')
data=csv.reader(f)
next(data)
result=[]

for row in data:
    if row[-1]!='':
        result.append(float(row[-1]))

plt.boxplot(result)
plt.show()

#%% 1월 8월 기온 상자그림 그리기 

import csv
import matplotlib.pyplot as plt

f=open('seoul.csv')
data=csv.reader(f)
next(data)
jan=[]
aug=[]

for row in data:
    month=row[0].split('-')[1]
    if row[-1]!='':
        if month=='08':
            aug.append(float(row[-1]))
        if month=='01':
            jan.append(float(row[-1]))

plt.boxplot(aug)
plt.boxplot( jan)
plt.title('최고 기온 상자그림')
plt.ylabel('최고 기온')
plt.show()

plt.style.use('ggplot')
plt.figure(figsize=(10,5)) 
plt.boxplot([ jan,aug], labels=['1월','8월'])
plt.title('최고 기온 상자그림')
plt.ylabel('최고 기온')
plt.show()


#%% 1월 ~ 12월 기온 상자그림 그리기

import csv
import matplotlib.pyplot as plt

f=open('seoul.csv')
data=csv.reader(f)
next(data)

# 월별 데이터를 저장할 month 리스크 생성
month=[]
for i in range(12):
    month.append([])

for row in data:
    if row[-1]!='':
        month[int(row[0].split('-')[1])-1].append(float(row[-1]))

plt.style.use('ggplot')
plt.figure(figsize=(10,5))
plt.boxplot(month, labels=['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월']) 
plt.title('최고 기온 상자그림')
plt.ylabel('최고 기온')
plt.show()
 
 
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

plt.style.use('ggplot')
plt.figure(figsize=(10,5))
plt.boxplot(month, labels=['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월']) 
plt.title('월별 일교차 그림')
plt.ylabel('일교차')
plt.show()

# %%

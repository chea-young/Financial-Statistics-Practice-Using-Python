import csv 
f=open('gender.csv') 
data=csv.reader(f) 

first_name=input("인구 구조를 비교하고 싶은 첫번째 지역의 이름(읍면동 단위)을 입력해주세요: ")
first_gender = input("인구 구조를 비교하고 싶은 첫번째 지역의 성별을 입력하세요(예: 남 또는 예 여): ")

second_name=input("인구 구조를 비교하고 싶은 두번째 지역의 이름(읍면동 단위)을 입력해주세요: ")
second_gender = input("인구 구조를 비교하고 싶은 두번째 지역의 성별을 입력하세요(예: 남 또는 예 여): ")

first = []
second = []
first_compare = 0
second_compare = 0
if(first_gender == '여'):
    first_compare = (3, 104)
    first_gender = ' 여자'
else:
    first_compare = (106,-1)
    first_gender = ' 남자'

if(second_gender == '여'):
    second_compare = (3, 104)
    second_gender = ' 여자'
else:
    second_compare = (106,-1)
    second_gender = ' 남자'

for row in data: 
    if first_name in row[0]: 
        for i in row[first_compare[0]:first_compare[1]]: 
            first.append(-int(i)) 
    if second_name in row[0]:
        for i in row[second_compare[0]:second_compare[1]]: 
            second.append(int(i))

import matplotlib.pyplot as plt 
plt.rc('font',family='Malgun Gothic') 
plt.rcParams['axes.unicode_minus']=False 
plt.title('모현읍 지역의 남녀 성별 인구 분포') 
plt.barh(range(101),first, label=first_name+first_gender, color='red') 
plt.barh(range(101),second, label=second_name+second_gender, color='blue') 
plt.xticks([-300,-200,-100,0,100,200,300],[300,200,100,0,100,200,300]) 
plt.legend() 
plt.show() 

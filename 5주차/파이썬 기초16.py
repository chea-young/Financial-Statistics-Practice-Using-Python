#%% 참고 교재: 모두의 데이터 분석 with 파이썬 p.27 ~ p.250
#%% 지금까지 배운 내용을 바탕으로 다음의 간단한 분석을 해봅시다
#%% 인구 구조 데이터 (age.csv)를 바탕으로 우리 동네와 인구구조가 가장 비슷한 지역
# 을 찾아 봅시다.
import numpy as np
import csv
# 1. 데이터를 읽어 온다
f=open('age.csv')
data=csv.reader(f)
next(data)
data=list(data)
# 2. 궁금한 지역의 이름을 입력 받는다
name=input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해 주세요: ')
mn=1
result_name=''
result=0
home =0
temp=[]
# 3. 궁금한 지역의 인구 구조를 저장한다
for row in data:
    if name in row[0]:
        for i in row[2:]:
            temp.append(i.replace(',',''))
        home=np.array(temp[1:], dtype=int)/int(temp[0])

# 4. 궁금한 지역의 인구 구조와 가장 비슷한 인구를 가진 지역을 찾는다
temp=[]
for row in data:
    for i in row[2:]:
        temp.append(i.replace(',',''))
    away=np.array(temp[1:], dtype=int)/int(temp[0])
    s=np.sum((home-away)**2)
    print(s)
    if s<mn and name not in row[0]:
        mn=s
        result_name=row[0]
        result=away
    temp =[]

# 5. 궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 시각화
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rc('font',family='Malgun Gothic')
plt.title(name+' 지역과 가장 비슷한 인구 구조를 가진 지역')
plt.plot(home, label=name)
plt.plot(result, label=result_name)
plt.legend()
plt.show()

#%% [과제16-1] 'gender.csv'파일을 사용해서 관심있는 지역을 선택한 후 그 지역의 
# 남자와 여자 각 연령대별 인구구성비를 
# 따로 구하고 (예, 남자 0세 인구구성비=남자0세 인구/남자 총인구, # 여자 0세 인구구성비=여자 0세 인구수/여자 총인구), 
# 그 지역과 남자와 여자 인구구성비가 가장 비슷한 지역을 찾아서 시각화 하시오. 
# 시각화 방법은 여러분이 편한 방법(시각화가 가장 훌륭한 방법)을 선택하세요. 
#  가장 비슷한 지역을 찾는 방법: 
# np.sum(male_home-male_away)**2+(female_home-female_away)**2)

# 1. 데이터를 읽어 온다
import csv
import numpy as np
f=open('gender.csv') 
data=csv.reader(f)
next(data)
data=list(data) 

# 2. 궁금한 지역의 이름을 입력 받는다
name=input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해 주세요: ')
mn=(1,1)
result_name=''
result_male=0
result_female = 0
male_home = 0
female_home =0
m = []
f = []

# 3. 궁금한 지역의 인구 구조를 저장한다
for row in data:
    if name in row[0]:
        for i in row[3:104]:
            m.append(int(i.replace(',','')))
        for i in row[106:]:
            f.append(int(i.replace(',','')))
        male_home = np.array(m[1:], dtype=int)/int(m[0])
        female_home = np.array(f[1:], dtype=int)/int(f[0])

# 4. 궁금한 지역의 인구 구조와 가장 비슷한 인구를 가진 지역을 찾는다

m = []
f = []
for row in data:
    for i in row[3:104]:
        m.append(int(i.replace(',','')))
    for i in row[106:]:
        f.append(int(i.replace(',','')))
    male_away = np.array(m[1:], dtype=int)/int(m[0])
    female_away = np.array(f[1:], dtype=int)/int(f[0])
    print(male_away, female_away)
    s = np.sum((male_home-male_away)**2+(female_home-female_away)**2)
    print(s)
    if s<mn and name not in row[0]:
        mn=s
        result_name=str(row[0])
        print(result_name)
        result_male = male_away
        result_female = female_away
    x = []
    y = []
    
# 5. 궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 시각화
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rc('font',family='Malgun Gothic')
plt.title(name+'지역과 남자와 여자 인구구성비가 가장 비슷한 지역')
plt.plot(male_home, label=name+ ' 남성')
plt.plot(female_home, label=name+ ' 여성')
plt.plot(result_male, label=result_name+ ' 남성')
plt.plot(result_female, label=result_name+ '여성')
plt.legend()
plt.show()
# %%

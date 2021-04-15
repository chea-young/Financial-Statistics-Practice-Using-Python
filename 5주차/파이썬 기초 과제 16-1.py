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
        for i in row[2:104]:
            m.append(int(i.replace(',','')))
        for i in row[105:]:
            f.append(int(i.replace(',','')))
        male_home = np.array(m[1:], dtype=int)/int(m[0])
        female_home = np.array(f[1:], dtype=int)/int(f[0])

# 4. 궁금한 지역의 인구 구조와 가장 비슷한 인구를 가진 지역을 찾는다
mn = np.array([1], dtype=np.float64)
m = []
f = []
for row in data:
    for i in row[2:104]:
        m.append(int(i.replace(',','')))
    for i in row[105:]:
        f.append(int(i.replace(',','')))
    male_away = np.array(m[1:], dtype=int)/int(m[0])
    female_away = np.array(f[1:], dtype=int)/int(f[0])
    s = np.sum((male_home-male_away)**2+(female_home-female_away)**2)
    if s<mn and name not in row[0]:
        mn=s
        result_name=str(row[0])
        result_male = male_away
        result_female = female_away
    m = []
    f = []



# 5. 궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 시각화
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rc('font',family='Malgun Gothic')
plt.title(name+'지역과 남자의 인구구성비가 가장 비슷한 지역')
plt.barh(range(101), -male_home, label=name+ ' 남성', color='red')
plt.barh(range(101), -result_male, label=result_name+ ' 남성', color='yellow')
plt.xticks([-0.020,-0.015,-0.010,-0.005, 0.000,0.005,0.010,0.015, 0.020],[0.020,0.015,0.010,0.005, 0.000,0.005,0.010,0.015, 0.020]) 
plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
plt.tight_layout()
plt.savefig('./sin.png')
plt.show()

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rc('font',family='Malgun Gothic')
plt.title(name+'지역과 여자의 인구구성비가 가장 비슷한 지역')
plt.barh(range(101), female_home, label=name+ ' 여성', color='blue')
plt.barh(range(101), result_female, label=result_name+ '여성', color='green')
plt.xticks([-0.020,-0.015,-0.010,-0.005, 0.000,0.005,0.010,0.015, 0.020],[0.020,0.015,0.010,0.005, 0.000,0.005,0.010,0.015, 0.020]) 
plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
plt.tight_layout()
plt.savefig('./sin.png')
plt.show()
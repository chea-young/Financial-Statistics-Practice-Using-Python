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
# 2. 궁금한 지역의 이름을 입력 받는다
name=input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해 주세요: ')
mn=0
result_name=''
result=0
# 3. 궁금한 지역의 인구 구조를 저장한다
for row in data:
    if name in row[0]:
        home=(np.array(row[3:], dtype=int)/int(row[2]))

# 4. 궁금한 지역의 인구 구조와 가장 비슷한 인구를 가진 지역을 찾는다
for row in data:
    away=np.array(row[3:], dtype=int)/int(row[2])
    s=np.sum((home-away)*2)
    if s<mn and name not in row[0]:
        mn=s
        result_name=row[0]
        result=away

#%% 한번 불러온 데이터 여러번 사용하기
import numpy as np
import csv

# 1. 데이터를 읽어 온다
f=open('age2.csv')
data=csv.reader(f)
next(data)
data=list(data) # 데이터를 리스트로 미리 저장
# 2. 궁금한 지역의 이름을 입력 받는다
name=input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해 주세요: ')
mn=1
result_name='
result=0
# 3. 궁금한 지역의 인구 구조를 저장한다
for row in data:
    if name in row[0]:
        home=np.array(row[3:], dtype=int)/int(row[2])

# 4. 궁금한 지역의 인구 구조와 가장 비슷한 인구를 가진 지역을 찾는다
for row in data:
    away=np.array(row[3:], dtype=int)/int(row[2])
    s=np.sum((home-away)*2)
    if s<mn and name not in row[0]:
        ms = s
        result_name=row[0]
        result=away

# 5. 궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 시각화
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rc('font',family='Malgun Gothic')
plt.title(name+' 지역과 가장 비슷한 인구 구조를 가진 지역')
plt.plot(home, label=name)
plt.plot(result, label=result_name)
plt.legend()
plt.show()

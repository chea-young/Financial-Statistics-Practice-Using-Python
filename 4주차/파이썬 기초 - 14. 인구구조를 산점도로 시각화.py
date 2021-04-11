#%% 참고 교재: 모두의 데이터 분석 with 파이썬 p.141 ~ p.156
#%% 1. 꺽은선 그래프로 표현하기
# 앞선 실습에서 제주도 전체 남성과 여성의 비율을 파이차트를 활용하여 시각화
# 이제 연령대별로 남녀의 비율을 좀 더 쉽게 비교하여 보자. #%% 남성 데이터와 여성 데이터를 서로 다른 색의 꺽은선 그래프로 표현하여 연령대별
# 성별 비율을 살펴봅시다.
import csv
f=open('gender.csv')
data=csv.reader(f)
m=[]
f=[]

name=input('궁금한 동네를 입력해주세요: ')

for row in data:
    if name in row[0]:
        for i in range(3,104):
            m.append(int(row[i]))
            f.append(int(row[i+103]))
        break
import matplotlib.pyplot as plt
plt.plot(m, label='Male')
plt.plot(f, label='Female')
plt.legend()
plt.show()
# 꺽은선 그래프가 항아리 모형 그래프 보다 연령대별 남녀 인구의 차이를 더 잘 보여줍니다. # 보여주고자 하는 내용을 시각화하는 방법은 다양하게 존재합니다. # 어떤 그래프를 사용하느냐에 따라 정보의 전달력도 달라집니다. # 다음과 같이 연령대별 남녀 인구의 차이를 시각화하는 다양한 방법을 살펴 봅시다.
#%% 2. 막대그래프로 표현하기
import csv
f=open('gender.csv')
data=csv.reader(f)
result=[]
name=input('궁금한 동네를 입력해주세요: ')
for row in data:
    if name in row[0]:
        for i in range(3,104):
            result.append(int(row[i])-int(row[i+103]))
        break
import matplotlib.pyplot as plt
plt.bar(range(101), result)
plt.show()
#%% 3. scater()함수로 표현하기
# 산점도는 scater()함수를 사용하여 표현
# 산점도는 x축과 y축에 해당하는 데이터의 상관관계를 표현할 때 사용
# 다음의 간단한 코드를 봅시다.
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.scatter([1,2,3,4],[10,30,20,40]) # scatter(x,y)
plt.show()

#%% 4. 버블차트로 표현하기
# 위에서 그린 산점도에서 점의 크기에 정보를 추가해봅시다. # 예를들어, (x,y)=(1,10)인 사람이 10명
# (x,y)=(2,30)인 사람이 20명
# (x,y)=(3,20)인 사람이 250명
# (x,y)=(4,40)인 사람이 30명
import matplotlib.pyplot as plt
plt.scatter([1,2,3,4],[10,30,20,40], s=[10,20,250,30]) # s는 점의 크기(size)
plt.show()

#%%
import matplotlib.pyplot as plt
plt.scatter([1,2,3,4],[10,30,20,40], s=[10,20,250,30], c=['red','blue','green','gold']) # c는 점의 색깔(color)
plt.show()

#%% 이렇게 해놓고 보니 그래프를 보았을 경우 빨간색이 10명을 의미하고, 파란색이 20명을
# 의미한다는 표시가 필요하겠죠?
import matplotlib.pyplot as plt
plt.scatter([1,2,3,4],[10,30,20,40], s=[10,20,250,30], c=range(4) )
plt.colorbar() # colorbar()를 사용하면 알아서 최소값과 최대값이 극과극 색깔로 표현
plt.show()

#%% cmap이라는 컬러맵속성을 사용하면 컬러바에 사용될 색상의 종류를 선택 가능
import matplotlib.pyplot as plt
plt.scatter([1,2,3,4],[10,30,20,40], s=[10,20,250,30], c=range(4), cmap='jet')
plt.colorbar()
plt.show() 

# 구글 검색을 통해서 다양한 옵션을 확인하고 적용해 보세요. # htps:/matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.scater.html

#%% 버블차트의 장점을 보기 위해 좀 더 많은 자료를 임의로 생성해서 그려봅시다. 
import matplotlib.pyplot as plt
import random

x=[]
y=[]
size=[]
for i in range(10):
    x.append(random.randint(50,10))
    y.append(random.randint(50,10))
    size.append(random.randint(10,10))
plt.scatter(x,y,s=size)
plt.show()

#%% 컬러바 추가
import matplotlib.pyplot as plt
import random
x=[]
y=[]
size=[]
for i in range(10):
    x.append(random.randint(50,100))
    y.append(random.randint(50,100))
    size.append(random.randint(10,100))
plt.scatter(x,y,s=size,c=size,cmap='jet')
plt.colorbar()
plt.show()

#%% 일부점들이 겹쳐서 보기 힘들네요. 투명도를 조절해 볼까요?
import matplotlib.pyplot as plt
import random

x=[]
y=[]
size=[]

for i in range(10):
    x.append(random.randint(50,100))
    y.append(random.randint(50,100))
    size.append(random.randint(10,100))
plt.scatter(x,y,s=size,c=size,cmap='jet',alpha=0.6) # alpha는 점의 투명도 조절
plt.colorbar()
plt.show()

#%% 연령대별 성별 비율을 산점도(버블차트)로 시각화
import csv
f=open('gender.csv')
data=csv.reader(f)
m=[]
f=[]

name=input('궁금한 동네를 입력하세요: ')
for row in data:
 if name in row[0]:
    for i in range(3,104):
        m.append(int(row[i]))
        f.append(int(row[i+103]))
    break

import matplotlib.pyplot as plt
plt.scatter(m,f)
plt.show()

#%% 남녀인구가 같은 기준선을 표시해서 그래프의 가치를 올려봅시다.
import matplotlib.pyplot as plt
plt.scatter(m,f)
plt.plot(range(0,max(m)),range(0,max(m)),'g')
plt.show()

#%% 지금 그린 그래프의 문제점이 무엇일까요? 연령대를 알 수가 없습니다. # 연령대 정보를 추가하기 위해 컬러맵을 적용해봅시다.
import matplotlib.pyplot as plt
plt.scatter(m,f,c=range(101),alpha=0.5,cmap='jet')
plt.colorbar()
plt.plot(range(0,max(m)),range(0,max(m)),'g')
plt.show()

#%% 이제 점의 크기로 남녀의 인구를 합한 인구수를 나타내게 한다면 더 좋겠죠?
import csv
f=open('gender.csv')
data=csv.reader(f)
m=[]
f=[]
size=[]

name=input('궁금한 동네를 입력하세요: ')
for row in data:
    if name in row[0]:
        for i in range(3,104):
            m_temp=int(row[i])
            f_temp=int(row[i+103])
            m.append(m_temp)
            f.append(f_temp)
            size.append(m_temp+f_temp)
        break

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rc('font',family='Malgun Gothic')
plt.title(name+' 지역의 성별 인구 그래프')
plt.scatter(m,f,s=size,c=range(101),alpha=0.5,cmap='jet')
plt.colorbar()
plt.plot(range(0,max(m)),range(0,max(m)),'g')
plt.xlabel('남성인구수')
plt.ylabel('여성인구수')
plt.show()

#%% 괜찮은 그래프가 나왔지만 버블이 너무 크죠?
import csv
f=open('gender.csv')
data=csv.reader(f)
m=[]
f=[]
size=[]

name=input('궁금한 동네를 입력하세요: ')
for row in data:
    if name in row[0]:
        for i in range(3,104):
            m_temp=int(row[i])
            f_temp=int(row[i+103])
            m.append(m_temp)
            f.append(f_temp)
            size.append(0.3*(m_temp+f_temp)) # 버블의 크기를 70% 축소
        break
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rc('font',family='Malgun Gothic')
plt.title(name+' 지역의 성별 인구 그래프')
plt.scatter(m,f,s=size,c=range(101),alpha=0.5,cmap='jet')
plt.colorbar()
plt.plot(range(0,max(m)),range(0,max(m)),'g')
plt.xlabel('남성인구수')
plt.ylabel('여성인구수')
plt.show()
# %%

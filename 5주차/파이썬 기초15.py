#%% 참고 교재: 모두의 데이터 분석 with 파이썬 p.204 ~ p.26
#%% 1. numpy 라이브러리 소개
# 앞선 실습에서 우리는 random라이브러리에서 randint()함수를 사용해서 정수 난수를
# 생성한 경우가 있었습니다. 그리고 그 때 생성된 난수를 저장하기 위해서 공갈리스트를
# 먼저 생성하고 for문을 활용하였습니다. # 이제 이번 시간에 우리는 numpy라이브러리를 통해서 동일한 작업을 해 볼 예정입니다. # 그럼 어차피 동일한 작업을 하는데 왜 numpy라이브러리를 활용해야 하지? 라는 
# 의문이 드는 것이 당연하겠죠. 
# numpy라이브러리를 사용하면 다음과 같은 장점이 있습니다.
# [numpy 라이브러리의 장점]
# 1. 수학, 선형대수, 통계학, 금융에서 많이 사용하는 다양한 함수를 제공하므로
# 여러가지 다양한 라이브러리를 불러올 필요가 없음
# 2. 코드가 간결, 예를 들어 for문을 사용할 필요가 없어짐
# 3. 동일한 작업을 위한 코드를 실행하였을 경우 연산시간(computing time)이 짧음
#%% 2. numpy라이브러리 시작하기
#%% 수학함수 활용 예제
# 먼저 2의 제곱근을 출력해 봅시다.
#print(sqrt(2))

import numpy
print(numpy.sqrt(2))
# 동일한 코드
import math # numpy와 동일한 기능을 사용할 수 있다.
print(math.sqrt(2))


# 원주율과 삼각함수를 사용
import numpy as np
print(np.pi) # 상용변수
print(np.sin(0))
print(np.cos(np.pi))

#%% 통계함수 활용 예제
import numpy as np
a=np.random.rand(5) # 0과 1사이에 있는 실수를 생성하여서 5*1을 갖는 배열로 저장
# rand(d0): [0,1]사이에 있는 실수를 생성하여 d0X1크기를 갖는 1차원 배열로 저장
print(a)
print(type(a)) # numpy는 array가 아니다.


#%% 실행결과를 보니 a의 타입이 'numpy.ndaray'입니다. # 'ndaray'는 'N-Dimensional 배열(N차원 배열)': 쉽게 말해 행렬(matrix)
# Variable explorer에서 a를 열고 type을 확인해 보세요. b=np.random.rand(5,5) 
# rand(d1,d2): [0,1]사이에 있는 실수를 생성하여 d0Xd1 크기를 갖는 2차원 배열로 저장

import numpy as np
c=np.random.rand(2,5,5) 
# rand(d1,d2,d3): [0,1]사이에 있는 실수를 생성하여 d0Xd1Xd2 크기를 갖는 다차원 배열로 저장
print(c)
print(np.random.choice(6,6))
# 0과 5사이의 정수를 반복해서 랜덤하게 6개 생성
print(np.random.choice(6,6,replace=False))
# 0과 5사이의 정수를 반복을 허락하지 않고 랜덤하게 6개 생성
print(np.random.choice(6,3,p=[0.1, 0.2, 0.3, 0.2, 0.1, 0.1]))
# 0과 5사이의 정수가 뽑힐 확률을 지정하여 반복을 허락하고 생성
print(np.random.choice(6,3,p=[0.1, 0.2, 0.3, 0.2, 0.1, 0.1], replace=False))
# 0과 5사이의 정수가 뽑힐 확률을 지정하여 반복을 허락하지 않고 생성


#%% 3. numpy라이브러리를 사용하면 코드가 정말 간결하고 빠른가?
# 예전 코드
import time
tic=time.clock() # stopwatch tic
import matplotlib.pyplot as plt
import random
dice=[]

for i in range(10): # numpy보다 이게 더 빠른 이유는 여기에 횟수가 너무 작기 때문이다
    dice.append(random.randint(1,6))
print(dice)
plt.hist(dice,bins=6)
plt.show()
elapse_random=time.clock()-tic # stopwatch toc , 경과시간

#%% numpy를 활용한 코드
import time
tic=time.clock()
import matplotlib.pyplot as plt
import numpy as np
dice=np.random.choice(6,10)
plt.hist(dice,bins=6)
plt.show()
elapse_numpy=time.clock()-tic
# 왜 numpy가 빠를까?


#%% [과제15-1] 지난 시간 학습했던 다음 코드를 numpy를 사용하여 변경하여 코드와 
# 결과물을 제출하세요.
import matplotlib.pyplot as plt
import random
x=[]
y=[]
size=[]
for i in range(10):
    x.append(random.randint(50,100))
    y.append(random.randint(50,100))
    size.append(random.randint(10,100))
plt.scatter(x,y,s=size)
plt.show()

# 컬러바 추가
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


#%% numpy의 다양한 함수들
# htps:/docs.scipy.org/doc/numpy-1.13.0/reference/
#%% 4. numpy aray생성하기
# list와 numpy aray 차이
import matplotlib.pyplot as plt
import random
dice1=[]

for i in range(10):
    dice1.append(random.randint(1,6))

print(dice1) # 쉼표로 구분

import matplotlib.pyplot as plt
import numpy as np
dice2=np.random.choice(6,10)
print(dice2) # 쉼표가 없음

#%% list를 numpy aray로 넘겨볼까요?

import numpy as np
a=np.array([1,2,3,4])
print(a) # list가 numpy aray로 저장
print(a[1],a[-1]) # list와 동일하게 인데싱 사용 가능
print(a[1:]) # list와 동일하게 슬라이싱도 사용 가능
# list는 숫자, 문자열, 리스트를 다양하게 동시에 저장 가능
# numpy aray는 한 가지 타입의 데이터만 저장 가능
a1=[1,2,'3',4]
import numpy as np
a2=np.array([1,2,'3',4])
print(a2)

#%% numpy aray를 생성하는 다양한 방법
import numpy as np
a=np.zeros(10) # 0으로 이루어진 크기가 10X1인 배열
b=np.ones(10) # 1로 이루어진 크기가 10X1인 배열
c=np.eye(10) # 크기가 10X10인 단위 행렬
d=np.arange(3) # 0부터 3보다 적을 때 까지 1씩 증가시키면서 1차원 배열
e=np.arange(3,7) # 3부터 7보다 적을 때 까지 1씩 증가시키면서 1차원 배열
f=np.arange(3,7,0.2) # 3부터 7보다 적을 때 까지 0.2씩 증가시키면서 1차원 배열 
g=np.linspace(1,2,1) # 1보다 크거나 같고 2보다 작거나 같은 구간을 1개의 구간으로 나눈 1차열 배열
print('a', a)
print('b', b)
print ('c', c) 
print(d)
print( e)
print( f)
print( g)
#%% 5. numpy aray의 다양한 활용
# 모든 원소에 동시에 적용되는 연산
import numpy as np
a=np.zeros(10)
b=a+5
print(b)
a=np.linspace(1,2,1)
b=np.sqrt(a)
print(a,b)
# sin, cos 함수를 그려 봅시다.
import matplotlib.pyplot as plt
import numpy as np
a=np.arange(-np.pi, np.pi, np.pi/10)
plt.plot(a,np.sin(a))
plt.plot(a,np.cos(a))
plt.show()
# for반복문을 사용해서 하나씩 값을 계산할 필요가 없어서 편합니다.


#%% mask 기능: 조건에 부합하는 원소만 선택
import numpy as np
a=np.arange(-2,2)
print(a)
print(a<0)
mask=a<0
b=a[mask]
print(b)
# 몇 개의 마스크를 연결해서 사용
mask1=abs(a)>1
mask2=abs(a)%2==0
print(mask1, mask2)
b=a[mask1+mask2]
c=a[mask1*mask2]
print(mask1+mask2)
print(mask1*mask2)
# mask1 mask2 mask1+mask2
# 1 1 1
# 0 0 0
# 0 1 1
# 0 0 0
# mask1 mask2 mask1*mask2
# 1 1 1
# 0 0 0
# 0 1 0
# 0 0 0
 

#%% numpy를 사용하여 버블차트 그리기
import matplotlib.pyplot as plt
import numpy as np
x=np.random.randint(-100,100,1000)
y=np.random.randint(-100,100,1000)
size=np.random.rand(100)*100+10
mask1=abs(x)>50
mask2=abs(y)>50
x=x[mask1+mask2]
y=y[mask1+mask2]
plt.scatter(x,y,s=size,c=x,cmap='jet',alpha=0.7)
plt.colorbar()
plt.show()
# %%

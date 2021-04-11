""""""""""""""""""""""""""" 파이썬 기초 """""""""""""""""""""""""""""""""""""""
#%% 참고 교재: 모두의 데이터 분석 with 파이썬 p.54 ~ p.94

#%% 1. 기본 그래프 그리기

# 파이썬으로 데이터를 시각화하는 데는 matplotlib라이브러리를 많이 사용
# matplotlib 라이브러리는
#  - 2D형태의 그래프, 이미지 등 
#  - matplotlib의 튜토리얼: https://matplotlib.org 참조
#  - matplotlib을 사용하는 방법에는 두가지가 존재
#     i) 그림과 축의 객체(object)를 생성하고 각 객체의 매서드(method)를 호출하여 그림 생성
#    ii) pyplot을 사용하여 그림과 축을 생성 및 관리
#  - 여기서는 ii)번 방식 사용

#%% 1-1. plot()함수를 사용한 기본 그래프
# plot함수()사용한 기본 그래프 구성
# import matplotlib.pyplot as plt: 라이브러리 불러오기
# plt.plot([x축 데이터],[y축 데이터]): plot()함수에 데이터 입력
# plt.show(): 그림을 보여주는 함수
import csv
f = open('seoul.csv', 'r', encoding='cp949')
data = csv.reader(f, delimiter=',')
print(data)
f.close()

# 간단한 예제
import matplotlib.pyplot as plt
plt.plot([3,4,5,6],[23,35,42,30])
plt.show()

# 만약 데이터 리스트를 하나만 주게 되면? x을 0부터 자동으로 생성
import matplotlib.pyplot as plt
plt.plot([23,35,42,30])
plt.show()

#%% 1-2. 그래프에 옵션 추가하기
# 제목 넣기
import matplotlib.pyplot as plt
plt.title('plotting exercise')    # plt.title과 plt.plot 순서는 중요하지 않음
plt.plot([3,4,5,6],[23,35,42,30])
plt.show()

import matplotlib.pyplot as plt
plt.plot([3,4,5,6],[23,35,42,30])

plt.show()
plt.title('plotting exercise')    # plt.title과 plt.plot 순서는 중요하지 않음

# 선을 하나 더 추가한 후 범례 넣기
import matplotlib.pyplot as plt
plt.title('plotting exercise')    
plt.plot([3,4,5,6],[23,35,42,30], label='line 1')
plt.plot([3,4,5,6],[33,22,43,25], label='line 2')
plt.legend()
plt.show()

# plt.legend(): 특별히 명시하지 않으면 범례의 위치는 자동으로 결정되지만 
# plt.legend(loc=5)와 같이 지정할 수도 있음
# -----------------
# |  2  |  9  |  1  |
# -------------------
# |  6  | 10  | 5,7 |
# -------------------
# |  3  |  8  |  4  |
# -------------------

import matplotlib.pyplot as plt
plt.title('plotting exercise')    
plt.plot([3,4,5,6],[23,35,42,30], label='line 1')
plt.plot([3,4,5,6],[33,22,43,25], label='line 2')
plt.legend(loc=2)
plt.show()

# 그래프 색상 바꾸기
import matplotlib.pyplot as plt
plt.title('plotting exercise')    
plt.plot([3,4,5,6],[23,35,42,30], label='line 1', color='skyblue') # color속성 추가
plt.plot([3,4,5,6],[33,22,43,25], 'pink', label='line 2', )  # color를 명시하지 않으면 순서가 중요
plt.legend(loc=2)
plt.show()

# 색상을 표현할 때 약자도 사용가능
# r: red
#g: green
#b: blue
#k: black
#y: yellow

# 선 모양 변경
import matplotlib.pyplot as plt
plt.title('plotting exercise')    
plt.plot([3,4,5,6],[23,35,42,30], label='line 1', color='skyblue', linestyle='--')
# linestyle 속성 추가
plt.plot([3,4,5,6],[33,22,43,25], 'pink', label='line 2', ls=':')  
# linestyle을 ls로 줄여도 가능
plt.legend(loc=2)
plt.show()
# '-', '--', '-.', ':' 등 여러가지 시도해 보세요.


# 마커(marker) 바꾸기
import matplotlib.pyplot as plt
plt.title('plotting exercise')    
plt.plot([3,4,5,6],[23,35,42,30], label='line 1', color='skyblue', marker='.',  linestyle='--')
# linestyle 속성 추가
plt.plot([3,4,5,6],[33,22,43,25], color='pink', marker='^',  ls=':', label='line 2')  
# linestyle을 ls로 줄여도 가능
plt.legend(loc=2)
plt.show()
# 인터넷에서 'matplotlib marker'로 검색해서 다양한 마커를 확인하고 시도해 보세요.





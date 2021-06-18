""""""""""""""""""""""""""" 파이썬 기초 """"""""""""""""""""""""""""""""""""""" 
#%% 참고 교재: 데이터 분석을 위한 판다스 입문 p.80 ~ p.87
# 수백, 수천, ..., 수억 줄의 자료로 이루어진 데이터를 읽고 기초 통계 수치를 계산하는
# 방법으로는 데이터를 제대로 이해하기 어려움
# 이런한 경우 데이터 시각화는 데이터의 숨겨진 패턴을 찾거나 이해하는데 많은 도움을 줌

#%% 1.Anscombe 4분할 그래프
# 데이터 시각화의 필요성을 보여주는 전형적인 사례: 앤스콤 4분할 그래프
# 앤스콤 4분할 그래프를 구성하는 데이터 집합은 4개의 그룹으로 구성
# 각 데이터 그룹은 평균, 분산, 상관계수, 회귀선(기초 통계 수치)가 동일하다는 특징
# 하지만 각 데이터 그룹을 시각화하면 완전히 서로 다른 데이터 패턴을 가짐
import seaborn as sns
import matplotlib.pyplot as plt
anscombe=sns.load_dataset("anscombe")
print("----------------------------1------------------------")
print(anscombe)
# 데이터프레임 형태의 데이터인 anscombe이 만들어지고, 'dataset'열이 데이터의 그룹을
# 표시하고 있음
# 데이터 그룹별로 새로운 데이터셋을 생성
dataset_1=anscombe[anscombe['dataset']=='I']
dataset_2=anscombe[anscombe['dataset']=='II']
dataset_3=anscombe[anscombe['dataset']=='III']
dataset_4=anscombe[anscombe['dataset']=='IV']
print("----------------------------2------------------------")
print(dataset_1)
print("----------------------------3------------------------")
print(dataset_2)
print("----------------------------4------------------------")
print(dataset_3)
print("----------------------------5------------------------")
print(dataset_4)

#%% 기초 통계량 확인하기
import pandas as pd
Stats_1=[dataset_1.mean(), dataset_1.std()] # NOTE 평균, 표준편차 -> 거의 4개가 동일한 data이다.
Stats_2=[dataset_2.mean(), dataset_2.std()]
Stats_3=[dataset_3.mean(), dataset_3.std()]
Stats_4=[dataset_4.mean(), dataset_4.std()]
print("----------------------------1------------------------")
print(Stats_1)
print("----------------------------2------------------------")
print(Stats_2)
print("----------------------------3------------------------")
print(Stats_3)
print("----------------------------4------------------------")
print(Stats_4)

Corr_1=dataset_1.corr() # NOTE 상관계쑤
Corr_2=dataset_2.corr()
Corr_3=dataset_3.corr()
Corr_4=dataset_4.corr()
print("----------------------------1------------------------")
print(Corr_1)
print("----------------------------2------------------------")
print(Corr_2)
print("----------------------------3------------------------")
print(Corr_3)
print("----------------------------4------------------------")
print(Corr_4)

#%% 이제 matplotlib라이브러리로 그래프를 그려 봅시다.
# ----------------------------------------- # matplotlib으로 그래프를 그리는 순서
#------------------------------------------
# 1. 전체 그래프가 위치할 기본 틀을 만듦
# 2. 그래프를 그려 넣을 그래프 격자를 만듦
# 3. 격자에 그래프를 하나씩 추가
#------------------------------------------
# 1. 전체 그래프가 위치할 기본 틀 생성
fig=plt.figure()
# 2. add_subplot 메서드로 그래프 격자 생성
axes1=fig.add_subplot(2,2,1) # add_subplot(행크기, 열크기, 위치)
axes2=fig.add_subplot(2,2,2)
axes3=fig.add_subplot(2,2,3)
axes4=fig.add_subplot(2,2,4)
# 3. 격자에 그래프를 하나씩 추가
#axes1.plot(dataset_1['x'], dataset_1['y'])
axes1.plot(dataset_1['x'], dataset_1['y'],'o')
axes2.plot(dataset_2['x'], dataset_2['y'],'o')
axes3.plot(dataset_3['x'], dataset_3['y'],'o')
axes4.plot(dataset_4['x'], dataset_4['y'],'o')
# 격자에 제목 추가
axes1.set_title("dataset I")
axes2.set_title("dataset II")
axes3.set_title("dataset III")
axes4.set_title("dataset IV")
# 기본 틀에 제목 추가
fig.suptitle("Anscombe Data")
# sub 그래프 간격 자동 조절
fig.tight_layout()
# %%

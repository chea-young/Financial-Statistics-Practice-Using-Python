""""""""""""""""""""""""""" 파이썬 기초 """"""""""""""""""""""""""""""""""""""" 
#%% 참고 교재: 데이터 분석을 위한 판다스 입문 p.95 ~ p.97
# seaborn 라이브러리를 사용하면 matplotlib라이브러리를 사용하는 것보다
# 좀 더 화려한 그래프를 그릴 수 있음
# 참고로, seaborn라이브러리는 matplotlib라이브러리를 기반으로 만든 라이브러리

#%% 1. 단변량 그래프 그리기 - 히스토 그램
import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")
# sns라이브러리에서 히스토그램 그리는 메서드는 distplot()으로 histogram과 더불어
# kernel density도 함게 보여 줌
ax=plt.subplots()
#ax=sns.distplot(tips['total_bill'])
#ax=sns.distplot(tips['total_bill'], kde=False) # kernel density를 보기 싫은 경우
#ax=sns.distplot(tips['total_bill'], hist=False) # histogram을 보기 싫은 경우
ax=sns.distplot(tips['total_bill'], rug=True) # 자료의 밀집도를 보고 싶은 경우
# 자료가 있는 위치에 동일한 길이의
# 직선을 표시
ax.set_title('Total Bill Histogram with Density Plot')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Frequency')

#%% 2. 단변량 그래프 그리기 - count 그래프
# 히스토그램과 count 그래프의 차이는 x축이 히스토그램의 경우 연속값이고, # count 그래프의 경우 x축이 이산형값인 경우 (사실 구분의 의미는 없지만...)
ax=plt.subplots()
#ax=sns.countplot('day', data=tips)
ax=sns.countplot(tips['day'])
ax.set_title('Count of days')
ax.set_xlabel('Day of the Week')
ax.set_ylabel('Frequency')
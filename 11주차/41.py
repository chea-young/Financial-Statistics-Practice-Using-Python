""""""""""""""""""""""""""" 파이썬 기초 """"""""""""""""""""""""""""""""""""""" #%% 참고 교재: 데이터 분석을 위한 판다스 입문 p.99 ~ p.112
# seaborn 라이브러리를 사용하여 다양한 종류의 이변량 그래프를 그려 봅시다.
#%% 1. 산점도 그래프 그리기
# seaborn라이브러리에서 산점도 그래프를 그리기 위해서 regplot()메서드 사용
# regplot()메서드는 산점도와 회귀직선을 함께 그릴 수 있으며, 만약 회귀선을 제거하려면
# fit_reg인자를 False로 지정
# NOTE 회귀분석: 잘 설명하는 직선의 절편과 기울기는 찾는 것, 그리고 그 변수와의 관계를 설명하는 것
# NOTE 거리를 최소화시켜주는 두 변수를 찾는데 -> 최소 제곱법

import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")

ax=sns.regplot(x='total_bill', y='tip', data=tips, ci=95) # ci: 기울기와 절편의 신뢰구간
ax.set_title('Scatter plot of Total Bill and Tip')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Tip')

#%% 회귀선을 지우고 단순한 산점도만 그려 봅시다. 
ax=plt.subplots()
ax=sns.regplot(x='total_bill', y='tip', data=tips, fit_reg=False) # ci: 기울기와 절편의 신뢰구간
ax.set_title('Scatter plot of Total Bill and Tip')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Tip')

#%% 2. 산점도와 히스토그램을 한번에 그리기: joinplot()메서드
joint=sns.jointplot(x='total_bill',y='tip',data=tips)
joint.set_axis_labels(xlabel='Total Bill',ylabel='Tip') # NOTE 축 이름 지정
joint.fig.suptitle('Joint Plot of Total Bill and Tip',fontsize=10, y=1.1) # y인자는 제목의위치 지정
# 산점도와 히스트그램을 한번에 그리면 각각의 일변량에 대한 정보와 두 변수간의
# 이변량 정보를 동시에 전달하여 효율적
# NOTE 중앙에는 산점도 각 위와 오른쪽에는 히스토그램이 나와있다 -> 히스토그램이 높은 곳이 total_bill이나 tip이 많이 몰려있는 것

#%% 3. 육각 그래프(hexbin)
# 산점도 그래프는 점이 겹쳐 보일 경우 점을 구분하기 어려움. 
# 육각 그래프는 2차원 표면에 육각형으로 데이터를 쌓아 표현하는 그래프로서
# 특정 데이터의 개수가 많아지면 점점 진한 색으로 표현
hexbin=sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')
hexbin.set_axis_labels(xlabel='Total Bill',ylabel='Tip')
hexbin.fig.suptitle('Hexbin Joint Plot of Total Bill and Tip',fontsize=10,y=1.03)

#%% 4. 이차원 밀집도 그리기: kdeplot()메서드
ax=sns.kdeplot(data=tips['total_bill'],data2=tips['tip'],
 shade=True, # shade 인자: 음영 추가
 n_levels=5, # 동고선 갯수
 cmap="Blues", # 색지정
 cbar=True) # 등고선에 대한 colorbar 정보
ax.set_title('Kernel density Plot of Total Bill and Tip')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Tip')

#%% 남여 두 경우로 나누어 그려봅시다. 
ax=sns.kdeplot(
    data=tips[tips['sex']=='Male']['total_bill'],
    data2=tips[tips['sex']=='Male']['tip'],
 shade=True, # shade 인자: 음영 추가
 n_levels=5, # 동고선 갯
 cmap="Reds", # 색지정
 cbar=True,
 alpha=0.3) # 투명도

ax=sns.kdeplot(
    data=tips[tips['sex']=='Female']['total_bill'],
    data2=tips[tips['sex']=='Female']['tip'],
 shade=True, # shade 인자: 음영 추가
 n_levels=5, # 동고선 갯
 cmap="Blues", # 색지정
 cbar=True,
 alpha=0.3
 ) # 등고선에 대한 colorbar 정보
ax.set_title('Kernel density Plot of Total Bill and Tip')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Tip')

#%% 5. 바 그래프 그리기
# 바 그래프는 지정한 변수의 평균을 계산하여 바 형태로 그림
ax=sns.barplot(x='time',y='total_bill',data=tips)
ax.set_title('Bar Plot of average total bill for time of day')
ax.set_xlabel('Time of day')
ax.set_ylabel('Average total bill')

#%% 6. 박스 그래프 그리기
ax=sns.boxplot(x='time',y='total_bill', data=tips)
ax.set_title('Boxplot of total bill by tiem of day')
ax.set_xlabel('Time of day')
ax.set_ylabel('Total Bill')

#%% 7. 바이올린 그래프
# 박스 그래프는 다양한 통계 수치를 제공하지만, 데이터의 전체적인 분포 표현이 필요한 경우도 있음
# 이런 경우 박스그래프와 함께 바이올린 그래프를 그리면 편리
ax=sns.violinplot(x='time',y='total_bill',data=tips, hue='sex', split=True)
ax.set_title('Violin plot of total bill by tiem of day')
ax.set_xlabel('Time of day')
ax.set_ylabel('Total Bill')

#%% 8. 관계 그래프 그리기
# 관계 그래프는 범주형 변수를 제외한 숫자형 변수에 대하여 히스토그램과 산점도를 함께보여줌 
# NOTE -> 여기서는 total_bill,size/ total_bill,tip/ tip,size 총 3개가 나옴
fig=sns.pairplot(tips)
fig=sns.pairplot(tips, hue='sex') # hue는 색깔을 따로 입힐 변수를 지정

#%% 위의 관계 그래프에서 대각의 히스토그램을 중심으로 비대각 그림은 동일한 그림으로서
# 중복된 정보를 전달 -> NOTE 그래서 비효율적이다.
# 중복된 그래프가 그려지는 위치를 직접 지정하고 원하는 그래프로 교체 가능 => PairGrid()

pair_grid=sns.PairGrid(tips) # NOTE PairGrid를 따라서 그림을 그린다.
pair_grid.map_upper(sns.regplot)# NOTE 대각 위
pair_grid.map_lower(sns.kdeplot) # NOTE 대각 아래
pair_grid.map_diag(sns.distplot, bins=3, rug=True)

#%% 9. 산점도 그래프 - 색상 추가
# 위에서 사용한 regplot()메서드도 산점도를 그리기는 좋으나 hue인자 사용 불가
# NOTE hue는 파라미터로 카ㅔ고리 변수를 지정하여 카테고리별로 각각 데이터의 분포와 선형관계 표현 가능
# 이런 경우는 lmplot()메서드 사용
ax=sns.regplot(x='total_bill', y='tip', data=tips, ci=100, hue='sex') # NOTE hue가 있어서 에러
#%%
scatter=sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', fit_reg=True) #NOTE 하지만 lmplot는 hue 사용 가능

#%% 추가적인 정보(size)를 점의 크기로 반영
scatter=sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', fit_reg=True, scatter_kws={'s': tips['size']*10})

#%% 남녀 marker 설정
scatter=sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', fit_reg=True,
 markers=['o','x'], scatter_kws={'s': tips['size']*10}) # 추가적인 정보(size)를 점의 크기로 반영

#%% 10. FacetGrid 클래스를 사용 그리기
# 여러개의 범주를 가지는 변수에 대하여 여러가지 그래프를 그리는 경우 FacetGrid를
# 사용하면 간편하게 그릴 수 있음
#%% 예제 1
facet=sns.FacetGrid(tips, col='time') # col인자를 사용하여 여러개의 동일한 그래프를 그릴 범주형 변수를 지정
facet.map(sns.distplot, 'total_bill', rug=True)

#%% 예제 2
print(tips['day'])
facet=sns.FacetGrid(tips, col='day', hue='sex')
facet.map(plt.scatter, 'total_bill','tip')
facet.add_legend()

#%% 예제 3
facet=sns.FacetGrid(tips, col='time',row='smoker',hue='sex') #NOTE hue로 들어간 sex가 Female가 Male이기 때문에 색이 2개인 그래프 생성
facet.map(plt.scatter, 'total_bill', 'tip')

#%% [과제 41-1] "gapminder.tsv" 데이터에 대하여 FacetGrid를 사용하여 국가별 lifeExp, pop, gdpPercap
# 의 데이터를 설명할 그래프를 그려보시오. # 예제:
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('gapminder.tsv', sep='\t')
facet=sns.FacetGrid(df, row='country')
facet.map(plt.plot, 'year','lifeExp')
# %%

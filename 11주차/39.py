""""""""""""""""""""""""""" 파이썬 기초 """"""""""""""""""""""""""""""""""""""" #%% 참고 교재: 데이터 분석을 위한 판다스 입문 p.88 ~ p.94
# matplotlib라이브러리에서 제공하는 기본 그래프를 그려 보도록 합시다.
#%% 1. 기초 그래프를 그릴 데이터 생성하기
import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")

#%% 2. 히스토그램 그리기
# 1. 전체 그래프가 위치할 기본 틀을 만듦
fig=plt.figure()
# 2. add_subplot 메서드로 그래프 격자 생성
axes1=fig.add_subplot(1,1,1)
# 3. 격자에 그래프를 하나씩 추가
axes1.hist(tips['total_bill'], bins=10, color='b') # bins: 막대의 수
axes1.set_title('Histogram of Total Bill')
axes1.set_xlabel('Total Bill')
axes1.set_ylabel('Frequency')

#%% 3. 산점도 그리기
scatter_plot=plt.figure()
axes1=scatter_plot.add_subplot(1,1,1)
axes1.scatter(tips['total_bill'], tips['tip'], color='b')
axes1.set_title('Scatter plot of Total Bill vs Tip')
axes1.set_xlabel('Total Bill')
axes1.set_ylabel('Tip')

#%% 3. Boxplot 그리기
boxplot=plt.figure()
axes1=boxplot.add_subplot(1,1,1)
#axes1.boxplot(tips[tips['sex']=='Female']['tip'],labels=['Female'])
#fig

axes1.boxplot([tips[tips['sex']=='Female']['tip'],
 tips[tips['sex']=='Male']['tip']],
 labels=['Female','Male'])

axes1.set_xlabel('Sex')
axes1.set_ylabel('Tip')
axes1.set_title('Boxplot of Tips by Sex')

#%% Boxplot 해석
# 상자 가운데 빨간선: Median (중위수; 2nd quantile; Q2; 50th percentile)
# 상자 아래선: 1st quantile (1사분위수; Q1: 25th percentile)
# 상자 윗선: 3rd quantile (3사분위수; Q3; 75th percentile)
# Inter-Quantile Range (IQR) = Q3-Q1
# 상자 아래의 가로선: Q1-1.5*IQR의 값보다 큰 값 중에서 최소값
# 상자 위의 가로선: Q3+1.5*IQR의 값보다 작은 값 중에서 최대값
# 둥근 점: Q1-1.5*IQR의 값보다 작거나 Q3+1.5*IQR의 값보다 큰 값으로서 이상치(outlier)

#%% 사용자 컬러 정의 방법
# matplotlib에서 사용자가 컬러를 정의하는 방법
# 1. 삼중(triplet): 컬러를 빨강, 초록, 파랑성분의 삼중 값으로 설정하는 것으로
# 각 성분값은 0과 1사이
fig=plt.figure()
axes1=fig.add_subplot(1,1,1)
axes1.hist(tips['total_bill'], bins=10, color=(0,0,1))
axes1.set_title('Histogram of Total Bill')
axes1.set_xlabel('Frequency')
axes1.set_ylabel('Total Bill')

#%% 2. 사중(quadruplet): 삼중처럼 작동하며, 마지막에 투명 값을 추가
fig=plt.figure()
axes1=fig.add_subplot(1,1,1)
axes1.hist(tips['total_bill'], bins=10, color=(0,0,1,0.1))
axes1.set_title('Histogram of Total Bill')
axes1.set_xlabel('Frequency')
axes1.set_ylabel('Total Bill')

#%% 3. 사전 정의 이름: 미리 정의된 문자열을 사용
# --------------------- # 문자 컬러
#----------------------
# b blue
# g green
# r red
# c Cyan
# m Magenta
# y Yellow
# k Black
# w White
# --------------------- # 4. HTML 컬러 문자열: 웹에서 RGB 색상표 검색하여 사용
fig=plt.figure()
axes1=fig.add_subplot(1,1,1)
axes1.hist(tips['total_bill'], bins=10, color='#483D8B')
axes1.set_title('Histogram of Total Bill')
axes1.set_xlabel('Frequency')
axes1.set_ylabel('Total Bill')
#%% 5. 회색 계열: 0과 1사이 값을 문자열로 설정
fig=plt.figure()
axes1=fig.add_subplot(1,1,1)
axes1.hist(tips['total_bill'], bins=10, color='0.5')
axes1.set_title('Histogram of Total Bill')
axes1.set_xlabel('Frequency')
axes1.set_ylabel('Total Bill')
# 6. 데이터로 넘겨 주는 방법: 아래 다변량 그래프 그리기를 보세요.
#%% 4. 다변량 그래프 그리기
# 앞서 산점도에서 total_bill과 tip을 산점도로 그렸습니다. # 여기에 성별을 추가하여 산점도는 어떻게 그릴까요?
# 남자는 빨간점으로 여자는 파란점으로 그리면 정보를 하나 더 추가할 수 있겠죠?
# 여기에 또 하나의 정보를 추가하여 식사 인원을 점의 크기로도 표현할 수 있겠죠?
# tips 데이터프레임에서 성별을 색상으로 사용하면 좋을 것 같은데
# Female, male과 같은 문자열은 색상으로 지정하는 값으로 사용이 불가능합니다. 
# 따라서 Female을 0으로 Male을 1로 바꾸기 위해 다음 함수를 정의합시다. 
def recode_sex(sex):
    if sex=='Female':
        return 0
    else:
        return 1
tips['sex_color']=tips['sex'].apply(recode_sex)

scatter_plot=plt.figure()
axes1=scatter_plot.add_subplot(1,1,1)
axes1.scatter(x=tips['total_bill'],
 y=tips['tip'],
 s=tips['size']*10, # size (점의 크기)
 c=tips['sex_color'], # color (점의 색깔)
 alpha=0.5) # alpha는 점의 투명도
axes1.set_title('Total Bill vs Tip Colored by Sex and Size')
axes1.set_xlabel('Total Bill')
axes1.set_ylabel('Tip')

#%% [과제 39-1] 위의 tip에 대한 산점도에서 범례 등을 추가하여 그래프를 화려하게
# 꾸며보세요.
def recode_sex(sex):
    if sex=='Female':
        return 0
    else:
        return 1
tips['sex_color']=tips['sex'].apply(recode_sex)

scatter_plot=plt.figure()
axes1=scatter_plot.add_subplot(1,1,1)
axes1.scatter(x=tips['total_bill'],
 y=tips['tip'],
 s=tips['size']*10, # size (점의 크기)
 c=tips['sex_color'], # color (점의 색깔)
 alpha=0.5) # alpha는 점의 투명도
axes1.set_title('Total Bill vs Tip Colored by Sex and Size',fontsize = 20)
axes1.set_xlabel('Total Bill',fontsize = 18)
axes1.set_ylabel('Tip',fontsize = 18)
axes1.legend(loc=(1.005, 0.9), ncol=1,frameon=True, shadow=True) # NOTE 범례추가, loc는 위치, ncol는 범례를 나타낼 때 열 개수
plt.rc('xtick', labelsize=15) 
plt.rc('ytick', labelsize=15)
# %%

""""""""""""""""""""""""""" 파이썬 기초 """"""""""""""""""""""""""""""""""""""" #%% 참고 교재: 데이터 분석을 위한 판다스 입문 p.217 ~ p.225
#%% 1. groupby()메서드 사용하여 데이터 집계하기
# 앞선 강의에서 gapminder.tsv 데이터 집합으로 groupby()메서드를 사용하여
# 각 연도의 평균 수명 구했었습니다. # 여기서는 groupby()메서드와 연계하여 집계할 수 있는 메서드들을 추가로 알아보고, # groupby()메서드와 사용자 정의 함수를 어떻게 연계하여 사용가능한지 알아 봅시다. # gapminder.tsv 불러오기
import pandas as pd
df=pd.read_csv('gapminder.tsv', sep='\t')
# year열을 기준으로 데이터를 그룹화한 다음 lifeExp의 열의 평균을 구해봅시다. avg_life_exp_by_year=df.groupby('year').lifeExp.mean()
# 이러한 grouby()메서드에 의한 절차는 
# 1. 원 자료를 year별로 데이터를 분할하고 (분할)
# 2. 각 분할된 데이터에서 평균을 구하고 (반영)
# 3. 연도별로 구한 평균을 다시 합침 (결합)
# 위의 세 단계(분할-반영-결합)를 거쳐서 완성
# groupby()메서드와 함께 사용하는 집계 메서드
#-----------------------------------------------------------------------------
# 메서드 \ 설명
#-----------------------------------------------------------------------------
# count \ 누락값을 제외한 데이터 수를 반환
# size \ 누락값을 포함한 데이터 수를 반환
# mean \ 평균값 반환
# std \ 표준편차 반환
# min \ 최솟값 반환
# quantile(q=0.25) \ 백분위수 25%
# quantile(q=0.50) \ 백분위수 50%
# quantile(q=0.75) \ 백분위수 75%
# max \ 최대 반환
# sum \ 전체 합 반환
# var \ 분산 반환
# sem \ 평균의 표준편차 반환
# describe \ 데이터 수, 평균, 표준편차, 최소값, 백분위수(25, 50, 75%), 최댓값을 모두 반혼
# first \ 첫 번째 행 반환
# last \ 마지막 행 반환
# nth \ n번째 행 반환
#-----------------------------------------------------------------------------

#%% 2. agg메서드로 사용자 함수와 groupby메서드 조합하기
# 마치 앞서 학습했던 사용자 함수를 apply메서드로 적용했던 것과 유사
# 1개 인자 예제
def my_mean(values):
 n=len(values)
 sum=0
 for value in values:
    sum+=value
 return sum/n
agg_my_mean=df.groupby('year').lifeExp.agg(my_mean)
print(df)
print(agg_my_mean)

#%% 2개 인자 예제
def my_mean_diff(values,diff_value):
 n=len(values)
 sum=0
 for value in values:
    sum+=value
 mean=sum/n
 return mean-diff_value
global_mean=df.lifeExp.mean()
print(global_mean)
agg_mean_diff=df.groupby('year').lifeExp.agg(my_mean_diff,diff_value=global_mean)
print(agg_mean_diff)

#%% 3. 여러개의 메서드 한 번에 사용하기
# numpy의 집계 메서드를 리스트로 담아 전달
import numpy as np
gdf=df.groupby('year').lifeExp.agg([np.count_nonzero, np.mean, np.std])
print(gdf)

# 딕셔너리의 키로 집계 메서드를 적용할 열 이름을 전달하고, 딕셔너리 값으로 집계 메서드를 전달
gdf_dic=df.groupby('year').agg({'lifeExp': 'mean', 'pop': 'median','gdpPercap':'median'}) # NOTE mean, median은 함수 
print(gdf_dic)
# %%

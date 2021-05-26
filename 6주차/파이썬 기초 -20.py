#%% 참고 교재: 데이터 분석을 위한 판다스 입문 p.48 ~ p.51
#%% 기초적인 통계 계산하기
# 데이터를 그룹별로 묶어서 그룹별 평균을 계산하여 보자
#%% 열 단위 데이터 추출하기
import pandas as pd
df=pd.read_csv('gapminder.tsv', sep='\t') # 나라별, 대륙별 데이터

#%% 데이터 출력해 봅시다
print(df.head(n=10)) # 데이터의 앞 부분만을 출력

#%% 연도별 lifeExp열의 평균을 계산해 봅시다. #%% 1. 데이터프레임을 연도별로 그룹화
grouped_year_df=df.groupby('year') # 데이터를 년도 별로 그룹회 -> year을 기준으로 묶이게 되는 것
print(type(grouped_year_df)) # 그룹화한 데이터의 자료형은 DataFrameGroupBy
print(grouped_year_df) # grouped_year_df가 저장된 메모리의 위치 확인


#%% 2. 그룹화한 데이터에서 lifeExp얼을 추출
grouped_year_df_lifeExp=grouped_year_df['lifeExp'] # 열 이름으로 묶이게 되는것 SeriesGroupBY로 변경된다.
print(type(grouped_year_df_lifeExp)) # lifeExp 하나만 가져와서 SeriesGroupBy

#%% 3. mean 메서드(함수)를 사용하여 연도별 lifeExp의 평균 계산
mean_lifeExp_by_year=grouped_year_df_lifeExp.mean()
print(mean_lifeExp_by_year)

#%% 위의 1~3 단계를 하나의 코드로 묶어 봅시다
print(df.groupby('year')['lifeExp'].mean())
mean_lifeExp_by_year_2=df.groupby('year')['lifeExp'].mean()

#%% lifeExp, gdpPercap열의 평균값을 연도별+대륙별로 그룹화하여 한번에 계산
multi_group_var=df.groupby(['year','continent'])['lifeExp','gdpPercap'].mean()

#%% nunique()함수를 사용하여 그룹화한 데이터 갯수 세기
print(df.groupby('continent')['country'].nunique())
print(df['country'].nunique())
# %%

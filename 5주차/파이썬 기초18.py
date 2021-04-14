#%% 참고 교재: 데이터 분석을 위한 판다스 입문 p.31 ~ p.35
#%% 판다스란?
# 판다스(Pandas; Panel Datas의 약자)는 데이터프레임(2차원 배열 형태)과 
# 시리즈(1차원 배열형태)라는 자료형과 데이터 분석을 위한 다양한 기능을 제공하는 
# 파이썬 라이브러리
#%% 데이터 불러오기
import pandas as pd
df=pd.read_csv('gapminder.tsv', sep='\t')
print(df.head()) # head()함수는 데이터프레임에서 가장 앞에 있는 5개의 행을 출력
#%% 자료형 확인
print(type(df))
#%% 데이터프레임은 데이터의 행과 열의 크기에 대한 정보를 shape이라는 속성이 저장
print(df.shape)
#%% columns 속성 사용하여 데이터 프레임의 열 이름 확인
print(df.columns) # Variable explorer를 열어서 열이름 확인도 해보세요. #%% 데이터프레임을 구성하는 값의 자료형은 데이터프레임의 dtypes 속성이나 
# info메서드로 확인 가능
print(df.dtypes)
#%% 판다스와 파이썬 자료형 비교
# --------------------------------- # 판다스 자료형 | 파이썬 자료형 | 설명
# --------------------------------- # object | string | 문자열
# int64 | int | 정수
# float64 | float | 실수
# datetime64 | datetime | 파이썬 표준 라이브러리인 datetime이 반환하는 자료형
# ---------------------------------
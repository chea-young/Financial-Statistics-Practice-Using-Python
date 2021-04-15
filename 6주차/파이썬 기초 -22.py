#%% 참고 교재: 데이터 분석을 위한 판다스 입문 p.69 ~ p.75
#%% 2-1. 데이터프레임 불린 추출: 시리즈와 동일하게 사용
import pandas as pd
scientists=pd.read_csv('scientists.csv')
old_scientists=scientists[scientists['Age']>scientists['Age'].mean()]
#%% 2-2. 데이터프레임 브로드캐스팅
old_scientists2=old_scientists*2 # 숫자데이터는 2를 곱한 숫자, 문자열은 2배로 늘어남
#%% 2-3. 시리즈와 데이터프레임 데이터 처리하기
# scientists데이터프레임의 Born과 Died열의 자료형을 확인해 봅시다. print(scientists['Born'].dtype)
print(scientists['Died'].dtype)
# 둘 다 모두 문자열(object)형태로 저장되어 있음
#%% 날짜 관련 데이터는 시간 관련 작업을 할 수 있도록 datetime자료형으로 바꾸는 것이 
좋음
born_datetime=pd.to_datetime(scientists['Born'], format='%Y-%m-%d')
died_datetime=pd.to_datetime(scientists['Died'], format='%Y-%m-%d')
#%% scientists데이터프레임에 born_datetime과 died_datetime열을 추가
scientists['born_dt'], scientists['died_dt']=(born_datetime, died_datetime)
# 데이터프레임에 없는 column명을 사용하여 무언가를 할당하면 새로운 열 추가
scientists['new_col_test']=0
# 시간 계산을 해봅시다
scientists['age_days_dt2']=(scientists['died_dt']-scientists['born_dt'])
#%% 데이터 섞기
# 특정한 열의 데이터만 섞어 봅시다.
import random
random.sed(42)
random.shufle(scientists['Age'])
print(scientists['Age'])

# 이러한 데이터 섞기는 통계학에서 bootstrap방법(어떤 통계량의 표준오차를 구하기 위한 
비모수적 방법)이나
# 금융에서 역사적 시뮬레이션 (historical simulation)에서 많이 사용
#%% 데이터프레임의 열 삭제하기
scientists_dropped=scientists.drop(['Age'], axis=1)
#%% 데이터프레임의 행 삭제하기
scientists_dropped=scientists.drop([0], axis=0)
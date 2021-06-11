#%% 참고 교재: 데이터 분석을 위한 판다스 입문 p.152 ~ p.165
#%% 1. 열과 피벗
# 필요한 데이터를 만들기 위해 필요한 여러가지 메서드를 알아봅시다. #%% melt 메서드
# 경우에 따라서는 열의 데이터를 행으로 옮겨서 정리해야할 경우가 존재하는데 
# 이럴 때 melt 메서드가 유용
# ------------------------------------------ 
# # melt 메서드 인자 \ 설명
# ------------------------------------------ 
# # id_vars \ 위치를 그대로 유지할 열의 이름 지정
# value_vars \ 행으로 위치를 변경할 열의 이름을 지정
# var_name \ value_vars로 위치를 변경한 열의 이름을 지정
# value_name \ var_name으로 위치를 변경한 열의 데이터를 저장한 열의 이름 지정
# ------------------------------------------ # 다음 예제를 봅시다.
import pandas as pd
bilboard=pd.read_csv('bilboard.csv')
bilboard_long=pd.melt(bilboard, id_vars=['year','artist','track','time','date.entered'], var_name='wek', value_name='rating')
# 이렇게 melt메서드를 사용하여 자료를 세로로 관리하게 되면 장점들이 있습니다. # 1. 보기에 편함
# 2. 연산을 수행하기가 편함. 왜냐하면 대부분의 연산을 수행하는 메서드들은 열기준으로 연산
Loser=bilboard_long[bilboard_long.track=='Loser']
Loser_mean=Loser.rating.mean()
# 3. 시각화하기가 편함. 왜냐하면 대부분의 시각화 메서드들은 열기준으로 수행
import matplotlib.pyplot as plt
plt.plot(range(1,77),Loser.rating)

#%% 2. 열 이름 관리하기
# 세상에는 정말 다양한 형태의 데이터가 존재합니다. # 일을 하다 보면 하나의 변수명이 2가지의 의미를 갖는 경우도 있습니다. # 다음 에볼라 자료를 봅시다.
import pandas as pd
ebola=pd.read_csv('country_timeseries.csv')
# ebola 데이터프레임에서 열의 이름을 보면 
# Cases_Guinea: 기니에서 발병한 환자수
# Deaths_Guinea: 기니에서 사망한 환자수
# 하나의 변수가 '발병+지역' 또는 '사망+지역' 이라는 2가지의 의미를 가집니다. # 이렇게 하나의 변수가 2가지의 의미를 가지는 경우 별도의 2개 변수를 생성하여
# 2가지 의미를 하나씩 나누어 가지게 하고 싶은 경우 어떻게 해야할까요?
#%% split메서드로 열 이름 분리하기
ebola_long=pd.melt(ebola, id_vars=['Date','Day'])
# split메서드를 사용하여 열 이름을 분리
variable_split=ebola_long.variable.str.split('_')
# variable_split은 시리즈 자료형이고, 각각의 시리즈에 저장된 값은 리스트입니다. print(type(variable_split)
print(type(variable_split[0]))
# get 메서드를 사용하여 variable_split에 있는 리스트를 한번에 추출
status_values=variable_split.str.get(0)
country_values=variable_split.str.get(1)
# status_value와 country_value를 ebola_long데이터프레임에 추가해 봅시다. ebola_long['status']=status_values
ebola_long['country']=country_values
#%% 3. pivot_table메서드를 사용하여 피벗 테이블 생성하기
# 피벗 테이블: 특정 조건을 기준으로 행과 열로 자료를 정리한 테이블
import pandas as pd
weather=pd.read_csv('weather.csv')
# 날짜별 온도가 옆으로 길게 늘어져 있어 보기 불편하니, melt메서드를 사용하여
# 행과 열을 바꾸어 봅시다. 
weather_melt=pd.melt(weather,id_vars=['id','year','month','element'], var_name='day',value_name='temp')
# weather_melt 데이터프레임에는 element가 tmax와 tmin이 함께 있어 temp를 본 후에
# 이 값이 tmax인지 tmin인지 확인해야하는 번거로움이 존재
# 따라서 tmax와 tmin의 온도를 따로 가지고 있는 2개의 별도 변수를 생성하고 싶습니다. 
weather_tidy=weather_melt.pivot_table(
index=['id','year','month','day'], # 마치 melt메서드의 id_vars와 동일한 역할
columns='element', # 피벗할 열 이름 지정
values='temp', # 데이터로 들어갈 열 이름 지정
dropna=False # 누락값 처리
)
# index를 reset
weather_tidy_flat=weather_tidy.reset_index()
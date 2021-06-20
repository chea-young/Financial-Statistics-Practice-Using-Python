#%% 1. 일반적인 데이터의 특성
# 실제 데이터 분석 작업을 하기 위해서는 row data로 부터 분석하기에 알맞은 데이터로 정제하는 작업이 필요합니다.
# 이러한 데이터 정제 작업은 다음의 기본 원칙에 다라 수행합니다.
# 1. 기조의 데이터로 부터 데이터 분석의 목적에 맞게 여러가지 데이터를 뽑고, 붙이고 하여 새로운 데이터로 생성
# 2. 측정한 값은 row로 구성
# 3. 변수는 열로 구성

# %%  2. 데이터 연결 기초

# %% 2-1.  concat메서드로 데이터 연결하기
# 서로 다른 데이터를 연결하려면 concat메서드를 사용
import pandas as pd

df1 = pd.read.csv()
df2 = pd.read.csv()
df3 = pd.read.csv()

# 데이터프레임을 리스트에 담아 concat 메서드에 전달하여 새로운 데이터프레임 생성
row_concat=pd.cocnat([df1, df2, df3])

# concat메서드는 데이터프레임을 연결할 때 같은 변수에 대해 위해서 아리 방향으로 연결
# 즉, default는 열 기준으로 데이터를 붙이게 됨.

#이번에는 데이터프레임에 시리즈를 연결해 봅시다.
new_row_series = pd.Series(['n1', 'n2', 'n3', 'n4'])

# new_row_series를 알아서 index와 column을 확인해 보세요.
df4 = pd.concat([df1, new_row_series])

#df1 데이터프레임에는 new_row_series에 있는 column인 '0'이 없고
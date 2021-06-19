#1. 국내 주식 삼성전자, 셀트리온, 현대자동차의 2018년 1월 1일부터(휴일인 경우 2018년 첫 거래일부터)
#최근까지의 주가자료를 다운로드 받고, 우리나라 양식의 candlestick 그래프 를 그리시오.

# 범례조절하기
# X축 lable 크기 조절 잘 하기
# 영어도 한글로 표시하기
#%% 수업 내용을 바탕으로 가시성이 있고 정보전달력이 있게 그리기
import pandas as pd
import numpy as np
# 1. set data
s =pd.read_csv('삼성.csv')
c =pd.read_csv('셀트리온.csv')
h =pd.read_csv('현대자동차.csv')

# %%
#2. high와 low 평균 구해서 s_data에 넣기
s_data = s[['date', 'volume']]
s_data['price']=(pd.to_numeric(s['high'])+pd.to_numeric(s['low']))//2

# %%
#3. volume data 정리 -: 0 M: 제거, K: *100
s_volume = s_data['volume'].tolist()
for i in range(len(s_volume)):
    try:
        if(type(s_volume[i]) == float or type(s_volume[i]) == int):
            continue
        elif(s_volume[i] == '-'):
            s_volume[i] = '0'
        elif("M" in s_volume[i]):
            s_volume[i] = s_volume[i][:-1]
        elif("K" in s_volume[i]):
            s_volume[i] = float(s_volume[i][:-1]) *100
    except Exception as e:
        print(str(e))
        print(s_volume[i])
s_data['volume'] = pd.DataFrame(s_volume)

# %%

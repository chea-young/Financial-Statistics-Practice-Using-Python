""""""""""""""""""""""""""" 파이썬 기초 """"""""""""""""""""""""""""""""""""""" 
#%% 참고 교재: 데이터 분석을 위한 판다스 입문 p.240 ~ p.250
# 시계열 데이터는 금융 데이터 분석 분야에서 가장 중요하게 다루는 데이터 형테입니다. 
# 시계열 데이터는 어떤 변수에 대해서 일정 시간 간격으로 자료의 값을 기록한 데이터 입니다. 
# 금융 분야에서는 시계열 데이터를 반드시 자유롭게 다룰수 있어야 합니다.

#%% 1. datetime 오브젝트
# datetime 라이브러리는 날짜와 시간을 처리하는 등의 다양한 시계열 데이터에 적용되는 기능을 제공
# datetime 오브젝트 사용하기 위해서는 datetime 라이브러리를 불러옵니다. from datetime import datetime
# 현재시간 출력
now1=datetime.now() # 자료형이 datetime
now2=datetime.today()

# datetime 오브젝트를 생성할 때 시간을 직접 입력하여 인자로 전달
t1=datetime.now()
t2=datetime(1970, 1, 1)
t3=datetime(1970, 12, 12, 13, 24, 34)

# datetime 오브젝트를 사용하면 시간 차이를 쉽게 계산 가능
diff1=t1-t2
diff2=t2-t1

#%% 여러 가지 데이터를 다루다 보면 시간 변수가 문자열로 저장되어 있는 경우가 많음
# 이런 경우는 문자열을 datetime 오브젝트로 변경해주어야 하는데
# 이 때 사용하는 것이 to_datetime메서드 
import pandas as pd
ebola=pd.read_csv('country_timeseries.csv')
print(ebola.info())
# ebola 데이터프레임을 보면 Date가 문자열로 저장되어 있음을 확인할 수 있습니다. # to_datetime메서드를 사용하여 Date 열의 자료형을 datetime오브젝트로 변환해 봅시다.ebola['date_dt']=pd.to_datetime(ebola['Date'])
print(ebola.info())

#%% to_datetime메서드에서 시간 형식 지정자 (%d, %m, %y)와 기호 (/, -)를 사용하여 
# format인자에 전달하면 그 형식에 맞게 datetime오브젝트 생성 가능
test_df1=pd.DataFrame({'order_day': ['01/01/15','02/01/15','03/01/15']})
test_df1['date_dt1']=pd.to_datetime(test_df1['order_day'], format='%d/%m/%y')
test_df1['date_dt2']=pd.to_datetime(test_df1['order_day'], format='%m/%d/%y')
test_df1['date_dt3']=pd.to_datetime(test_df1['order_day'], format='%y/%m/%d')
test_df2=pd.DataFrame({'order_day': ['01-01-15','02-01-15','03-01-15']})
test_df2['date_dt']=pd.to_datetime(test_df2['order_day'], format='%y-%m-%d')

#%% 다양한 시간형식 지정자
#-----------------------------------------------------------------------------
# 시간 형식 지정자 의미 결과
#-----------------------------------------------------------------------------
# %a 요일 출력 Sun, Mon,...,Sat
# %A 요일 출력(긴 이름) Sunday, Monday, …, Saturday
# %w 요일 출력(숫자, 0부터 일요일) 0, 1, …, 6
# %d 날짜 출력(2자리로 표시) 01, 02, …, 31
# %b 월 출력 Jan, Feb,..., Dec
# %B 월 출력(긴 이름) January, February, …, December
# %m 월 출력(숫자) 01, 02, …, 12
# %y 년 출력(2자리로 표시) 00, 01, …, 99
# %Y 년 출력(4자리로 표시) 0001, 0002, …, 2013, 2014, …, 9999
# %H 시간 출력(24시간) 00, 01,...,23
# %I 시간 출력(12시간) 01, 02,...,12
# %p AM 또는 PM 출력 AM, PM
# %M 분 출력(2자리로 표시) 100, 01, …, 59
# %S 초 출력(2자리로 표시) 00, 01, …, 59
# %f 마이크로초 출력 000000, 000001,...,999999
# %z UTC 차이 출력(+HHMM이나 -HHMM형태) (None), +0000, -0400, +1030
# %Z 기준 지역 이름 출력 (None), UTC, EST, CST
# %j 올해의 지난 일 수 출력(1일, 2일, …) 001, 002, …, 366
# %U 올해의 지난 주 수 출력(1주, 2주, …) 100, 01, …, 53# %c 날짜와 시간 출력 Tue Aug 16 21:30:00 1988
# %x 날짜 출력 08/16/88 (None);08/16/1988
# %X 시간 출력 21:30:00
# %G 년 출력(ISO 8601 형식) 0001, 0002, …, 2013, 2014, …, 9999
# %u 요일 출력(ISO 8601 형식) 1, 2,..., 7
# %V 올해의 지난 주 수 출력(ISO 8601 형식) 01, 02, …, 53
#----------------------------------------------------------------------------- 
# now메서드로 얻은 현재 시간의 시계열 데이터는 아주 정밀한 단위까지 시간을 표현
# 원하는 시간의 형태로 자르기 위해서 strftime메서드 사용
now=datetime.now()
nowDate=now.strftime('%Y-%m-%d')
nowTime=now.strftime('%H:%M:%S')
nowDatetime=now.strftime('%Y-%m-%d %H:%M:%S')

#%% read_csv메서드에서 parse_dates 인자에 datetime 오브젝트로 변환하고자 하는 열의 이름을 
# 바로 지정하여 저장 가능
ebola1=pd.read_csv('country_timeseries.csv',parse_dates=['Date'])
print(ebola1.info())
# dt접근자 사용하여 datetime오브젝트에서 날짜 정보 추출하기
print(ebola1['Date'][0].year)
print(ebola1['Date'][0].month)
print(ebola1['Date'][0].day)
ebola1['year']=ebola1['Date'].dt.year
ebola1['month']=ebola1['Date'].dt.month
ebola1['day']=ebola1['Date'].dt.day
print(ebola1.info()) # year, month, day는 정수형
# %%

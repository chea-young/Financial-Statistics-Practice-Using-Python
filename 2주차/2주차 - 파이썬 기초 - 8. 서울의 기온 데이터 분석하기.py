""""""""""""""""""""""""""" 파이썬 기초 """""""""""""""""""""""""""""""""""""""
#%% 참고 교재: 모두의 데이터 분석 with 파이썬 p.14 ~ p.52

#%% 1. 서울의 기온 데이터 분석하기

#%% 1-1. CSV파일에서 데이터 읽어오기

import csv                                 # csv 모듈 불러오기
f=open('seoul.csv','r',encoding='cp949')   # open()함수: 일반적인 파일 읽고 쓰기
data=csv.reader(f,delimiter=',')           # csv.reader(): data라는 csv reader객체 생성
print(data)                                # data를 출력
f.close()                                  # open()함수에서 연 파일을 닫음

# open()함수
#  - 일반적인 파일을 읽거나 쓰는 함수
#  - 함수 도움말을 보면 'Open file and return a stream' 
#      ==> 파일을 열고 stream(데이터의 흐름)을 반환
#      ==> 'seoul.csv'는 읽고자 하는 CSV파일
#      ==> 'r'은 'read'이 약자로 읽기만을 위해서 파일을 연다는 의미이며 default값
#      ==> 'cp494'는 Windows 한글 인코딩 방식으로 읽어 오라는 의미이며 default값
#          다른 운영체제는 'utf8'을 사용

# csv.reader()함수
#   - open()함수에서 읽어온 csv파일 데이터를 콤마(,)를 기준으로 분리해서 저장
#   - delimiter=','이 default값

# default값을 생략한 다음 코드는 위의 코드와 동일
import csv                                 # csv 모듈 불러오기
f=open('seoul.csv')   # open()함수: 일반적인 파일 읽고 쓰기
data=csv.reader(f)           # csv.reader(): data라는 csv reader객체 생성
print(data)                                # data를 출력
f.close()                                  # open()함수에서 연 파일을 닫음

# 실행결과를 확인: 아무것도 출력하지 않고 
# '<_csv.reader object at 0x00000205AB1A63C8>' 만 출력
# 위 코드는 CSV파일 데이터를 읽기만 하는 코드이므로, 특별한 실행 결과가 없음
# 단지, 우리가 읽어온 데이터가 csv reader 객체라는 정도만 알 수 있음

# close()함수
#   - 함수도움말: Flush and close the IO object.
#   - 즉 현재 우리가 읽고있는 csv reader 객체를 닫으라는 의미



#%% 1-2. 데이터 출력하기

# 위에서 'print(data)'라고 파일에 저장된 데이터 전체를 출력하고자 했더니, 
# '<_csv.reader object at 0x00000205AB1A63C8>' 만 출력
# 이번에는 CSV파일에 저장된 데이터를 한 줄씩 출력해 봅시다.

import csv
f=open('seoul.csv','r',encoding='cp949')
data=csv.reader(f,delimiter=',')
for row in data:
    print(row)
f.close()

# 출력결과
#  - 각 행의 데이터가 대괄호([])에 둘러싸여 있음 ==> list형태임을 확인할 수 있음
#  - 각 list내에서 데이터가 작은 따옴표('')로 둘러 싸여 있음 ==> 문자열(str) list
#  - 따라서, 나중에 기온이 최대값 또는 최소값을 찾는 등의 크기 비교가 필요한 경우
#    문자열을 실수(float)형태로 변환해야 함
#  - 한 줄씩 출력 ==> 왠만하면 하지 마세요!


#%% Tips: csv reader 객체 변수로 저장하기
# 위의 코드에서 csv reader객체는 'Variable explorer'에 저장이 안 됨.
# 만약 csv reader객체를 Variable explorer'에 저장하기 위한 가장 쉬운 방법은 
# PANDAS라는 모듈을 사용하는 방법
# 하지만, 우리는 아직 PANDAS를 배우지 않았으므로 다음과 같은 방법을 사용할 수 있음

import csv
f=open('seoul.csv','r',encoding='cp949')
data=csv.reader(f,delimiter=',')
seoul=[]                                   # 공갈 list 생성
for row in data:
    seoul.append(row)                      # list에 추가
f.close()


#%% 1-3. 헤더 저장하기

import csv
f=open('seoul.csv','r',encoding='cp949')
data=csv.reader(f,delimiter=',')
header=next(data)                       # header라는 변수에 헤데 데이터 행을 저장
print(header)                           # header변수 출
f.close()

# next()함수
#  - 첫 번째 데이터 행을 읽어오고 데이터의 탐색 시작 위치를 다음 행으로 이동키는 명령
# 실행결과: header라는 변수에 헤더를 저장

#%%
# 위의 코드에 for문을 추가하여 몇번째 줄부터 출력하는지 확인해봅시다.
import csv
f=open('seoul.csv','r',encoding='cp949')
data=csv.reader(f,delimiter=',')
header=next(data)                      
for row in data:
        print(row)
f.close()

#%%
# 헤더가 출력되지 않고 두 번째 행부터 출력

# 만약 첫 다섯행만 출력하고 싶다면 다음과 같이 할 수 있음
# - 행의 수를 직접 카운트해서 출력
import csv
f=open('seoul.csv','r',encoding='cp949')
data=csv.reader(f,delimiter=',')
header=next(data)
count_row=1;                     
for row in data:
    if count_row<=5:
        print(row)
        count_row+=1;   # count_row=count_row+1
f.close()

# PANDAS 모듈을 사용하면 head()라는 함수를 사용할 수 있으나, 아직 안 배웠으니 
# 나중에 설명하도록 함.


#%% 1-3. 서울의 최고기온이 가장 높았던 날은 언제인가?

# 위의 코드에서 data는 csv reader객체이면서 문자열의 list 데이터 형태를 가짐
# 최고기온을 찾기 위해서는 최고기온값이 문자열이 아닌 실수로 저장
# 따라서 다음과 같이 최고기온값을 실수로 변경해서 저장
import csv
f=open('seoul.csv','r',encoding='cp949')
data=csv.reader(f,delimiter=',')
header=next(data)                      
for row in data:
    row[-1]=float(row[-1])
    print(row)
f.close()

# 에러발생
#   - ValueError: could not convert string to float: 
#   - 값계산에러: 문자열을 실수로 변경할 수 없었습니다.
#   - Console창을 보니 '1950-08-31'까지 실행이 되고 그 다음행에서 에러 발생
#   - seoul.csv파일을 열어서 에러 발생 원인 확인
#   - 값이 없는 경우에 빈 문자열(midding value)이라는 것을 실수로 표현하기 위해
#   - '-999'를 입력
#%%
import csv
f=open('seoul.csv','r',encoding='cp949')
data=csv.reader(f,delimiter=',')
header=next(data)                      
for row in data:
    if row[-1]=='':
        row[-1]=-999
    else:
        row[-1]=float(row[-1])
    print(row)
f.close()

# 실행결과를 확인해 보세요.

# 이제 최고기온을 따로 저장하기 위해서 최고기온을 저장할 변수를 만들어 봅시다.
import csv
f=open('seoul.csv','r',encoding='cp949')
data=csv.reader(f,delimiter=',')
header=next(data)  
max_temp=-999                             # 최고기온을 담을 공갈 변수
maxt_date=''                              # 최고기온 발생일을 담을 공갈 변수
for row in data:
    if row[-1]=='':
        row[-1]=-999
    else:
        row[-1]=float(row[-1])
    
    if max_temp<row[-1]:
        max_temp=row[-1]
        max_date=row[0]
f.close()
print('기상 관측 이래 서울의 최고 기온이 가장 높았던 날은',max_date+'로',str(max_temp)+'도 였습니다.')

#%%[과제8-1] 서울 기온 데이터에서 기상 관측 이래 일교차가 가장 컸던 날은 언제인지 
#            찾고, 다음과 같이 출력하시오.
#            출력: '기상 관측 이래 서울의 일교차가 가장 컸던 날은 yyyy-mm-dd로 일교차는 xx였습니다.'

import csv
f=open('seoul.csv','r',encoding='cp949')
data=csv.reader(f,delimiter=',')
header=next(data)  
max_daily_temp=-999                             # 최고기온을 담을 공갈 변수
maxt_date=''  
for row in data:
    # 최고 기온 바꾸기
    if row[-1]=='':
        row[-1]=-999
    else:
        row[-1]=float(row[-1])
    # 최저 기온 바꾸기
    if row[-2]=='':
        row[-2]=-999
    else:
        row[-2]=float(row[-2])
    daily_temper = row[-1] - row[-2]
    #일교차 큰 값 찾기 위해 비교하기
    if max_daily_temp<daily_temper:
        max_daily_temp=daily_temper
        max_date=row[0]
f.close()
print('기상 관측 이래 서울의 일교차가 가장 컸던 날은',max_date+'로',str(max_daily_temp)+'도 였습니다.')
# %%

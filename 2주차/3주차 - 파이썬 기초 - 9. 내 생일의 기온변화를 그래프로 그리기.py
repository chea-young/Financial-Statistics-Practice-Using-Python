""""""""""""""""""""""""""" 파이썬 기초 """""""""""""""""""""""""""""""""""""""
#%% 참고 교재: 모두의 데이터 분석 with 파이썬 p.54 ~ p.94

#%% 새로운 프로그래밍 언어를 배우는 것은 새로운 언어를 배우는 것과 동일
#   문법 위주로 먼저 배우고 활용을 하면 지루한 일
#   이 수업에서는 문법을 먼저 배우기 보다는 사례 위주로 먼저 학습한 후
#   마지막에 최종적으로 전체 문법을 배우는 방법을 채택


#%% 1. 데이터에 질문하기

# 여러분의 생일날의 최고 기온을 그래프로 그려 봅시다.

#%% 1-1. 데이터 읽어오기
import csv
f=open('seoul.csv')
data=csv.reader(f)

for row in data:
    print(row)
    
#%% 이제 next()함수를 사용해서 헤더 부분을 제외시킨 후 최고 기온 데이터만 출력
import csv
f=open('seoul.csv')
data=csv.reader(f)
next(data)

for row in data:
    print(row[-1])
    

#%% 데이터 리스트에 저장하기
import csv
f=open('seoul.csv')
data=csv.reader(f)
next(data)
result=[]                               # 최고 기온 데이터를 저장할 리스트 생성

for row in data:
    if row[-1]!='':                     # 최고 기온 데이터 값이 존재한다면
        result.append(float(row[-1]))   # result리스트에 최고 기온 값 추가
print(result)
print(len(result))                      # 데이터가 몇 개인지 출력

# Variable explorer에서 result 변수의 형태와 자료의 갯수를 확인해 보세요.

                                        
#%% 2. 데이터 시각화하기
# 최고 기온 데이터를 꺽은선 그래포로 표현해 봅시다.
import csv
import matplotlib.pyplot as plt

f=open('seoul.csv')
data=csv.reader(f)
next(data)
result=[]                               # 최고 기온 데이터를 저장할 리스크 생성

for row in data:
    if row[-1]!='':                     # 최고 기온 데이터 값이 존재한다면
        result.append(float(row[-1]))   # result리스트에 최고 기온 값 추가


plt.figure(figsize=(8,2))              # 그래프 크기 가로 8인치, 세로 2인
plt.plot(result,'r')                    # result리스크에 저장된 값을 빨간색 그래프로 그리기
plt.show()


#%% 3. 날짜 데이터 추출하기
# split()함수는 사용자가 설정하는 특정 문자를 기준으로 문자열을 분리
# 다음 예제를 봅시다.
s='hello python'
print(s.split())                        # 지정하지 않으면 공백문자를 기준으로 문자열 분리
print(s.split('o'))                     # 'o'를 기준으로 문자열 분리
print(s.split('e'))

date='1907-10-01'
print(date.split('-'))                  # '-'를 기준으로 분리

# 다음 결과를 예측해 봅시다.
print(date.split('-')[0])
print(date.split('-')[1])
print(date.split('-')[2])


# 이제 split()함수를 사용해서 1년 중 3월의 최고 기온 데이터만 추출해서
# 그래프로 그려봅시다.
import csv
import matplotlib.pyplot as plt

f=open('seoul.csv')
data=csv.reader(f)
next(data)
result=[]                                   # 최고 기온 데이터를 저장할 리스크 생성

for row in data:
    if row[-1]!='':                         # 최고 기온 값이 공백이 아니라면
        if row[0].split('-')[1]=='03':      # 3월에 해당되는 값이 8월이면
            result.append(float(row[-1]))   # result리스트에 일별 최고기온을 추가

plt.plot(result,'r.-')                      # '색마선'
plt.show()


# 이제 바로 위의 코드를 확장하여 3월 1일의 최고 기온 데이터만 추출하여 그래프로 그려보자.
import csv
import matplotlib.pyplot as plt

f=open('seoul.csv')
data=csv.reader(f)
next(data)
result=[]                                  

for row in data:
    if row[-1]!='':                         
        if row[0].split('-')[1]=='03' and row[0].split('-')[2]=='01':
            result.append(float(row[-1]))   

plt.plot(result,'r.-')                      
plt.show()


# 이제 하나의 그래프에 1983이후의 자료만으로 최저 기온과 최고 기온을 동시에 그려 봅시다.
import csv
import matplotlib.pyplot as plt

f=open('seoul.csv')
data=csv.reader(f)
next(data)
high=[]                                  
low=[]

for row in data:
    if row[-1]!='' and row[-2]!='':          # 최저 기온과 최고 기온 모두 존재한다면                         
        if int(row[0].split('-')[0])>=1983:  # 1983년 이후 이면
            if row[0].split('-')[1]=='03' and row[0].split('-')[2]=='01':
                high.append(float(row[-1]))
                low.append(float(row[-2]))

plt.plot(high,'r.-')
plt.plot(low,'b.-')                      
plt.show()


# 그래프 꾸미기
plt.plot(high,'r.-', label='최고 기온')
plt.plot(low,'b.-', label='최저 기온')                      

plt.rc('font',family='Malgun Gothic')     # 그래프 제목을 한글로 쓸 경우 깨지는 것을 방지하기 위해
plt.rcParams['axes.unicode_minus']=False  # 세로축의 음수 기호(-)가 깨지는 것을 방지
plt.title('삼일절 기온 변화 그래프')
plt.legend()

plt.show()


#%% [과제9-1] 일교차를 계산하여 저장할 리스트를 생성하고 1983년 이후 8월 15일의 일교차를
#             그래프로 그리시오.
import csv
import matplotlib.pyplot as plt

f=open('seoul.csv')
data=csv.reader(f)
next(data)

daily_temp = [] #일교차를 담을 리스트
for row in data:
    if row[-1]!='' and row[-2]!='':                                
        if int(row[0].split('-')[0])>=1983:  
            if row[0].split('-')[1]=='08' and row[0].split('-')[2]=='15':
                daily_temp.append(float(row[-1]) - float(row[-2]))

plt.plot(daily_temp,'b.-', label='8월 15일 일교차')
                   
plt.rc('font',family='Malgun Gothic')     # 그래프 제목을 한글로 쓸 경우 깨지는 것을 방지하기 위해
plt.rcParams['axes.unicode_minus']=False  # 세로축의 음수 기호(-)가 깨지는 것을 방지

plt.legend()
plt.show()    
f.close()






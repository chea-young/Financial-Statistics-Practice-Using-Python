#%% 참고 교재: 모두의 데이터 분석 with 파이썬 p.109 ~ p.123 
#%% 지난 시간 인구 그래프를 좀더 꾸며 봅시다 
import csv 
f=open('age.csv') 
data=csv.reader(f) 
result=[] 
name=input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요: ') 

for row in data: 
    if name in row[0]: 
        for i in row[3:]: 
            result.append(int(i))

import matplotlib.pyplot as plt 
plt.style.use('ggplot') 
plt.rc('font',family='Malgun Gothic') 
plt.title(name+' 지역의 인구 구조') 
plt.plot(result) 
plt.show() 

#%% 1. 막대그래프 그리기 
# bar()함수: 막대그래프를 그리는 명령어 
import matplotlib.pyplot as plt 
plt.bar([0,1,2,3,6,10],[1,2,3,5,6,7]) # bar(막대를 표시할 위치, 막대의 높이) 
plt.show()


#%% 1-1. 특정 지역의 인구 구조 막대그래프 그리기 
import csv 
f=open('age.csv') 
data=csv.reader(f) 
result=[] 
name=input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요: ') 

for row in data: 
    if name in row[0]: 
        for i in row[3:]: 
            result.append(int(i.replace(',','')))
import matplotlib.pyplot as plt 

plt.bar(range(101), result) # bar(막대를 표시할 위치, 막대의 높이) 
plt.show() 
# 수평막대그래프 그리기 

#%% [과제12-1] 인터넷에서 'matplotlib bar'를 검색해서 막대그래프의 색을 변경하는 
# 방법을 검색하고 원하는 색으로 변경하는 코드를 작성해서 제출하세요. 
import matplotlib.pyplot as plt 

colors=input("""생성되기를 원하는 막대그래프이 색을 입력해주세요: 
                가능한 색은 [빨강, 주황, 노랑, 초록, 검정, 분홍, 보라]""")
color_list = {'빨강':'red', '주황': 'orange', '노랑': 'gold', '초록':'forestgreen', '검정':'black', '분홍': 'hotpink', '보라':'purple'}

plt.bar([0,1,2,3,6,10],[1,2,3,5,6,7], color=color_list[colors]) # bar(막대를 표시할 위치, 막대의 높이) 
plt.show()


#%% 1-2. 항아리 모양 그래프 그리기 
# 인구 구조의 시각화에서 주로 사용되는 항아리 모양 그래프를 그려 봅시다. 
# 남여 인구데이터를 www.mois.go.kr --> 정책자료 --> 통계 --> 주민등록 인구 통계 
# 다운로드 하세요.

import csv 
f=open('gender.csv') 
data=csv.reader(f) 
m=[] 
f=[] 

for row in data: 
    if '모현읍' in row[0]: 
        for i in range(0,101): 
            m.append(row[i+3]) 
            f.append(row[-(i+1)]) 
f.reverse()

# 또는
import csv 
f=open('gender.csv') 
data=csv.reader(f) 
m=[] 
f=[]

for row in data: 
    if '모현읍' in row[0]: 
        for i in row[3:104]: # row[3]: 남0세, row[103]: 남100세이상 
            m.append(int(i)) 
        for i in row[106:]: 
            f.append(int(i)) 

# 가로 막대 그래프 그리기 
import matplotlib.pyplot as plt 
plt.barh(range(101),m) 
plt.barh(range(101),f) 
plt.show() 

#%% 겹쳐 보이는 부분때문에 알아보기 어려우니 항아리 모양 그래프로 변경 
import csv 
f=open('gender.csv') 
data=csv.reader(f) 
m=[] 
f=[]

for row in data: 
    if '모현읍' in row[0]: 
        for i in row[3:104]: 
            m.append(int(i)) 
        for i in row[106:]: 
            f.append(-int(i)) # 남자 데이터를 음수로 변경 

import matplotlib.pyplot as plt 
plt.rc('font',family='Malgun Gothic') 
plt.title('모현읍 지역의 남녀 성별 인구 분포') 
plt.barh(range(101),m, label='남성') 
plt.barh(range(101),f, label='여성') 
plt.legend() 
plt.show() 

#%% 남자쪽 그래프에서 x축이 음수가 깨지는 것 수정 
import csv 
f=open('gender.csv') 
data=csv.reader(f) 
m=[] 
f=[] 

for row in data: 
    if '모현읍' in row[0]: 
        for i in row[3:104]: 
            m.append(int(i)) 
        for i in row[106:]: 
            f.append(-int(i)) # 남자 데이터를 음수로 변경

import matplotlib.pyplot as plt 
plt.rc('font',family='Malgun Gothic') 
plt.rcParams['axes.unicode_minus']=False 
plt.title('모현읍 지역의 남녀 성별 인구 분포') 
plt.barh(range(101),m, label='남성') 
plt.barh(range(101),f, label='여성') 
plt.legend() 
plt.show() 


#%% 남자쪽 그래프에서 x축이 음수로 보이는 것을 양수로 변경 
import csv 
f=open('gender.csv') 
data=csv.reader(f) 
m=[] 
f=[]

for row in data: 
    if '모현읍' in row[0]: 
        for i in row[3:104]: 
            m.append(int(i)) 
        for i in row[106:]: 
            f.append(-int(i))

import matplotlib.pyplot as plt 
plt.rc('font',family='Malgun Gothic') 
plt.rcParams['axes.unicode_minus']=False 
plt.title('모현읍 지역의 남녀 성별 인구 분포') 
plt.barh(range(101),m, label='남성') 
plt.barh(range(101),f, label='여성') 
plt.xticks([-300,-200,-100,0,100,200,300],[300,200,100,0,100,200,300]) 
plt.legend() 
plt.show() 

#%% [과제12-2] [과제12-2]결과와 동일한 결과를 생성하는 코드를 작성하세요. 
import csv 
f=open('gender.csv') 
data=csv.reader(f) 

first_name=input("인구 구조를 비교하고 싶은 첫번째 지역의 이름(읍면동 단위)을 입력해주세요: ")
first_gender = input("인구 구조를 비교하고 싶은 첫번째 지역의 성별을 입력하세요(예: 남 또는 예 여): ")

second_name=input("인구 구조를 비교하고 싶은 두번째 지역의 이름(읍면동 단위)을 입력해주세요: ")
second_gender = input("인구 구조를 비교하고 싶은 두번째 지역의 성별을 입력하세요(예: 남 또는 예 여): ")

first = []
second = []
first_compare = 0
second_compare = 0
if(first_gender == '여'):
    first_compare = (3, 104)
    first_gender = ' 여자'
else:
    first_compare = (106,-1)
    first_gender = ' 남자'

if(second_gender == '여'):
    second_compare = (3, 104)
    second_gender = ' 여자'
else:
    second_compare = (106,-1)
    second_gender = ' 남자'

for row in data: 
    if first_name in row[0]: 
        for i in row[first_compare[0]:first_compare[1]]: 
            first.append(-int(i)) 
    if second_name in row[0]:
        for i in row[second_compare[0]:second_compare[1]]: 
            second.append(int(i))

import matplotlib.pyplot as plt 
plt.rc('font',family='Malgun Gothic') 
plt.rcParams['axes.unicode_minus']=False 
plt.title('모현읍 지역의 남녀 성별 인구 분포') 
plt.barh(range(101),first, label=first_name+first_gender) 
plt.barh(range(101),second, label=second_name+second_gender) 
plt.xticks([-300,-200,-100,0,100,200,300],[300,200,100,0,100,200,300]) 
plt.legend() 
plt.show() 


# %%

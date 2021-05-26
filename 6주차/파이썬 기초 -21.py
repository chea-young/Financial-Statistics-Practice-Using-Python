#%% 참고 교재: 데이터 분석을 위한 판다스 입문 p.54 ~ p.68

# 데이터프레임은 리스트나 딕셔너리보다 데이터를 다루는데 더 특화되어 있음
# 판다스의 데이터프레임과 시리즈는 많은 양의 데이터를 저장할 수 있으며
# 행과 열을 단위로 데이터를 조작할 수 있는 다양한 속성과 메서드를 제공
#%% 1. 시리즈와 데이터프레임 직접 만들기

#%% 1-1. 시리즈 만들기
import pandas as pd

# 판다스의 Series메서드에 리스트를 전달하여 시리즈 생성
s0=pd.Series(['banana','42']) 
print(s0)

# index를 지정하지 않으니 0으로 지정
s1=pd.Series(['Wes McKnney','Creator of Pandas'])
print(s1)

# 문자열을 인덱스로 지정
s2=pd.Series(['Wes McKnney','Creator of Pandas'], index=['Person','Who'])
print(s2)
#%% 1-2. 데이터프레임 만들기
scientists1=pd.DataFrame({
    'Name':['Rosaline Franklin','Wiliam Goset'],
    'Ocupation':['Chemist','Statistician'],
    'Born':['1920-07-25','1876-06-13'],
    'Died':['1958-04-16','1937-10-16'],
    'Age':[37,61]})
# 딕셔너리는 Key와 Value의 형태로 저장된 데이터
print(scientists1)

# 데이터프레임도 index를 따로 지정하지 않으면 0부터 자동으로 생성하여 부여
# index를 따로 지정하려면 index인자에 리스트를 전달하면 가능
# column인자를 사용하면 데이터프레임의 열 순서를 지정 가능
scientists2=pd.DataFrame(
    data={'Ocupation':['Chemist','Statistician'],
    'Born':['1920-07-25','1876-06-13'],
    'Died':['1958-04-16','1937-10-16'],
    'Age':[37,61]},
    index=['Rosaline Franklin','Wiliam Goset'],
    columns=['Ocupation','Born','Age','Died']
)
print(scientists2)

#%% 1-2. 시리즈 다루기 - 기초
#%% loc속성을 사용하여 데이터프레임에서 시리즈 선택하기
first_row=scientists2.loc['Wiliam Goset'] # key값이 index
print(type(first_row))
print(first_row)
# 앞서 실습한 loc, iloc과 같은 속성 이외에도 시리즈에는 다양한 속성이 미리 정의

#%% index, values 속성과 keys 메서드 사용하기
#%% index 속성
print(first_row.index) # 시리즈의 index가 저장; 데이터프레임도 동일하게 사용가능

#%% values 속성
print(first_row.values) # 시리즈의 data가 저장; 데이터프레임도 동일하게 사용가능

#%% keys메서드 
print(first_row.keys()) # index속성과 같은 역할이지만 메서드

#%% index속성과 keys메서드 응용
print(first_row.index[0])
print(first_row.keys()[0])

# 위의 두 코드는 동일한 결과: 속성과 메서드의 차이를 느껴보세요.

#%% 시리즈의 기초 통계 메서드
ages=scientists2['Age']
print(ages)

mean_ages=ages.mean() # 평균
min_ages=ages.min() # 최소값
max_ages=ages.max() # 최대값
std_ages=ages.std() # 표준편차
print(mean_ages, min_ages, max_ages, std_ages)

#%% 시리즈 메서드 정리
#-----------------------------
# 시리즈 메서드 \ 설명
#-----------------------------

# append \ 2개 이상의 시리즈 연결
# describe \ 요약 통계량 계산
# drop_duplicates \ 중복값이 없는 시리즈 반환
# equals \ 시리즈에 해당 값을 가진 요소가 있는지 확인
# get_values \ 시리즈 값 구하기 (values 속성과 동일)
# isin \ 시리즈에 포함된 값이 있는지 확인
# replace \ 특정값을 가진 시리즈 값을 교체
# sample \ 시르즈에서 임의의 값 반환
# sort_values \ 값을 정렬
# to_frame \ 시리즈를 데이터프레임으로 변환
#-----------------------------

print (ages.describe()[0])
#%% 1-3. 시리즈 다루기 - 응용
#%% mask를 사용한 불린 추출
import pandas as pd
scientists=pd.read_csv('scientists.csv')

ages=scientists['Age']
print(ages>ages.mean())
old_ages=scientists[ages>ages.mean()]
print(old_ages)

#%% 시리즈와 브로드캐스팅
#%% 벡터에 대한 Broadcasting: 동일한 위치에 있는 값끼리 연산을 수행한 후 결과 생성
print(ages+ages) 
print(ages*ages)
print(ages+10)
print(ages*2)
print(ages+pd.Series([1,10]))

temp = pd.Series([1,100])
print(ages+temp) # NOTE  index가 같은 것끼리 더한다
#%%
rev_ages=ages.sort_index(ascending=False) # NOTE 내림차순으로 변한다.
print(ages+rev_ages)

ages_sorted_by_value=ages.sort_values(ascending=False) # NOTE index가 같은 것끼리 더한다.
print(ages+ages_sorted_by_value)

ages_sorted_by_value2=ages.sort_values(ascending=False).reset_index() # NOTE index가 같은 것끼리 더하기 위해 index를 리셋한 이후에 더한다.
print(ages+ages_sorted_by_value2['Age'])
# %%

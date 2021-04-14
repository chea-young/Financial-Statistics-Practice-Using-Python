#%% 참고 교재: 데이터 분석을 위한 판다스 입문 p.36 ~ p.47
#%% 데이터 추출하기
# 데이터프레임에서 데이터를 열단위 또는 행단위로 추출하는 방법에 대해 학습
#%% 열 단위 데이터 추출하기
import pandas as pd
df=pd.read_csv('gapminder.tsv', sep='\t')
country_df=df['country'] # 열이름이 country인 열을 추출하여 country_Df에 저장
print(type(country_df)) # 1차원 배열 형태인 시리즈(Series)로 저장된 것 확인
print(country_df.head())
print(country_df.tail()) # 마지막 5개의 행을 출력
# 한 번에 여러개의 열을 추출
subset=df['country','continent','year'] #counrty, continent, year 열만 추출하여 
#subset에 새로 저정
print(type(subset)) # 2개 이상의 열을 추출했으므로 DataFrame으로 저장
print(subset.head())
print(subset.tail())
#%% 행 단위 데이터 추출하기
# 행 단위 데이터 추출하는 속성
# -------------------- # 속성 \ 설명
# -------------------- # loc \ 인덱스를 기준으로 행 데이터 추출
# iloc \ 행 번호를 기준으로 행 데이터 추출
# -------------------- # 우리는 이미 리스트(List)를 학습하면서 index를 알고 있음
# 하지만 판다스에서는 우리가 앞서 배웠던 index를 행번호라고 부르고
# 인덱스는 조금 다른 의미로 사용
# 다음에서 판다스의 행번호와 인덱스의 개념을 알아 봅시다. # 인덱스와 행번호 개념
# Variable explorer를 열어 보면 맨 왼쪽에 index가 있음. # 이러한 데이터프레임의 index는 숫자뿐만 아니라 문자열로도 지정하여 사용가능
# 반면, 행 번호는 데이터의 순서에 따라서 생성되는 정수 (이게 리스트에서 말하는 index)
print(df.loc[0])
afghan_1952=df.loc[0]
print(df.loc[9])
Bangladesh_1967=df.loc[9]
print(df.loc[-1]) # 에러 발생!: 왜냐하면 loc속성은 인덱스를 기준으로 행 데이터 추출
print(df.iloc[-1]) # iloc은 행 번호를 기준으로 행 데이터를 추출하므로 -1을 사용하면 
 # 리스트와 마찬가지로 맨 마지막 데이터를 추출 가능
Zimbabwe_207=df.iloc[-1] 
# 그럼 데이터프레임의 index를 사용하는 loc속성으로는 어떻게 마지막 데이터를 추출할까?
print(df.shape) # shape속성으로 부터 행과 열의 갯수를 확인
print(df.loc[df.shape[0]-1])
print(df.tail(n=1)) # tail함수를 사용하여 추출 가능
print(df.tail(n=2)) # 맨 끝에서 2개 데이터 추출 가능
# 참고: loc속성과 tail함수로 추출한 데이터의 자료형은 다르다. # 다음 코드를 실행하고 Variable explorer로 가서 Type을 확인해 보세요. Zimbabwe_207_loc=df.loc[df.shape[0]-1]
Zimbabwe_207_tail=df.tail(n=1)
# 만약 인덱스가 0, 9, 99인 데이터를 한 번에 추출하려면?
print(df.loc[0,9,99])
# 정리하자면, 데이터프레임에서 사용자가 특별히 index를 지정해주지 않으면
# 판다스는 행 번호를 index로 사용하게 됨. # 따라서 이 경우는 index와 행번호가 일치하게 됨
# 하지만, loc속성은 index조회시 사용하고
# iloc속성은 행 번호로 조회시 사용
#%% loc, iloc속성을 이용하여 자유자재로 데이터 만들기
# 리스트에서 배웠던 슬라이싱과 인데싱을 데이터프레임에서도 loc, iloc속성을 사용하여 
# 자유자재로 데이터를 추출하고 저장할 수 있음
# 슬라이싱
subset_loc=df.loc[:,['year','pop']] # loc속성에서 행추출은 index로 열 추출은 열이름으로 추출
subset_iloc=df.iloc[:,[2,4,-1]] # # iloc속성에서 행추출은 행과 열의 순서번호를 사용하여 추출
# 다시 한번 정리합시다. 다음 코드는 실행가능할까요?
subset_loc=df.loc[:,[2,4,-1]]
# 이외에도 앞서 배웠던 여러가지 방법으로도 행과 열을 추출하고 저장할 수 있음
subset_iloc_range=df.iloc[:,range(5)] # df 데이터프레임에서 행은 모든 행을 추출하고 
 # 열은 [0,1,2,3,4] 추출하여 저장
subset_iloc_range=df.iloc[:,:5] # 위와 동일한 코드
subset_iloc_range=df.iloc[:, 0:6:2] # 행은 모든행, 열은 [0,2,4] 선택 저장
subset_iloc_range=df.iloc[0,9,9],[0,3,5] # 행은 [0,9,9] 선택, 열은 [0,2,4]선택 저장
#%% [과제 19-1] subset_iloc_range=df.iloc[0,9,9],[0,3,5]동일한 결과를 주는 코드를 
# loc속성을 이용하여 작성하시오.
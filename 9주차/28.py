""""""""""""""""""""""""""" 파이썬 기초 """"""""""""""""""""""""""""""""""""""" #%% 참고 교재: 데이터 분석을 위한 판다스 입문 p.174 ~ p.183
#%% 1. 자료형 다루기
# 자료형은 연산을 사용하는 경우 원하는 결과를 얻기 위해 중요
# 따라서, 적절한 연산의 결과를 얻기위해서 자료형을 우리가 원하는 형태로 변형하는 것이 필요
# 다음 예제를 봅시다.
import pandas as pd
import seaborn as sns

# seborn에 있는 tips라는 데이터프레임을 불러오고 열의 자료형을 확인
tips=sns.load_dataset("tips") # NOTE 식당에서 팁을 얼마나 받았냐에 대한 data
print(tips.dtypes) # NOTE 각 data의 type이 출력 (category는 특별히 몇가지의 범주가 정해진 type)

#%% 예를들어 sex라는 열의 자료형은 category로 저장되어 있음
# sex라는 열을 category 자료형으로 하지 않고 문자열로 변경한다고 가정하자. 
# astype메서드를 사용하여 문자열로 변경하여 봅시다. 변경하면 색이 바꾼다.
tips['sex str']=tips['sex'].astype(str) 
print(tips.dtypes) # NOTE 판다스에서는 str은 object로 나타난다.

#%% astype메서드를 사용하여 float64 자료형인 total_bill을 문자열로 변경해 봅시다. 
tips['total_bill']=tips['total_bill'].astype(str)
print(tips.dtypes)

# 이제 total_bill의 자료형을 원위치 시켜봅시다. 
tips['total_bill']=tips['total_bill'].astype(float)
print(tips.dtypes)

#%% 우리가 데이터를 다루다 보면 자료형이 예를들어 숫자와 문자열이 혼합되어 있는 경우가있습니다. 
# 예를 봅시다. 
tips_sub_miss=tips.head(10) # 앞에 10개만 가져온다.
tips_sub_miss.loc[[1,3,5,7],'total_bill']='missing' #loc: indew, column이 total_bill에 missing을 입력
print(tips_sub_miss.dtypes)

#%% 이렇게 자료형이 혼합되어 있는 경우 문자열은 누락값 처리하고, 
# 숫자만 숫자 자료형으로 저장하려면 어떻게 해야 할까요?
# astype()메서드 사용
tips_sub_miss['total_bill']=tips_sub_miss['total_bill'].astype(float) # NOTE missing 때문에 에러가 난다.

#%% to_numeric()메서드 사용
pd.to_numeric(tips_sub_miss['total_bill']) # errors 인자에 'raise'를 설정한 것과 동일한결과
pd.to_numeric(tips_sub_miss['total_bill'], errors='raise') # 숫자로 변환할 수 없는 값이있으면 오류 발생
#%%
pd.to_numeric(tips_sub_miss['total_bill'], errors='ignore') # NOTE 프로그램은 실행하되 아무 작업도 하지 마
#%%
pd.to_numeric(tips_sub_miss['total_bill'], errors='coerce') # 숫자로 변환하되 숫자로 변환할 수 없느 값은 누락값으로 처리

#%% downcast는 숫자의 자료형을 더 작은 형태로 저장하는 경우
pd.to_numeric(tips_sub_miss['total_bill'], errors='coerce', downcast='float')

#%% 2. 카데고리 자료형
# category자료형: 유한 개수의 값만 가질 수 있는 특수한 자료형
# 예: 성별, 요일, 아침, 점심 ,저녁, 흡연여부, 설문조사 선택지, 지역 등
# category자료형의 장점: 용량과 속도면에서 매우 효율적
# category자료형과 문자열로 각각 성별을 저장한 경우 용량의 차이를 확인해 봅시다. 
print(tips.dtypes)
#%%
tips['sex']=tips['sex'].astype(str)
print(tips.dtypes)
print(tips.info())
#%%
tips['sex']=tips['sex'].astype('category')
print(tips.dtypes)
print(tips.info())
# %%

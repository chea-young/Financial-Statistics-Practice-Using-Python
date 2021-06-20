""""""""""""""""""""""""""" 파이썬 기초 """"""""""""""""""""""""""""""""""""""" #%% 참고 교재: 데이터 분석을 위한 판다스 입문 p.204 ~ p.210
#%% 1. 간단한 함수 만들기
# 사용자 정의 함수는 다음과 같은 기본 구조
# def my_function():
# 코드... # return x
def my_sq(x):
 return x**2
print(my_sq(3))

def my_exp(x,n):
 return x**n
print(my_exp(2,4))

#%% 2. apply메서드 사용 - 기초
import pandas as pd

df=pd.DataFrame({'a':[10,20,30], 'b':[20,30,40]})
print("===============1================")
print(df)
print(df['a']**2)

# 사용자 정의 함수를 사용하여 동일한 결과를 출력해봅시다. 
# 1개의 인자를 전달 받는 my_sq()의 경우
sq=df['a'].apply(my_sq)
print("===============2================")
print(sq)

# 2개의 인자를 전달 받는 my_exp()의 경우
ex=df['a'].apply(my_exp, n=2) #NOTE  apply 첫번째는 함수이름, 뒤에는 파라미터 = 들어갈 data
print("===============3================")
print(ex)

#%% 다음과 같이 바꿔 볼까요?
def my_exp2(n,x):
    return x**n

print(my_exp2(2,3))
ex=df['a'].apply(my_exp2, n=2)
print(ex)

#%% 다음은 어떨까요? 차이를 잘 생각해보세요. 
def my_exp2(n,x):
 return x**n
ex=df['a'].apply(my_exp2, x=2)
print(ex)

#%% HIGHLIGHT apply()메서드에서 첫 번째 인수가 데이터가 되어야 합니다.
# axis인자를 사용하여 함수를 열 또는 행방향으로 적용
def print_me(x):
 #print('1')
 #print("----------1----------")
 #print(type(x))
 #print("---------2-----------")
 print(x)

print("===============1================")
print(df)
print("===============2================")
print(df.apply(print_me)) # NOTE 열이 따로 따로 자동으로 들어감.
print("===============3================")
print(df.apply(print_me, axis=0)) # NOTE axis=0은 열기준
print("===============4================")
print(df.apply(print_me, axis=1)) # NOTE axis=1은 행기준

#%% 위의 결과로 부터 사용자 정의 함수가 적용 되는 원리를 유추할 수 있겠죠?
# 3개 인자를 받는 경우
def avg_3(x,y,z):
 return (x+y+z)/3
print(df.apply(avg_3)) # 에러의 내용을 살펴 보세요. 

#%% 다음과 같이 수정해 봅시다. 
def avg_3_apply(col):
# print('1')
 x=col[0]
 y=col[1]
 z=col[2]
 return (x+y+z)/3
print(df.apply(avg_3_apply))

#%% 위 코드의 일반화
def avg_3_apply(col):
   print(col)
   sum=0
   for item in col:
      sum +=item # sum=sum+item
   return sum/df.shape[0]

print("===============1================")
print(df.apply(avg_3_apply))
df2=pd.DataFrame({'a':[10,20,30,40], 'b':[20,30,40,50], 'c':[50,60,70,80]})
print("===============2================")
print(df2.apply(avg_3_apply))

#%% [과제 31-1] 위의 코드에서 평균을 제대로 구할 수 있도록 수정해서 제출하세요. 
# Hint: 자료의 개수를 세고 저장할 변수를 만들어 sum에 나누어 주세요.
# 행방향으로 평균을 구해 봅시다. 
def avg_2_apply(row):
 sum=0
 for item in row:
    sum +=item
 return sum/df.shape[1]
print(df.apply(avg_2_apply,axis=1))
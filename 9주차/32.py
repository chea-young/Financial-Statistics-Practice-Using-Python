""""""""""""""""""""""""""" 파이썬 기초 """"""""""""""""""""""""""""""""""""""" 
#%% 참고 교재: 데이터 분석을 위한 판다스 입문 p.211 ~ p.210
# apply()메서드를 사용법을 실제 자료를 가지고 실습해 봅시다.
import seaborn as sns
titanic=sns.load_dataset("titanic") # titanic데이터에는 타이타닉 침몰 시 탑승자에 대한 데이터 저장
print(titanic.info())

#%% 누락값의 개수를 반환하는 사용자 정의 함수를 만들고 누락값의 개수를 세어 봅시다.
import numpy as np
import pandas as pd
def count_missing(vec):
 null_vec=pd.isnull(vec)
 #print("===============1================")
 #print(null_vec)
 null_count=np.sum(null_vec) # 열로 합쳐짐
 return null_count
cmis_col=titanic.apply(count_missing) # 열마다 들어감
#print("===============2================")
print(cmis_col)

#%% 누락값의 비율을 계산하는 사용자 정의 함수를 만들고 누락값의 비율을 계산해 봅시다. 
def prop_missing(vec):
 num=count_missing(vec)
 dem=vec.size
 return num/dem

pmis_col=titanic.apply(prop_missing)
print(pmis_col)

#%% 행방향으로 데이터를 처리해 봅시다. 
cmis_row=titanic.apply(count_missing,axis=1)
pmis_row=titanic.apply(prop_missing,axis=1)
print(cmis_row.head())
print(pmis_row.head())

#%% 이제 누락값의 개수를 구하여 titanic데이터프레임에 추가하여 봅시다. 
titanic['num_missing']=titanic.apply(count_missing,axis=1)
print(titanic.head())
# 누락값이 있는 데이터만 모아 봅시다. 
titanic_missing=titanic.loc[titanic.num_missing>1,:]
print(titanic_missing)
# %%

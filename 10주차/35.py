""""""""""""""""""""""""""" 파이썬 기초 """"""""""""""""""""""""""""""""""""""" #%% 참고 교재: 데이터 분석을 위한 판다스 입문 p.230 ~ p.239
#%% 1. 데이터 필터링 
import seaborn as sns
tips=sns.load_dataset('tips')
print(tips[:10])
print(tips.shape)
print(tips['size'].value_counts())
tips_filtered=tips.groupby('size').filter(lambda x: x['size'].count()>=30) # Series의 count()메서드
tips_filtered2=tips.groupby('size').filter(lambda x: len(x)>=30) # len()메서드 사용
print('---------------1-----------------')
print(tips_filtered)
print('---------------2-----------------')
print(tips_filtered2)

#%% 2. 그룹 오브젝트
# groupby메서드의 결과값인 그룹 오브젝트에 대해 살펴봅시다. 
# tips데이터 집합에서 임의로 10개의 데이터 추출
tips_10=sns.load_dataset('tips').sample(10, random_state=40)

# groupby 메서드의 결과값을 출력 => 자료형이 DataFrameGroupBy object (그룹 오브젝트)
grouped=tips_10.groupby('sex')
print('---------------1-----------------')
print(grouped)
# DataFrameGroupBy object에 있는 그룹을 보려면 groups속성을 출력
print('---------------2-----------------')
print(grouped.groups)

#%% 그룹의 평균 구하기
avgs=grouped.mean()
print('---------------1-----------------')
print(avgs)
# smoker, day, time에 대해서는 평균을 반환하지 않음
# 위의 결과로 부터 파이썬은 그룹 연산에 적합한 열만 알아서 골라 계산
# 만약 그룹오브젝트에서 특정 데이터만 추출하려면 get_group메서드를 사용
female=grouped.get_group('Female')
male=grouped.get_group('Male')# 그룹별로 반복문 적용
for sex_group in grouped:
    print('---------------2-----------------')
    print(sex_group)
    # sex_group은 튜플: 리스트와 동일한데 값 변경이 불가
    print(type(sex_group)) 
#%%
mean_vec=[]
for sex_group in grouped:
    mean_vec.append(sex_group[1].mean()) # NOTE sex_group[0]은 Female, male
print('---------------3-----------------')
#print(mean_vec)

#%% 앞서 배운 다른 방법으로 해볼까요? 
male2=tips_10.loc[tips_10.sex=='Male',:] 
male_mean=male2.mean() 
print('---------------1-----------------')
print(male_mean)

# size 그룹으로 해 볼까요?
grouped2=tips_10.groupby('size') 
for size_group in grouped2:# NOTE 2, 3, 4 가 따로 들어옴
    print('---------------2-----------------')
    print(size_group)

#%% 여러 열을 사용해 그룹 오브젝트 만들고 계산
bill_sex_time=tips_10.groupby(['sex','time'])
group_avg=bill_sex_time.mean() # DataFrame으로 생성
print('---------------1-----------------')
print(group_avg)

# group_avg의 index는 Multiindex형태 (여러 인데스를 담고 있는 index)
# index를 새로 부여
group_method=tips_10.groupby(['sex','time']).mean().reset_index()
print('---------------2-----------------')
print(group_method)
# %%

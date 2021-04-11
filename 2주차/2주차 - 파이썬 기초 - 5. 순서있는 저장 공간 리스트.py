""""""""""""""""""""""""""" 파이썬 기초 """""""""""""""""""""""""""""""""""""""

#%% 5. 순서있는 저장 공간 리스트

# List: 순서가 있는 데이터를 다룰 때 사용하는 데이터 구조(배열(array)이라고도 함)
# 앞서 우리가 본 코드에서 대괄호'[]'로 감싸고 각각의 값은 콤마로 구분한 것이 리스트
for i in [0,1,2,3]:
    print(i*2)

z=[0,1,2,3]
for i in z:
    print(i*2)

names=['쵸파','루피','상디','조로']    
for name in names:
    print(name)

temp=[['쵸파',10,'쵸코파이 줄임말'],['루피',20,'뽀로로의 친구']]

#%% 5-1 리스트에 저장된 색인(index)로 값에 접근하기
# 다음 코드를 실행해 봅시다.
names=['쵸파','루피','상디','조로']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# 리스트를 셀 때 색인(index)을 0부터 시작!
# index는 음수로도 사용할 수 있는데 이런 경우 뒤에서 부터 셈
names=['쵸파','루피','상디','조로']
print(names[-1])
print(names[-2])
print(names[-3])
print(names[-4])


#%% 5-2 리스트에 저장된 위치로 데이터의 일부 자르기(slicing)
names=['쵸파','루피','상디','조로']
print(names[0:2])           # 주의: names[2]인 '상디'는 포함하지 않음
print(names[1:3])           # 주의: names[3]인 '조로'는 포함하지 않음
print(names[1:])
print(names[:])


#%% 5-3 리스트에 값 추가하기
# 기존의 리스트에 값을 추가할 때는 append라는 함수 사용
names=['쵸파','루피','상디','조로']
names.append('나미')
print(names)

# len(): 리스트의 길이를 반환하는 함수
print(len(names))                                 # names라는 리스트의 길이 출력     
print(len('Financial Statistics using Python'))   # 문자열의 길이 출력  

z=[['쵸파',10],['루피',20],['상디',30]]
print(len(z))

# 간단한 예제
names=['쵸파','루피','상디','조로']
names.append('해적왕')
for name in names:
    if len(name)>2:
        print(name,'이름이 3자 이상입니다.')
        

#%% [과제 5-1] names=['괌','미국','캐나다','대한민국','해적왕','뽀로로']라는 리스트를
#             만들고 for 반복문, if 조건문, len()함수를 사용하여 
#             3자 이상인 이름만 따로 모은 리스트를 출력하는 코드를 작성하시오.
#             hint: 3자 이상인 이름만 담을 리스트를 미리 long_names=[] 를 사용하여 
#                   생성
names=['괌','미국','캐나다','대한민국','해적왕','뽀로로']
long_name = []
for i in name:
    if(len(i) >= 3):
        long_name.append(i)
print(long_name)
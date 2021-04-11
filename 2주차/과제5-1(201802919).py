#%% [과제 5-1] names=['괌','미국','캐나다','대한민국','해적왕','뽀로로']라는 리스트를
#             만들고 for 반복문, if 조건문, len()함수를 사용하여 
#             3자 이상인 이름만 따로 모은 리스트를 출력하는 코드를 작성하시오.
#             hint: 3자 이상인 이름만 담을 리스트를 미리 long_names=[] 를 사용하여 
#                   생성
names=['괌','미국','캐나다','대한민국','해적왕','뽀로로']
long_name = []
for i in names:
    if(len(i) >= 3):
        long_name.append(i)
print(long_name)
from math import gcd

first_num = int(input('첫번째 수를 입력해주세요: '))
second_num = int(input('두번째 수를 입력해주세요: '))
print(str(first_num) + '와 '+ str(second_num) + '의 최대 공약수는 ' + str(gcd(first_num, second_num)) +'입니다.')
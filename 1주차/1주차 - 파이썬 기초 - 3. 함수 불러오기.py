""""""""""""""""""""""""""" 파이썬 기초 """""""""""""""""""""""""""""""""""""""

#%% 3. 함수 불러오기

#%% 3-1 파이썬에서 제공하는 함수
# 파이썬에 내장되어 있는 함수 (내장함수; Built-in-Functions): 많은 함수들이 
# 파이썬에서 항상 사용할 수 있도록 내장
# 하지만 내장 함수가 모든 함수를 제공하지는 않습니다.
# 따라서 내장 되어 있지 않은 함수들은 별도로 불러서 사용해야 합니다.
# 내장함수 외의 함수들을 불러올 때는 내장되어 있지 않은 함수를 가지고 있는 
# 라이브러리(Library)를 불러와야 합니다.

#%% 3-1 import명령어
# 라이브러리를 불러오기 위해 사용하는 명령어
import random                 # random이라는 라이브러리(모듈이라고도 함)를 불러옴
dice=random.randint(1,6)      # random 라이브러리에 있는 randint이라는 함수 실행하고 결과를 dice변수에 저장
print(dice)                   # dice변수에 저장된 숫자를 출

# randint(a,b): [a,b]사이에 있는 정수중에서 무작위로 추출한 하나의 정수를 반환하는 함수
# random.randint(1,6): random이라는 라이브러리에 있는 randint이라는 함수를 실행하라는 의미
# 파이썬 자체에 내장되어 있는 함수의 경우는 라이브러리를 생략하고 사용
# 예) print(), input()


#%% Tips: 함수 도움말
# 파이썬 코드를 작성하다 보면 함수에 대한 도움말이 필요한 경우가 있습니다. 
# 다음과 같이 대략 네가지 방법으로 확인할 수 있습니다.

#   i) 도움말을 보고자 하 함수에 커서를 위치시킨후 [Ctrl+i]를 누르면 help창이 나타나면서 
#      함수가 들어 있는 라이브러리 및 함수에 대한 설명을 볼 수 있습니다.

#  ii) [메뉴]-[Tools]-[Preferences]-[Help]에서 [Automatic connections]의 
#      [Editor]와 [IPython Console]에 체크를 하면 함수를 Editor에 입력할 때 마다 
#      자동으로 [help]창에서 함수에 대한 도움말을 확인할 수 있습니다.

# iii) [Console]창에서 "?random.randint"이라고 입력하면 함수에 대한 
#      도움말을 볼 수 있습니다.

#  iv) 마지막으로 인터넷 검색 활용: 다음 URL을 방문하여 필요한 라이브러리와 함수 검색
#      https://docs.python.org/ko/3/library/index.html


#%% 3-2 제곱근 함수
import math
print(math.sqrt(2))


#%% Tips: 파이썬 레이아웃
# 프로그램을 실행한 후 변수의 확인 등 여러 가지 창을 동시에 봐야하는 경우
# [메뉴]-[View]-[Window layouts]에 가면 다양한 layout을 선택할 수 있어요.
# 본인에게 편한 layout을 찾아서 잘 활용해 보세요.


#%% [과제 3-1] 주사위를 두 번 던져서 생성된 값을 저장하고 두 숫자의 최대공약수를
#            계산하고 다음을 출력하는 코드를 작성하세요.
#            "첫번째 수를 입력해주세요: 3
#             두번째 수를 입력해주세요: 6
#             3와 6의 최대공약수는 3입니다."
#            hint: 최대공약수는 영어로 Greatest Common Divisor라고 합니다. 
#                  최대공약수를 반환하는 파이썬 함수를 인터넷 검색하세요.
from math import gcd

first_num = int(input('첫번째 수를 입력해주세요: '))
second_num = int(input('두번째 수를 입력해주세요: '))
print(str(first_num) + '와 '+ str(second_num) + '의 최대 공약수는 ' + str(gcd(first_num, second_num)) +'입니다.')
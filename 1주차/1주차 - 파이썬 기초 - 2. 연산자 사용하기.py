""""""""""""""""""""""""""" 파이썬 기초 """""""""""""""""""""""""""""""""""""""

#%% 2. 연산자 사용하기

#%% 2-1 산술 연산자
print(10+3)                   # 덧셈
print(10-3)                   # 뺄셈 
print(10*3)                   # 곱셈
print(10**3)                  # 거듭 제곱
print(10/3)                   # 나눗셈
print(10//3)                  # 나눗셈의 몫 구하는 연산자 
print(10%3)                   # 나눗셈의 나머지 구하는 연산자


#%% 2-2 비교 연산자
# 비교 연산자는 계산한 식이 참이면 True, 거짓이면 False라는 값을 반납
print(10>3)                  # 10이 3보다 큰지를 비교
print(10<=3)                 # 10이 3보다 작거나 같은지를 비교
print(10==3)                 # 10이 3과 같은지를 비교, =연산자는 변수에 값 할당
print(10!=3)                 # 10이 3과 다른지를 비교
print(3%2==1)                # 무엇을 의미하는나요?   


#%% 2-3 논리 연산자
# 논리 연산자는 True, False를 반환하는 연산자
# and 연산자 (논리곱 연산자): 둘 다 True인 경우 True 반환
print(1==1 and 2!=1)         # True and True ==> True 반환
print(10%2!=0 and 1+1>0)     # False and True ==> False 반환

# or 연산자 (논리합 연산자): 둘 중 하나라도 True이면 True 반환
print(10<5 or 10==5)         # False or False ==> False 반환
print(10%2!=0 or 1+1>0)      # True or False ==> True 반환

# not 연산자 (논리 부정): True이면 False 반환, False 이면 True 반환
print(not 10>5)              # True ==> False 반환
print(not 10==5)             # False ==> True 반환
print(not 0)                 # 0은 False와 동일 의미 ==> True 반환
print(not 10)                # 0이외의 숫자는 True를 의미 ==> False 반환


#%% Tips: 한글 변수명
# 파이썬은 변수명으로 한글을 지원합니다.
내나이=20
몇해후=10
print('나는 '+str(몇해후)+'년 후에는'+str(내나이+몇해후)+'살이 된다.')


#%% [과제 2-1] 한글변수명을 사용하여 학생의 국어와 영어 점수를 입력받은 후 
#             국어나 영어 점수 중 하나라도 90점보다 높으면 
#             "이 학생은 언어능력이 우수한 학생입니까? True" 라고 출력하고                  
#             그렇지 않으면 
#             "이 학생은 언어능력이 우수한 학생입니까? False" 라고 출력하는 
#             코드를 작성해 보세요.
korean = int(input('국어 점수를 입력하세요: '))
english = int(input('영어 점수를 입력하세요: '))
print('이 학생은 언어능력이 우수한 학생입니까? '+ str(korean>90 or english>90))
""""""""""""""""""""""""""" 파이썬 기초 """"""""""""""""""""""""""""""""""""""" #%% 참고 교재: 데이터 분석을 위한 판다스 입문 p.184 ~ p.192
#%% 1. 문자열 다루기
# 문자열은 작은 따옴표나 큰따옴표로 감싸서 생성
word='grail'
sent='a scratch'
# 인덱스로 문자열 추출하기
# 문자열은 문자 하나에 index가 0부터 부여
# 첫 번째 문자
print(word[0])
print(sent[0])

#%% 인덱스 슬라이싱
print(word[0:3]) # 첫 세문자
print(sent[-1]) # 맨 마지막 문자
print(sent[-9:-8]) # 끝에서 9번째~8번째 문자

#%% 전체 문자열 추출하기
print(word[:3]) # 왼쪽 범위를 생략하면 0부터 라는 의미와 동일
print(sent[2:len(sent)]) # 처음에서 3번째 부터 끝 문자까지
print(sent[2:]) # 오른쪽 범위를 생략하면 끝까지와 동일
print(sent[:]) # 양쪽을 모두 비우면 전체 문자열
print(sent[::2]) # 전체문자열을 추출하되 맨 왼쪽부터 추출하고 그 이후는

 # 추출한 문자로 부터 2번째 오는 문자들만 추출
#%% [과제 29-1] sent에서 3번째 문자부터 추출하고 그 이후는 추출한 문자로 부터 3번째 오는 문자들만
# 추출하여 print하는 코드를 작성하세요.
sent='a scratch'
string = sent[2:]
while(True):
    try:
        print(string[2])
        string = string[2:]
    except Exception as e:
        print(e)
        break


#%% 2. 문자열 메서드
# ----------------------------------------------------------------------------- # 메서드 | 설명
# -------------------------------------------------
# capitalize | 첫 문자를 대문자로 변환
# count | 문자열의 개수를 반환
# startswith | 문자열이 특정문자로 시작하면 True 아니면 False 반환
# endwith | 문자열이 특정문나로 끝나면 True 아니면 False 반환
# find | 찾을 문자열의 첫 번째 인덱스를 반환, 없는 경우 -1을 반환
# index | find메서드와 같은 역할을 수행하지만 없는 경우 ValueError를 반환
# isalpha | 몬든 문자가 알파벳이면 True 아니면 False 반환
# isdecimal | 모든 문자가 숫자면 True 아니면 False 반환
# isalnum | 모든 문자가 알파벳이거나 숫자면 True 아니면 False 반환
# lower | 모든 문자를 소문자로 변환
# upper | 모든 문자를 대문자로 변환
# replace | 문자열의 문자를 다른 문자로 교체
# strip | 문자열의 맨 앞과 맨 뒤에 잇는 빈 칸을 제거
# split | 구분자를 지정하여 문자열을 나누고, 나누 값들의 리스트를 반환
# partition | split메서드와 비슷한 역할을 수행하지만 구분자도 반환
# center | 지정한 너비로 문자열을 늘이고 문자열을 가운데 정렬
# zfill | 문자열의 빈 칸을 '0'으로 채움
# -----------------------------------------------------------------------------
"black Knight".capitalize()
"It's just a flesh wound!".count('u')
"Halt! Who goes there?".startswith('Halt') # 해당 문자로 시작하면 True 아니면 False
"coconut". endswith('nut')# 해당 문자로 끝나면 True 아니면 False
"It's just a flesh wound!".find('u') # index 반환, 없으면 -1 반환
"It's just a flesh wound!". index('scratch') # index 반환, 없으면 Error 반환
"old woman". isalpha()
"37".isdecimal()
"I'm 37".isalnum()
"Black Knight".lower( )
"Black Knight".upper()
"flesh wound!".replace('flesh wound', 'scratch')
" I'm not dead. ".strip( )
"NI! NI! NI! NI!".split(sep=' ')
"3,4".partition(',')
"nine".center(10)
"9".zfill(5)

# join메서드
# join메서드는 문자열을 연결하여 새로운 문자열 반환
d1='40^'
m1="46'"
d2='73*'
m2="58'"
coords='yaya'.join([d1,m1,d2,m2])

# splitlines메서드
multi_str="""Guard: What? Ridden on a horse?
King Arthur: Yes!
""" 
multi_str_split=multi_str.splitlines()
print(multi_str_split)
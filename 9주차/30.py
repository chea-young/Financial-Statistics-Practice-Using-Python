""""""""""""""""""""""""""" 파이썬 기초 """"""""""""""""""""""""""""""""""""""" 
#%% 참고 교재: 데이터 분석을 위한 판다스 입문 p.193 ~ p.196
#%% 1. 문자열 포멧팅
# 문자열 포멧팅은 문자열을 편리하게 출력할 수 있게 해주는 기능
# 단어를 삽입할 위치를 {}로 지정하고 format메서드에 원하는 단어를 전달하면 {}위치에
# 전달한 단어를 삽입해 출력
# {}: 플레이스 홀더라고 부름
var='fresh wound'
s="It's just a {}!"
print(s.format(var))
print(s.format('scarach'))

# 플레이스 홀더에 여러 단어를 전달할 때는 index를 사용할 수 있음
s="""Black Knight: It's but a {0}.
King Arthur: A {0}? Your arm's {1}!
""" 
print(s.format('scrach','off'))

#%% 플레이스 홀더에 여러 단어를 전달할 때 index를 사용하는 대신 변수로 지정도 가능
s="""Black Knight: It's but a {var1}.
King Arthur: A {var1}? Your arm's {var2}!
""" 
print(s.format(var1='scrach',var2='off'))

#%% 2. 숫자 데이터 포멧팅 하기
# 숫자 데이터도 플레이스 홀더 사용 가능
print('Some digits of pi: {}'.format(3.14159265359))
# 플레이스 홀더에 :, 를 넣으면 쉼표를 넣어 숫자로 표현 가능
print('In 2005, Lu Cho of China recited {:,} digits of pi'.format(67890))
# 소수에 대한 다양한 표현 방법
print("I remember {0:.2} or {0:.8%} of what Lu Chao recited".format(70000/67890))
# {0:.4} 1보다 작은 소수에 대하여 소수점이하 0이 아닌 값이 나오는 자리 부터 4번째
# 까지 표현하고 1보다 큰 수에 대해서는 소수점 이상과 이하를 모두 포함하여
# 4자리 까지 표현
# {0:.4%} 소수점하 4번째 이까지 표현
# 만약 42와 같은 2자리 값을 00042로 출력해야 한다면
print("My ID number is {0:05d}".format(42)) # d는 decimal을 의미

#%% 3. % 연산자로 포멧팅하기
#플레이스 홀더를 사용하는 대신 % 연산자로도 포멧팅이 가능
# 마치 C언어에서 printf()메서드의 출력형식과 유사
s='Some digits of pi: {}'
print(s.format(3.14159265359))
s='Some digits of pi: %.5f' % 3.14159265359 
# %.12f 는 소수 12자리 까지 소수표현
print(s)
# 삽입할 값이 문자열인 경우 %s를 사용하고, 
# 여러 값을 삽입할 경우 변수를 사용하고 지정할 값들은 {}로 지정
print('Some digits of %(cont)s: %(value).2f' % {'cont':'e','value':2.718})
var1='e'
var2=2.718
print('Some digits of %(cont)s: %(value).2f' % {'cont':var1,'value':var2})

#%% 4. f-strings 포멧팅 사용하기: 가독성이 훤씬 좋음
var='fresh wound'
s="It's just a {}!"
print(s.format(var))
print(f"It's just a {var}!")
lat='40.7815oN'
lon='73.9733oW'
s=f'Hayden Planetarium Coordinates: {lat},{lon}'
print(s)
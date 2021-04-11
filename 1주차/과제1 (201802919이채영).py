import datetime
name = input('이름을 입력하세요: ')
age = input('나이를 입력하세요: ')
year = int(datetime.datetime.now().strftime('%Y')) - int(age)
print(name + "의 출생년도는 " + str(year) + "년 입니다." )
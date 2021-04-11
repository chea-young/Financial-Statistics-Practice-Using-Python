
import csv
f=open('seoul.csv','r',encoding='cp949')
data=csv.reader(f,delimiter=',')
header=next(data)  
max_daily_temp=-999                             # 최고기온을 담을 공갈 변수
maxt_date=''  
for row in data:
    # 최고 기온 바꾸기
    if row[-1]=='':
        row[-1]=-999
    else:
        row[-1]=float(row[-1])
    # 최저 기온 바꾸기
    if row[-2]=='':
        row[-2]=-999
    else:
        row[-2]=float(row[-2])
    daily_temper = row[-1] - row[-2]
    #일교차 큰 값 찾기 위해 비교하기
    if max_daily_temp<daily_temper:
        max_daily_temp=daily_temper
        max_date=row[0]
f.close()
print('기상 관측 이래 서울의 일교차가 가장 컸던 날은',max_date+'로',str(max_daily_temp)+'도 였습니다.')
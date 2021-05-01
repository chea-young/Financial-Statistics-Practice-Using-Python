[10주차 실습 코드 주의사항]

1.  "파이썬 기초 - 33. 그룹연산 - 1. 데이터 집계" 실습파일
     - 실습 파일의 마지막 코드
        # 딕셔너리의 키로 집계 메서드를 적용할 열 이름을 전달하고, 딕셔너리 값으로 집계 메서드를 전달

        gdf_dic=df.groupby('year').lifeExp.agg({'lifeExp': 'mean', 'pop': 'median','gdpPercap':'median'})
        를 다음과 같이 변경하여 실행하기 바랍니다.
        gdf_dic=df.groupby('year').agg({'lifeExp': 'mean', 'pop': 'median','gdpPercap':'median'})

2. "파이썬 기초 - 37. 시계열 데이터 - 2. 사례별 시계열 데이터 계산하기" 실습파일

     - 실습 파일 중간 테슬라 주식 관련 코드
        #%% 3. 테슬라 주식 데이터로 시간 계산하기
        import pandas as pd
        tesla=pd.read_csv('tesla_stock_quandl.csv',parse_dates=[0])
        # 2010년 6월 데이터만 추출해봅시다.

        print(tesla.loc[(tesla.Date.dt.year==2010) & (tesla.Date.dt.month==6)])
        # datetime오브젝트를 데이터프레임의 index로 설정하면 원하는 시간의 데이터를 편리하게 추출

        tesla.index=tesla['Date']
        tesla_2015=tesla['2015']
        tesla_201006=tesla['2010-06']
        tesla_20151231=tesla['2015-12-31']

        에서 마지막 4줄을 다음과 같이 변경하여 실행하기 바랍니다.
        tesla.index=tesla['Date']
        tesla_2015=tesla.loc['2015']
        tesla_201006=tesla.loc['2010-06']
        tesla_20151231=tesla.loc['2015-12-31']

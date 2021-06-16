#%% 참고 교재: 데이터 분석을 위한 판다스 입문 p.76 ~ p.79

#%% 3-1. 데이터 피클로 저장하기: to_pickle()메서드
# 피클로 데이터를 저장하면 작은 용량으로 데이터 저장 가능
import pandas as pd
scientists=pd.read_csv('scientists.csv')
names=scientists['Name']
print(names)
print('=======================================================')
names.to_pickle('scientists_names_series.pickle') # to_pickle메서드를 사용하여 Series를 피클로 저장
scientists.to_pickle('scientists_df.pickle') # to_pickle메서드를 사용하여 DataFrame을 피클로 저장

#%% 피클 데이터 열기: read_pickle()메서드
scientist_names_from_pickle=pd.read_pickle('scientists_names_series.pickle')
scientist_from_pickle=pd.read_pickle('scientists_df.pickle')
print(scientist_names_from_pickle)
print('=======================================================')
print(scientist_from_pickle)
print('=======================================================')
#%% CSV 또는 TSV파일로 저장하기: to_csv()메서드
names.to_csv('scientists_names_series.csv',sep=',')
scientists.to_csv('scientists_df.csv',sep=',') 
names.to_csv('scientists_names_series.tsv',sep='\t')
scientists.to_csv('scientists_df.tsv',sep='\t') 
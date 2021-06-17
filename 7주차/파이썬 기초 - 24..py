#%% 참고 교재: 데이터 분석을 위한 판다스 입문 p.132 ~ p.136
#%% 1. merge메서드 사용하기
# merge메서드를 사용하여 좀 더 원하는 형태로 데이터를 연결하여 봅시다.
import pandas as pd
import sys 

#sys.path.append('/src/GG') # NOTE absolute path

person=pd.read_csv('survey_person.csv')
site=pd.read_csv('survey_site.csv')
survey=pd.read_csv('survey_survey.csv')
visited=pd.read_csv('survey_visited.csv')

visited_subset=visited.loc[[0,2,6],] # 특정 index만 갖는 일부 데이터 생성
# left_on, right_on : 각 join할 key (서로 다른 key 값을 갖을 경우)
o2o_merge=site.merge(visited_subset,left_on='name',right_on='site')

print(visited)
print('---------------------------')
print(visited_subset)
print('============================')

print(site)
print('---------------------------')
print(o2o_merge)
print('============================')
#%% 위의 코드는 'site'의 'name'과 'visited_subset'의 'site' 이 동일한 index를 찾아서
# 'site'를 기준으로 'visited_subset'에 있는 값을 붙여넣어라는 의미
# 몇 가지 더 해봅시다. 
ps=person.merge(survey,left_on='ident',right_on='person') # left_on은 person, right_on은 survey
vs=visited.merge(survey,left_on='ident',right_on='taken')

print(survey)
print('---------------------------')
print(person)
print('---------------------------')
print(visited)
print('---------------------------')
print(ps)
print('============================')
print(vs)
print('============================')

#%% left_on, right_on에 전달하는 값은 여려개도 가능
ps_vs = ps.merge(vs,left_on=['ident','taken','quant','reading'],right_on=['person','ident','quant','reading'])
# merge메서드의 left 데이터프레임과 right 데이터프렘임에 동일한 변수가 있다면
# 변수명 뒤에 '_x' 와 '_y'를 붙여 구분하여 표시

print(ps_vs)
# %%

#%% 참고 교재: 데이터 분석을 위한 판다스 입문 p.16 ~ p.168
#%% 2. 중복 데이터 처리하기
# 빌보드 차트 데이터를 다시 불러 옵시다.
import pandas as pd
bilboard=pd.read_csv('bilboard.csv')
bilboard_long=pd.melt(bilboard, id_vars=['year','artist','track','time','date.entered'], var_name='wek',value_name='rating')
# bilboard_long 데이터프레임을 보면 year, artist, track, time, date에서 중복 데이터가 많습니다. 
# 이러한 중복 데이터는 한 눈에 보기에는 편할 수 있지만, 
# 데이터가 매우 크다면 (정말 매우 크다면, 즉, 수백 GB 또는 TB 수준) 이러한 중복 데이터는
# 데이터 처리에 대한 시간을 지연시키고, 데이터 저장 공간을 많이 차지하며, 
# 다른 사람과 데이터를 공유하기도 어려워서 우리가 원하는 작업을 하는데 있어 비효율성을 야기합니다. # 따라서, 이러한 중복 데이터의 경우 unique한 값을 갖는 데이터따로 모아서 저장하고
# 구분할 수 있는 id를 부여한 후 관련 데이터와 id를 통해 연결하여 사용하는 것이 편리
# 중복데이터를 따로 모아서 중복데이터를 제거하여 봅시다. 
bilboard_songs=bilboard_long['year','artist','track','time']
bilboard_songs=bilboard_songs.drop_duplicates()
# 중복을 제거한 데이터에 고유 id를 부여
bilboard_songs['id']=range(len(bilboard_songs))
# merge메서드를 사용해 bilboard_long데이터와 연결하고 중복 데이터는 제거
bilboard_ratings=bilboard_long.merge(bilboard_songs,left_on=['year','artist','track','time'],right_on=['year','artist','track','time'])
# left_on과 right_on이 동일하면 on으로 줄여쓸 수 있습니다. 
bilboard_ratings=bilboard_long.merge(bilboard_songs,on=['year','artist','track','time'])
bilborad_ratings_tidy=bilboard_ratings.drop(columns=['year','artist','track','time'])
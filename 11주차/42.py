""""""""""""""""""""""""""" 파이썬 기초 """"""""""""""""""""""""""""""""""""""" 
#%% 참고 교재: 데이터 분석을 위한 판다스 입문 p.117 ~ p.119
# seaborn 라이브러리로 만든 그래프의 스타일을 변경

#%% 1. set_style 메서드
import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")

# 기본 스타일
ax=plt.subplots()
ax=sns.violinplot(x='time',y='total_bill', hue='sex', data=tips, split=True)

#%% seaborn라이브러리 스타일: darkgrid, whitegrid, dark, white, ticks의 5종류
# whitegrid 스타일
sns.set_style('darkgrid')
ax=plt.subplots()
ax=sns.violinplot(x='time',y='total_bill', hue='sex', data=tips, split=True)

#%% 동일한 코드: with문과 함께 사용할 때는 axes_style()메서드만 사용가능하며 temporarilystyle적용
with sns.axes_style('darkgrid'):
 ax=plt.subplots()
 ax=sns.violinplot(x='time',y='total_bill', hue='sex', data=tips, split=True)
 
#%% for문을 이용하여 모든 스타일을 한번씩 적용해 봅시다. 
seaborn_styles=['darkgrid','whitegrid','dark','white','ticks']
for idx, style in enumerate(seaborn_styles):
 print(idx, ':', style)

#%% enumerate(): 순서가 있는 자료형(list, set, tuple, dictionary, string)을 입력
# 받아 인덱스 값을 포함하는 enumerate 객체를 리턴
# 그림 그리기
fig=plt.figure()
seaborn_styles=['darkgrid','whitegrid','dark','white','ticks']
for idx, style in enumerate(seaborn_styles):
    plot_position=idx+1
    sns.axes_style(style) # axes_style() 도 사용가능하고, with문과 함께 axes_style사용가능
    ax=fig.add_subplot(2,3,plot_position)
    violin=sns.violinplot(x='time',y='total_bill',data=tips,ax=ax)
    violin.set_title(style)
fig.tight_layout()
# %%

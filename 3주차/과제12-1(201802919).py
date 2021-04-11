import matplotlib.pyplot as plt 

colors=input("""생성되기를 원하는 막대그래프이 색을 입력해주세요: 
                가능한 색은 [빨강, 주황, 노랑, 초록, 검정, 분홍, 보라]""")
color_list = {'빨강':'red', '주황': 'orange', '노랑': 'gold', '초록':'forestgreen', '검정':'black', '분홍': 'hotpink', '보라':'purple'}

plt.bar([0,1,2,3,6,10],[1,2,3,5,6,7], color=color_list[colors]) # bar(막대를 표시할 위치, 막대의 높이) 
plt.show()

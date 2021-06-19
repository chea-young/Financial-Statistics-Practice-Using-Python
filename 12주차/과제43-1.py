import numpy as np
PV=1000
r=0.05
n=5
m_max=1200
FV_compound=[]
for m in range(1,m_max+1):
    FV_compound.append(np.fv(r/m,n*m,0,-pv))

# m에 따른 FV_compound의 변화 그래프 그리기
import matplotlib.pyplot as plt
fig=plt.figure()
axes1=fig.add_subplot(1,1,1) # add_subplot(행크기, 열크기, 위치)
axes1.plot(range(1,m_max+1),FV_compound)
axes1.set_title("compounding effect")
axes1.set_xlabel('Compounding Frequency - m')
axes1.set_ylabel('Future Value - FV')
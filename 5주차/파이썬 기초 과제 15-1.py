
#과제
import matplotlib.pyplot as plt
import random
import numpy as np
x = 50 + np.random.choice(50, 10)
y = 50 + np.random.choice(50, 10)
size = 10 + np.random.choice(90, 10)
plt.scatter(x,y,s=size)
plt.show()

# 컬러바 추가
import matplotlib.pyplot as plt
import random
x=[]
y=[]
size=[]
x = 50 + np.random.choice(50, 10)
y = 50 + np.random.choice(50, 10)
size = 10 + np.random.choice(90, 10)
plt.scatter(x,y,s=size,c=size,cmap='jet')
plt.colorbar()
plt.show()

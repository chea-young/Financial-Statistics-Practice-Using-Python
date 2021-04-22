#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
from matplotlib import font_manager, rc
from matplotlib import style

# 1. 데이터를 읽어 온다
f=open('사고유형별.csv')
data=csv.reader(f)
next(data)
data=list(data) 

plt.style.use('ggplot')
plt.rc('font',family='Malgun Gothic')
plt.title('')

large = ''
graph = []
component_middle = []
component = []

for row in data:
    if(row[0] != large):
        graph.append((large,component_middle,component))
        large = row[0]
        component_middle = []
        component = []
    component_middle.append(row[1])
    component.append(row[2])
plt.figure(figsize = (12, 5))
location = 1
for i in graph[1:]:
    plt.subplot(1, 3, location)
    plt.title(i[0])
    plt.pie(i[2], labels=i[1], shadow=True, startangle=90)
    location +=1
plt.show()

        

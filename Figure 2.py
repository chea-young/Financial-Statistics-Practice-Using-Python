#%%
import matplotlib.pyplot as plt
import numpy as np

x = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
x_o = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]
x_y = [2013, 2014, 2015]
orange = [26.9, 27.7, 28.5, 29.1, 30.3, 31.4, 32.4, 33.3]
yellow = [36.3, 38.7, 43.7]
lime = [55.9, 59.6, 67.8]

fig = plt.figure(figsize=(17, 9))
plt.rcParams["font.family"] = 'Malgun Gothic'
#plt.grid()

plt.style.use('ggplot')
plt.rc('font',family='Malgun Gothic')
plt.title('''Traffic congestion costs by year
''',fontsize = 30)

plt.plot(x_o, orange, color = '#FF8C0A',label='Traffic congestion costs', marker='o', linestyle='solid', linewidth=4, markersize=12)
for i in range(len(x_o)):
    ay = str(int(orange[i]))
    annotation = ay
    plt.annotate(annotation, xy=(x[i] - .1, orange[i] + .7), size=20)

plt.plot(x_y, yellow, color = '#FFDC3C', label='Traffic congestion costs for new methods(B-1)', marker='*', linestyle='solid', markersize=12,linewidth=4)
for i in range(len(x_y)):
    ay = str(int(orange[i]))
    annotation = ay
    plt.annotate(annotation, xy=(x_y[i] - .1, yellow[i] + .7), size=20)

plt.plot(x_y, lime, color = '#8AE634', label='Traffic congestion costs for new methods(B-2)', marker='^', linestyle='solid', linewidth=4, markersize=12)
for i in range(len(x_y)):
    ay = str(int(lime[i]))
    annotation = ay
    plt.annotate(annotation, xy=(x_y[i] - .1, lime[i] + .7), size=20)

plt.grid(True, axis='y', color='gray', alpha=0.5, linestyle='--')
plt.tick_params(axis='both', direction='in', length=3, pad=6, labelsize=14)
plt.rc('xtick', labelsize=18) 
plt.rc('ytick', labelsize=18)
plt.legend(fontsize=15, fancybox=True, shadow=True, loc='upper left')
plt.savefig('Figure 2.png')
plt.show()

#
# %%

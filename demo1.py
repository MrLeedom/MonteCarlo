#求圆周率的近似值
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

#投点次数
n = 10000
#圆的半径＼圆心
r = 1.0
a,b = (0.,0.)
#正方形区域
x_min,x_max=a-r,a+r
y_min,y_max=b-r,b+r
#在正方形区域内随机投点
x = np.random.uniform(x_min,x_max,n)
y = np.random.uniform(y_min,y_max,n)
#计算点到圆心的距离
d = np.sqrt((x-a)**2+(y-b)**2)
#统计落在圆心的距离
res = sum(np.where(d<r,1,0))
#计算pi的近似值(Monte Carlo:用统计值去近似真实值)
pi = 4*res/n
print('pi:',pi)

#画图
fig = plt.figure()
axes = fig.add_subplot(111)
axes.plot(x,y,'ro',markersize=1)
plt.axis('equal')#防止图像变形
circle = Circle(xy=(a,b),radius=r,alpha=0.5)
axes.add_patch(circle)
plt.show()
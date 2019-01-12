import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def f(x):
    return x**2
#总次数
n = 1000
#矩形边界区域
x_min,x_max = 0.0,1.0
y_min,y_max = 0.0,1.0
#在矩形区域内随机投点x
x = np.random.uniform(x_min,x_max,n)
y = np.random.uniform(y_min,y_max,n)
#统计落在函数y=x^2下方的点
res = sum(np.where(y<f(x),1,0))
#计算定积分的近似值
integral = res/n
print('integral:',integral)
#画图
fig = plt.figure()
axes = fig.add_subplot(111)
axes.plot(x,y,'ro',markersize=1)
plt.axis('equal')
axes.plot(np.linspace(x_min,x_max,10),f(np.linspace(x_min,x_max,10)),'b-')
plt.show()
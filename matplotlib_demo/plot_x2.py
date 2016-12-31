import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2 * np.pi, 50)
plt.plot(x, np.sin(x),
        x, np.sin(2 * x))
plt.show()


# 自定义曲线的外观
x = np.linspace(0, 2 * np.pi, 50)
plt.plot(x, np.sin(x), 'r-o',
        x, np.cos(x), 'g--')
plt.show()

# 使用子图
x = np.linspace(0, 2 * np.pi, 50)
plt.subplot(2, 1, 1) # （行，列，活跃区）
plt.plot(x, np.sin(x), 'r')
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x), 'g')
plt.show()

# 简单的散点图
x = np.linspace(0, 2 * np.pi, 50)
y = np.sin(x)
plt.scatter(x,y)
plt.show()

# 彩色映射散点图
x = np.random.rand(1000)
y = np.random.rand(1000)
size = np.random.rand(1000) * 50
colour = np.random.rand(1000)
plt.scatter(x, y, size, colour)
plt.colorbar()
plt.show()


# 直方图
x = np.random.randn(1000)
plt.hist(x, 50)
plt.show()


# 添加标题，坐标轴标记和图例
x = np.linspace(0, 2 * np.pi, 50)
plt.plot(x, np.sin(x), 'r-x', label='Sin(x)')
plt.plot(x, np.cos(x), 'g-^', label='Cos(x)')
plt.legend() # 展示图例
plt.xlabel('Rads') # 给 x 轴添加标签
plt.ylabel('Amplitude') # 给 y 轴添加标签
plt.title('Sin and Cos Waves') # 添加图形标题
plt.show()



#! coding: cp936
from pylab import *

# -*- coding: utf-8 -*-   
from pylab import *  
myfont = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/simsun.ttc')  
mpl.rcParams['axes.unicode_minus'] = False  

# make a square figure and axes
figure(1, figsize=(6,6))
ax = axes([0.1, 0.1, 0.8, 0.8])

fracs = [45, 30, 25]             #每一块占得比例，总和为100
explode=(0, 0, 0.08)             #离开整体的距离，看效果
labels = 'Hogs', 'Dogs', 'Logs'  #对应每一块的标志

pie(fracs, explode=explode, labels=labels,
                autopct='%1.1f%%', shadow=False, startangle=90, colors = ("g", "r", "y"))
# startangle是开始的角度，默认为0，从这里开始按逆时针方向依次展开

#title(u'Raining Hogs and Dogs')   #标题
title(u'饼图')   #标题
show()


import numpy as np
import matplotlib.pyplot as plt
plt.figure(1)
plt.figure(2)
ax1 = plt.subplot(211)
ax2 = plt.subplot(212)
x = np.linspace(0, 3, 100)

y1=np.exp(1*x/3)
y2=np.exp(2*x/3)
y3=np.exp(3*x/3)
y4=np.exp(4*x/3)
y5=np.exp(5*x/3)
plt.figure(1)
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)
plt.plot(x, y5)


plt.sca(ax1)
z1=np.sin(1*x)
z2=np.sin(2*x)
z3=np.sin(3*x)
z4=np.sin(4*x)
z5=np.sin(5*x)
plt.plot(x, z1)
plt.plot(x, z2)
plt.plot(x, z3)
plt.plot(x, z4)
plt.plot(x, z5)

plt.sca(ax2)
w1=np.cos(1*x)
w2=np.cos(2*x)
w3=np.cos(3*x)
w4=np.cos(4*x)
w5=np.cos(5*x)
plt.plot(x, w1)
plt.plot(x, w2)
plt.plot(x, w3)
plt.plot(x, w4)
plt.plot(x, w5)
plt.show()
Fig = plt.figure(figsize=(800,400)) 
Fig.savefig("test1.pdf")


import matplotlib.pyplot as plt
X1 = range(0, 50)
Y1 = [num**2 for num in X1] # y = x^2
X2 = [0, 1]
Y2 = [0, 1]  # y = x
Fig = plt.figure(figsize=(8,4))                      # Create a `figure' instance
Ax = Fig.add_subplot(111)               # Create a `axes' instance in the figure
Ax.plot(X1, Y1, X2, Y2)                 # Create a Line2D instance in the axes
Fig.show()
Fig.savefig("test.pdf")

import numpy as np
import pylab as pl
x = [1, 2, 3, 4, 5]# Make an array of x values
y = [1, 4, 9, 16, 25]# Make an array of y values for each x value
pl.plot(x, y)# use pylab to plot x and y
pl.show()# show the plot on the screen


#test error
import numpy as np
import matplotlib.pyplot as plt
plt.figure(1) # 创建图表1
plt.figure(2) # 创建图表2
ax1 = plt.subplot(211) # 在图表2中创建子图1
ax2 = plt.subplot(212) # 在图表2中创建子图2
x = np.linspace(0, 3, 100)
for i in range(0,5):
    plt.figure(1)  #选择图表1
    plt.plot(x, np.exp(i*x/3))
    plt.sca(ax1)   #选择图表2的子图1
    plt.plot(x, np.sin(i*x))
    plt.sca(ax2)  # 选择图表2的子图2
    plt.plot(x, np.cos(i*x))
plt.show()

#test ok
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x**2)

plt.figure(figsize=(8,4))
plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
plt.plot(x,z,"b--",label="$cos(x^2)$")
plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("PyPlot First Example")
plt.ylim(-1.2,1.2)
plt.legend()
plt.show()
plt.show()


#run error
from matplotlib.matlab import * 
x = linspace(-4, 4, 200) 
f1 = power(10, x) 
f2 = power(e, x) 
f3 = power(2, x)  
plot(x, f1, 'r',  x, f2, 'b', x, f3, 'g', linewidth=2) 
axis([-4, 4, -0.5, 8])
text(1, 7.5, r'$10^x$', fontsize=16)
text(2.2, 7.5, r'$e^x$', fontsize=16)
text(3.2, 7.5, r'$2^x$', fonsize=16)
title('A simple example', fontsize=16)

savefig('power.png', dpi=75)
show() 
  
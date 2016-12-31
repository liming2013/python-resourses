# -*- coding: utf-8 -*-  
#description:设置图片边界,当前的图片边界设置得不好，所以有些地方看得不是很清楚。

# 导入 matplotlib 的所有内容（nympy 可以用 np 这个名字来使用）
from pylab import *

# 创建一个 10 * 6 点（point）的图，并设置分辨率为 80
figure(figsize=(10,6), dpi=80)

# 创建一个新的 1 * 1 的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）
subplot(1,1,1)

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)


#绘制余弦曲线，使用蓝色的、连续的、宽度为2.5（像素）的线条
plot(X, C, color="blue", linewidth=2.5, linestyle="-")

#绘制正弦曲线，使用绿色的、连续的、宽度为2.5（像素）的线条
plot(X, S, color="red",  linewidth=2.5, linestyle="-")

# 设置横轴的上下限
xlim(-4.0,4.0)

# 设置横轴记号
'''
设置记号

我们讨论正弦和余弦函数的时候，通常希望知道函数在 ±π±π 和 ±π2±π2 的值。这样看来，当前的设置就不那么理想了。
'''
xticks( [-np.pi, -np.pi/2, 0, np.pi/2, np.pi])

# 设置纵轴的上下限
ylim(-1.2,1.2)


# 设置纵轴记号
yticks([-1, 0, +1])

# xlim(X.min()*1.1, X.max()*1.1)
# ylim(C.min()*1.1, C.max()*1.1)
#===========================================
# xmin ,xmax = X.min(), X.max()
# ymin, ymax = Y.min(), Y.max()

# dx = (xmax - xmin) * 0.2
# dy = (ymax - ymin) * 0.2

# xlim(xmin - dx, xmax + dx)
# ylim(ymin - dy, ymax + dy)


# 以分辨率 72 来保存图片
# savefig("exercice_2.png",dpi=72)

# 在屏幕上显示
show()
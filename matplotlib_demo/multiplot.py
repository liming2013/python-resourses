#!/usr/bin/python
# -*- coding: UTF-8 -*-
# #matplotlib inline
import numpy as np
import matplotlib.pyplot as plt


func = np.poly1d(np.array([1, 2, 3, 4]).astype(float))
func2 = func.deriv(m=2)
x = np.linspace(-10, 10, 30)
y = func(x)
y2 = func2(x)

#绘制多项式函数及其导函数
func1 = func.deriv(m=1)
y1 = func1(x)

plt.subplot(311)
plt.plot(x, y, 'r-')
plt.title("Polynomial")

plt.subplot(312)
plt.plot(x, y1, 'b^')
plt.title("First Derivative")

plt.subplot(313)
plt.plot(x, y2, 'go')
plt.title("Second Derivative")
plt.show()



#绘制多项式函数
#其中，linspace函数常见x轴的数值，在-10和10之间产生30个均匀分布的值。

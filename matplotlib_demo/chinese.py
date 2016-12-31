#Matplotlib中文显示有问题,当然可以修改配置文件matplotlibrc ,不过较为麻烦.其实只要在代码中指定字体就可以了  
  
#第一种方法:  
  
# -*- coding: utf-8 -*-   
from pylab import *  
mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体  
  
mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题  
  
t = arange(-5*pi, 5*pi, 0.01)  
y = sin(t)/t  
plt.plot(t, y)  
plt.title(u'这里写的是中文')  
plt.xlabel(u'坐标')  
plt.ylabel(u'坐标')  
plt.show()  
  
   
  
   
  
#第二种方法 可行
  
# -*- coding: utf-8 -*-   
from pylab import *  
myfont = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/simsun.ttc')  
mpl.rcParams['axes.unicode_minus'] = False  
t = arange(-5*pi, 5*pi, 0.01)  
y = sin(t)/t  
plt.plot(t, y)  
plt.title(u'这里写的是中文',fontproperties=myfont) #指定字体  
plt.xlabel(u'X坐标',fontproperties=myfont)  
plt.ylabel(u'Y坐标',fontproperties=myfont)  
plt.show()  


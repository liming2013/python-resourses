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
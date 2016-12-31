# -*- coding: utf-8 -*-  
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab
from matplotlib import rcParams
fig1 = plt.figure(2)
rects =plt.bar(left = (0.2,1),height = (1,0.5),width = 0.2,align="center",yerr=0.000001)
plt.title('Pe')
plt.xticks((0.2,1),('frst','second'))
plt.show()


#增加直方图脚注

'''
1.1 上面中rects =plt.bar(left = (0.2,1),height = (1,0.5),width = 0.2,align=”center”,yerr=0.000001)这句代码是最重要的，其中left表示直方图的开始的位置（也就是最左边的地方），height是指直方图的高度，当直方图太粗时，可以通过width来定义直方图的宽度，注意多个直方图要用元组，yerr这个参数是防止直方图触顶。
'''

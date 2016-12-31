# -*- coding: utf-8 -*-
#直方图 Histograms

import numpy as np
import pylab as pl
# make an array of random numbers with a gaussian distribution with
# mean = 5.0
# rms = 3.0
# number of points = 1000
data = np.random.normal(5.0, 3.0, 1000)
# make a histogram of the data array
pl.hist(data)
# make plot labels
pl.xlabel('data')

'''
2.3.1 自定义直方图bin宽度 Setting the width of the histogram bins manually

增加这两行
'''
bins = np.arange(-5., 16., 1.) #浮点数版本的range
pl.hist(data, bins, histtype='stepfilled')

pl.show()
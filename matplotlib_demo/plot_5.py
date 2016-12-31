import numpy as np
import pylab as pl
x = [1, 2, 3, 4, 5]# Make an array of x values
y = [1, 4, 9, 16, 25]# Make an array of y values for each x value
pl.plot(x, y)# use pylab to plot x and y
pl.title('Plot of y vs. x')# give plot a title
pl.xlabel('x axis')# make axis labels
pl.ylabel('y axis')
pl.xlim(0.0, 7.0)# set axis limits
pl.ylim(0.0, 30.)
pl.show()# show the plot on the screen
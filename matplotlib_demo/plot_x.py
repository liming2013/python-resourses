import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-5,5,0.01)
y=x**3
plt.axis([-6,6,-10,10])
#plt.ylim()
plt.plot(x,y)
plt.show()
plt.grid(True)
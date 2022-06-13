#plotting a sin graph
import numpy as np
import matplotlib.pyplot as plt

xstart = 0
xstop = 2 * np.pi
increment = 0.1

x = np.arange(xstart, xstop, increment)
y = np.sin(x)

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
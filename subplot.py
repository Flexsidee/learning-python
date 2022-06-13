"""
creating a subplot of sin and cos
Created on Mon Jun 13 19:13:51 2022

@author: Flexsidee


"""

import matplotlib.pyplot as plt
import numpy as np

xstart = 0
xstop = 2 * np.pi
increment = 0.1

x = np.arange(xstart, xstop, increment)
y = np.sin(x)
z = np.cos(x)

plt.subplot(2, 1, 1)
plt.plot(x, y, 'g')
plt.title('sin')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid()
plt.show()

plt.subplot(2, 1, 2)
plt.plot(x, z, 'r')
plt.title('sin')
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.grid()
plt.show()
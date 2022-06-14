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
a = np.tan(x)

plt.subplot(3, 1, 1)
plt.plot(x, y, 'g')
plt.title('sin')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid()
plt.show()

plt.subplot(3, 1, 2)
plt.plot(x, z, 'r')
plt.title('cos')
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.grid()
plt.show()

plt.subplot(3, 1, 3)
plt.plot(x, a, 'b')
plt.title('tan')
plt.xlabel('x')
plt.ylabel('tan(x)')
plt.grid()
plt.legend(['Tan(x)'])
plt.show()
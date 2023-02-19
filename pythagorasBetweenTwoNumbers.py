# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 18:08:25 2023

@author: Flexsidee
"""

from math import sqrt

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))

x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

result = sqrt( ((x2-x1)**2) + ((y2-y1)**2))

print("Result = "+str(result))
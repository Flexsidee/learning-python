# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 10:20:42 2023

@author: Flexsidee
"""
from random import randrange

count = 0
for x in range(10000):
    num = randrange(1, 100)
    print(f"{num}, ")
    if num % 12 == 0:
        count += 1

print(f"\n\nTotal numbers divisible by 12 = {count}")

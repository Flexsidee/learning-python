# -*- coding: utf-8 -*-
"""
prime numbers 

Created on Mon Jun 13 20:49:56 2022
@author: Flexsidee
"""

def primeNumbers(startNum, endNum):
    result = []

    for x in range(startNum, endNum):
        prime = True
        for y in range(2, x):
            if (x % y == 0 ):
                prime = False
        if prime == True:
            result.append(x)
        
    return (result)


ans = primeNumbers(1, 100)
print(ans)
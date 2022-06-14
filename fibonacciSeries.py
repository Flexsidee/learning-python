# -*- coding: utf-8 -*-
"""
implementing Fibonacci Series

Created on Mon Jun 13 20:14:44 2022
@author: Flexsidee
""" 

#creating the function
def fibonacci(n):        
    result = [0, 1]
    
    for k in range(n-2):
        fib_next = result[k+1] + result[k]
        result.append(fib_next)
    
    print(result)

fibonacci(10) #this will list fibonacci of the first 10 terms
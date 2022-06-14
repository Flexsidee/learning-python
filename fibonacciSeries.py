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
    
    return result

fib = fibonacci(10)
print(fib) #print the first 10 terms of the fibonacci series
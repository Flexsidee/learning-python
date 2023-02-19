# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 11:47:45 2022
Name:       Somade Daniel Oluwaseunfunmi
Matric No:  21/8874
Department: 300Level Computer Science
Question 1: Python program to is used to display the first 100 prime numbers 
"""

def listPrimeNumbers(maxNum): 
    for num in range(1, maxNum+1):
        count = 0
        for x in range(2, (num//2 + 1)):
            if(num % x == 0):
                count = count + 1
                break
            
        if(count == 0 and num!=1):
            print(" %d" %num, end=" ")
            
listPrimeNumbers(101)
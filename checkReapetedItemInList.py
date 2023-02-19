# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 22:29:25 2023

@author: Flexsidee
"""

def dups(lst: list):
    seen = set()
    duplicates = []
    for element in lst:
        if element in seen:
            duplicates.append(element)
        else: 
            seen.add(element)
    return duplicates
    
a = [1, 2, 2, 1, "klsjs", "klsjs", 3, 2, 4, 6, 7,6]
result = dups(a)
print(result)
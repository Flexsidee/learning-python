# -*- coding: utf-8 -*-
"""
creating multiplication table

Created on Mon Jun 13 20:35:40 2022
@author: Flexsidee
"""

def multiplicationTable(to):
    for i in range(1, to):
        for k in range(1, 13):
            res = i * k
            print(str(i) + " X " + str(k) + " = " + str(res))
        print("------")
        
multiplicationTable(10)
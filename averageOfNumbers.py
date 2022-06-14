# -*- coding: utf-8 -*-
"""
finding the average of numbers with python

Created on Mon Jun 13 20:03:49 2022
@author: Flexsidee
"""

sum = 0 #initializing the sum of the scores
scores = [71, 85, 88, 65, 81, 70, 67, 71]

length = len(scores) 

for x in scores:
    sum +=x

average = sum / length

print("The sum of the scores : " + str(sum))
print("The length of the scores: " + str(length))
print("The average of the scores : " + str(average))

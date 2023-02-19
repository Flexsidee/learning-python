# -*- coding: utf-8 -*-
"""
Name:       SOMADE DANIEL OLUWASEUNFUNMI
Matric No:  21/8874
Department: 300 LEVEL COMPUTER SCIENCE
COURSE:     CSC 301 (STRUCTURAL PROGRAMMING USING PYTHON)
Question:   Write a python program to select the menu for a fresh student at the cafetaria
"""

print("Hi there, here is a list of the foods in our menu")
print("1. Rice and Beans")
print("2. Bread and Beans")
print("3. Amala and Ewedu")
print("4. Semo and Egusi")

print("\nType the number of your selected food in the menu: ")
selectedFood = int(input())
print("")

if(selectedFood == 1):
    print("You selected Rice and Beans")
elif(selectedFood == 2):
    print("You selected Bread and Beans")
elif(selectedFood == 3):
    print("You selected Amala and Ewedu")
elif(selectedFood == 4):
    print("You selected Semo and Egusi")
    

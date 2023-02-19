"""
Created on Tue Nov 22 11:47:45 2022
Name:       Somade Daniel Oluwaseunfunmi
Matric No:  21/8874
Department: 300Level Computer Science
Question 1:Create a python function for converting between degrees and radians and vice versa 
"""

def radToDeg(rad):
    pi = 22/7
    deg = (rad * 180) / pi
    return deg

def degToRad(deg):
    pi = 22/7
    rad = (deg * pi ) / 180
    return rad



rad = 1
deg = 57.2958

print(str(rad) + "radians = " + str(radToDeg(rad)) + "degrees")
print("{}degress = {}radians".format(deg, degToRad(deg)))
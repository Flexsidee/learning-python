# This program is used to convert from radians to degree and from degrees to radians
import math

def radiansToDegrees(rad):
    return rad * (180 / math.pi)

def degreesToRadians(deg):
    return deg * (math.pi / 180)


x = radiansToDegrees(5)
y = degreesToRadians(286.4788975654116)

print(x)
print(y)
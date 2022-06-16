# Question 2: Write 84.175, -528.685, -0.000924138 and -362005 in floating point form and rounded to 5 significant digit
import math


# this function is used to round a float to the number of significant digits specified
def round_to_sf(x, sf):
    return round(x, sf - int(math.floor(math.log10(abs(x)))) - 1)


numbers = [84.175, -528.685, -0.000924138, -362005]  # this is the list of numbers to be rounded off

for i in numbers:
    res = round_to_sf(i, 5)
    print(str(i) + " to 5 significant digits = " + str(res))

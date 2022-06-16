# Question 3: Write -76.437125, 60100 and -0.00001 in floating point form rounded to 4 significant digits
import math


# this function is used to round a float to the number of significant digits specified
def round_to_sf(x, sf):
    return round(x, sf - int(math.floor(math.log10(abs(x)))) - 1)


numbers = [-76.437125, 60100, -0.00001]  # this is the list of numbers to be rounded off

for i in numbers:
    res = round_to_sf(i, 4)
    print(str(i) + " to 4 significant digits = " + str(res))

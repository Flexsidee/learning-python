# Question 1: Solve x^2 - 30x + 1 = 0 and compute your answer using 6s.f in the computation
import math


# this function is used to get the values of x in the quadratic equation using Almighty formula
def quadratic_equation(a: int, b: int, c: int):
    m = (b * b) - (4 * a * c)
    m = math.sqrt(m)
    o = ((-1 * b) + m) / (2 * a)  # returns the first value of x
    p = ((-1 * b) - m) / (2 * a)  # returns the second value of x
    return o, p


# this function is used to round a float to the number of significant digits specified
def round_to_sf(x, sf):
    return round(x, sf - int(math.floor(math.log10(abs(x)))) - 1)


# from the equation, a=1, b=-30 and c=1
x1, x2 = quadratic_equation(1, -30, 1)  # getting the values of x using the function above
print("The values of x are; " + str(x1) + " and " + str(x2))

x1 = str(round_to_sf(x1, 6))
x2 = str(round_to_sf(x2, 6))
print("The values of x to 6 significant digits are; " + x1 + " and " + x2)

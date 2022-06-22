"""
Set up an iteration process for the equation f(x) = x^2 - 3x + 1 = 0 
"""
def equation(n):
    return ((n**2) + 1 ) / 3

for i in range (0, 6):
    x = equation(i)
    print("When x base 0  = " + str(i) + ", x" + str(i) + " = " + str(x) + ", Error = " + str(i - x) )
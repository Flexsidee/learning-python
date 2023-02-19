#check if a number is a prime number or not

def isPrime1(num):
    count = 0
    for x in range(2, num):
        if(num % x == 0):
            count +=1
            break

    if(count == 0): 
        print(f"{num} is prime")
    else: 
        print(num, " is not a prime number")

def isPrime2(num):
    if(num == 2 or num == 3 or num == 5 or num == 7):
        print(f"{num} is prime")
    elif (num % 2 != 0 and num %3 != 0 and num%5 != 0 and num%7 != 0):
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")

while True:
    numSupplied = int(input("Enter number to check: "))
    isPrime1(numSupplied)
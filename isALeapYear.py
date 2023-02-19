#python program to check if a year is a leap year

year = int(input("Enter the year: "))

if(year % 4 == 0):
    print(year, " is a leap year")
else:
    print(year, " is not a leap year")
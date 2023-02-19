def numericalDifferences(x, y):
    #this function used to populate the data
    def d(data):
        newData = [] #initialise the array to be empty
        
        for i in range(len(data) -1):
            res = data[i+1] - data[i]
            newData.append(res)
            
        return newData #this will return the new list after performing the action        
    
    d1y = d(y)
    d2y = d(d1y)
    d3y = d(d2y)
    d4y = d(d3y)
    d5y = d(d4y)
    if(len(y) > 6): d6y = d(d5y)
    else:   d6y = []
        
    h = x[1] - x[0]
    
    firstDerivative = (d1y[0] - (d2y[0] / 2) + (d3y[0] / 3) - (d4y[0] / 4) + (d5y[0] /5) ) / h
    
    secondDerivate = (d2y[0] - (d3y[0] / 2) + ((11 * d4y[0]) / 12) - ((5 * d5y[0]) / 6) ) / h**2
        
    print("x = " + str(x))
    print("y = " + str(y) + "\n")
    
    print("d1y = " + str(d1y))
    print("d2y = " + str(d2y))
    print("d3y = " + str(d3y))
    print("d4y = " + str(d4y))
    print("d5y = " + str(d5y))
    print("d6y = " + str(d6y) + "\n") if(len(y) > 6) else print("d6y = [] \n")
    
    print( "\nFirst derivative = " + str(firstDerivative))
    print( "Second derivative = " + str(secondDerivate) + "\n")
    
    
question1X = [1.00, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30]
question1Y = [1.00, 1.0247, 1.0488, 1.0723, 1.0954, 1.1180, 1.1401]

question2X = [1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
question2Y = [0.0, 0.128, 0.566, 1.296, 2.432, 4.0]

print("All calulated details of question 1 is given below \n------------------------------------")
numericalDifferences(question1X, question1Y)

print("All calulated details of question 2 is given below \n----------------------------------")
numericalDifferences(question2X, question2Y)
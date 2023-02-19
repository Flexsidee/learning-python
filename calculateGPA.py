"""
python program to calculate cgpa
"""
class GPA:
    def __init__(self) -> None:
        self.num = int(input("Enter number of courses you are offering: "))
        self.calculateGPA()

    def collectNumOfCourses(self) -> None:
        self.num = int(input("Enter number of courses you are offering: "))

    def calculatePoint(self, unit, grade) -> int:
        if(grade > 69):
            point = 5 * unit
        elif(grade > 59):
            point = 4 * unit
        elif(grade > 49):
            point = 3 * unit
        elif(grade > 44):
            point = 2 * unit
        elif(grade > 39):
            point = 1 * unit
        else:
            point = 0

        return point


    def calculateGPA(self) -> None:
        totalUnit = 0
        totalPoint= 0
        for x in range(self.num):
            courseUnit = int(input(f"Enter the course {x+1} unit: "))
            coureScore = int(input(f"Enter the course {x+1} score: "))
            coursePoint = self.calculatePoint(courseUnit, coureScore)
            totalUnit += courseUnit
            totalPoint += coursePoint
        
        gpa = totalPoint/totalUnit
        print("-----------------------")
        print(f"\nThe GPA of the student is: {gpa}")

gpa = GPA()

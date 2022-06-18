class TempConverter:
    def __init__(self, value):
        self.value = value
         
    def toF(self):
        print((self.value * (9/5)) + 32)

    def toCel(self):
        print((self.value - 32) * (5/9))


temp1 = TempConverter(0)
temp1.toF() # returns 32

temp2 = TempConverter(32)
temp2.toCel() #returns 0
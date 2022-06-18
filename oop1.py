class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def displayCar(self):
        print(self.model)
        print(self.color)

car1 = Car("Ford", "Yellow")
car2 = Car("Ferrari", "Red")

car1.displayCar()
car2.displayCar()

car2.color = "Indigo"

car2.displayCar()
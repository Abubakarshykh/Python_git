class Car:
    def __init__(self, name, model, color):  # constructor
        self.__name = name
        self.__model = model
        self.__color = color

    def getname(self):
        return self.__name

    def getmodel(self):
        return self.__model

    def getcolor(self):
        return self.__color

# ✅ Object creation and print statements must be OUTSIDE the class
c = Car("Honda Civic", 2020, "White")
a = c.getname()
b = c.getmodel()
q = c.getcolor()

print("Car name is:", a, "model is:", b, "and with color is:", q)

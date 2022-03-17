
class Car:

    typ = "osobowy"

    def __init__(self, name, number=0):
        print("Jestem w konstruktorze")
        self.name = name
        self.fuel = 10
        #self.__ukryty_ = "atrybut ukryty"

    def drive(self):
        print("jadę")
        self.fuel -= 1

    def factory_example():
        a = Car("Fiat")
        return a

class Truck(Car):
    def __init__(self, name, number=0):
        super().__init__(name, number)
        print("Jestem w konstruktorze truck")
        self.load = 5

    def unload(self):
        self.load = 0

    def __repr__(self):
        return f"Samochód marki {self.name}"

x = Truck("opel")
y = Truck("ford")
z = Truck.factory_example()


print(x)
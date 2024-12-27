from numpy.testing.print_coercion_tables import print_new_cast_table

from Data_structures_and_algorithms_neetcode import Animal


class Animal:
    def sound(self):
        return "Make some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.sound())


#Python Data Abstraction
from abc import ABC, abstractmethod #Importing ABC and abstract method
class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    @abstractmethod
    def PrintDetails(self): #Creating an abstract method
        pass

    def accelerate(self): #Creating a concrete method
        print("speed up...")
    def breaks_applied(self):
        print("Car stopped")

class Hatchback(Car): #Creating a child class
    def PrintDetails(self):
        print("Brand: ", self.brand)
        print("Model: ", self.model)
        print("Year :", self.year)

    def sunroof(self):
        print("Not having this feature.")

class Suv(Car): #Creating a child class
    def PrintDetails(self):
        print("Brand: ", self.brand)
        print("Model: ", self.model)
        print("Year :", self.year)

    def sunroof(self):
        print("Available")

car1 = Hatchback("Maruti", "Alto", "2022")
print(car1.PrintDetails())
print(car1.sunroof())


car2 = Suv("Mazda", "cx 5", "2025")
print(car2.PrintDetails())
print(car2.sunroof())






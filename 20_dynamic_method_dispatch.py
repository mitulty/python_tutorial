# -*- coding: utf-8 -*-
# @Author: Mitul Tyagi
# @Date:   2024-12-05 23:48:51
# @Description: Dynamic Method Dispatch
'''
- Dynamic method dispatch, also known as runtime polymorphism, is a feature in Python that allows to invoke a method on an object, and the method that 
  gets executed is determined at runtime based on the actual type of the object. This enables to create more flexible and extensible code by using 
  inheritance and method overriding.
- Inheritance: Dynamic method dispatch relies on inheritance. There is a super class (base class) and one or more subclasses (derived classes) that inherit
  from the super class.
- Method Overriding: To achieve dynamic method dispatch, a method must be overriden in a subclass. In other words, a method must be defined with the same 
  name and parameters as the method in the superclass.
- Polymorphism: The superclass reference can be used to refer to an object of any subclass. This is possible due to polymorphism. 
- Dynamic method dispatch is resolved at runtime based on the object's actual type, allowing for polymorphism and method overriding.
- Dynamic method dispatch allows to call methods of different derived classes through a shared base class interface. It enables to write code that can 
  work with various derived class objects using a common interface, making code more adaptable and extensible.
- If the subclass does not override a method from the superclass, the method in the superclass is called when the method is invoked on an object of the 
  subclass.
'''
class Animal:
    def make_sound(self):
        print("Some generic animal sound")


class Dog(Animal):
    def make_sound(self):
        print("Bark")


class Cat(Animal):
    def make_sound(self):
        print("Meow")


my_animal = Animal()
my_animal.make_sound()  # Calls the make_sound method of the Animal class

my_animal = Dog()
my_animal.make_sound()  # Calls the make_sound method of the Dog class

my_animal = Cat()
my_animal.make_sound()  # Calls the make_sound method of the Cat class

class Shape:
    def __init__(self):
        self.area = 0

    def print_area(self):
        print("Area:", self.area)


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
        self.area = self.length * self.width

    def print_area(self):
        print("Rectangle Area:", self.area)


s = None
r = Rectangle(4, 6)

s = r
s.print_area()

class Employee:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print("Name:", self.name)


class Worker(Employee):
    def __init__(self, name, hourly_rate):
        super().__init__(name)
        self.hourly_rate = hourly_rate

    def display_info(self):
        super().display_info()  # Call the base class method
        print("Hourly Rate: $" + str(self.hourly_rate))


# take input
name = "Jim" #input()
hourly_rate = 28 #int(input())


# Create object of Worker class
worker = Worker(name, hourly_rate)

# Use dynamic method dispatch to display worker information
worker.display_info()

def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()

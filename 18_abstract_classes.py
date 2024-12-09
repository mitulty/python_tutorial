# -*- coding: utf-8 -*-
# @Author: Mitul Tyagi
# @Date:   2024-12-05 23:48:51
# @Description: Abstract Classes
'''
- In Python, an abstract class is a class that cannot be instantiated on its own and is meant to be subclassed by other classes. Abstract 
  classes are created using the abc (Abstract Base Classes) module. Abstract classes may contain abstract methods, which are methods that are 
  declared in the abstract class but don't have an implementation. Subclasses of the abstract class are required to provide implementations for
  these abstract methods. Key points about abstract classes in Python:
    -> Abstract classes cannot be instantiated directly.
    -> Abstract methods are declared using the @abstractmethod decorator in the abstract class.
    -> Subclasses must provide concrete implementations for all abstract methods to be considered valid.
    -> Abstract classes can contain both abstract and non-abstract methods.
- The primary purpose of  abstract method in Python is to declare a function that has no implementation in the abstract class itself but must 
  be implemented by any derived classes. It enforces that derived classes provide their own implementations for the function.
- An abstract class in Python can have constructors. Abstract classes, like any other classes, can have an __init__ method or any other method,
  but it doesn't affect their abstract nature. Subclasses that inherit from the abstract class must still provide concrete implementations for 
  any abstract methods, including the constructor if it's declared in the abstract class.
- Abstract methods in an abstract class are declared using the `@abstractmethod` decorator in Python. This decorator indicates that the method 
  is meant to be overridden by concrete subclasses.
'''
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

# Example usage:
circle = Circle(radius=5)
square = Square(side_length=4)

print("Circle Area:", circle.area())          # Output: 78.5
print("Square Area:", square.area())            # Output: 16


class Vehicle(ABC):
    def __init__(self, n):
        self.name = n

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def __init__(self, n):
        super().__init__(n)

    def start_engine(self):
        print("Car engine started for " + self.name + ".")


car_name = "Nano"

my_car = Car(car_name)
my_car.start_engine()

from abc import ABC, abstractmethod

class TextFormatter(ABC):
    @abstractmethod
    def format(self, text):
        pass

class UpperCaseFormatter(TextFormatter):
    # Write your code here
    def format(self,text):
        return text.upper()

class ReverseFormatter(TextFormatter):
    # Write your code here
    def format(self,text):
        return text[::-1]
    


text = "Codechef"

# Format the text using UpperCaseFormatter
formatter = UpperCaseFormatter()
print(formatter.format(text))

# Format the text using ReverseFormatter
formatter = ReverseFormatter()
print(formatter.format(text))

from abc import ABC, abstractmethod

# Abstract base class Shape
class Shape:
    # Abstract method for calculating area
    @abstractmethod
    def calculate_area(self):
        pass

# Derived class Square
class Square(Shape):
    def __init__(self, side_length):
        self.side = side_length

    # Implementation of calculate_area for Square
    def calculate_area(self):
        return self.side * self.side

# Derived class Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Implementation of calculate_area for Rectangle
    def calculate_area(self):
        return self.length * self.width


square_side = 35 # int(input())
rectangle_length, rectangle_width = 13, 56 #list(map(int,input().split()))

# Create a Square with a side length
square = Square(square_side)

# Create a Rectangle with length and width
rectangle = Rectangle(rectangle_length, rectangle_width)

# Calculate and display the areas
print(square.calculate_area())
print(rectangle.calculate_area())

def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()

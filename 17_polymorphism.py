# -*- coding: utf-8 -*-
# @Author: Mitul Tyagi
# @Date:   2024-12-05 23:48:51
# @Description: Inheritance
'''
- Polymorphism is a fundamental concept in object-oriented programming that allows objects of different types to be treated as objects of a 
  common base type. It enables flexibility in code design and promotes code reuse. Polymorphism enhances the flexibility and reusability of 
  code in Python, making it a powerful feature of object-oriented programming.
- There are two types of polymorphism:
  -> Compile-time Polymorphism (Static Binding or Method Overloading)
  -> Run-time Polymorphism (Dynamic Binding or Method Overriding)
- A subclass can provide a specific implementation for a method that is already defined in its superclass. This allows objects of the derived 
  class to be used interchangeably with objects of the base class.

- In Python, method overloading with different parameter lists, as found in some other languages like Java or C++, is not directly supported. 
  However, to achieve similar functionality default parameter values or variable-length argument lists are used. Constructors in Python can't 
  be overloaded just like the regular methods in the class.
- Function overloading in Python allows a function to have multiple implementations with different parameter lists. This promotes code 
  reusability and flexibility by providing different ways to call the same function based on the provided arguments.

- Method overriding is a concept in object-oriented programming where a subclass provides a specific implementation for a method that is already
  defined in its superclass. This allows the subclass to provide a specialized behavior while still maintaining the same method signature as 
  the superclass. In Python, method overriding is achieved by creating a method in the subclass with the same name as the method in the 
  superclass. Key points are:
  -> The overridden method in the subclass must have the same name and parameters as the method in the superclass.
  -> Method overriding is a form of run-time polymorphism, and the specific implementation to be called is determined at runtime based on the 
     type of the object.
  -> The super() function can be used to call the overridden method from the superclass within the overridden method of the subclass if needed.
- The subclass method must have the same name and a compatible method signature (including the same number and types of parameters) as the 
  superclass method. The specific implementation of an overridden method is determined at runtime based on the type of the object. The super() 
  keyword is used to call the overridden method from the superclass within the overridden method of the subclass.

'''
class MyClass:
# This will result in an error in Python
    # def add(self, a, b):
    #     return a + b

    # def add(self, a, b, c):
    #     return a + b + c
    def add(a, b, c=None):
        if(c):
            return a+b+c 
        else:
            return a+b 

class Animal:
    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Example usage of method overriding
dog = Dog()
cat = Cat()

print(dog.make_sound())  # Output: Woof!
print(cat.make_sound())  # Output: Meow!

### Method Overloading
## Using Default Paramters
class MyClass:
    def add(self, a, b=0, c=0):
        return a + b + c

# Creating an instance of MyClass
my_object = MyClass()

# Calling the add method with different parameter lists
result1 = my_object.add(1)
result2 = my_object.add(1, 2)
result3 = my_object.add(1, 2, 3)

print(result1)  # Output: 1
print(result2)  # Output: 3
print(result3)  # Output: 6

## Using Variable-Length Arguent Lists
class MyClass:
    def add(self, *args):
        return sum(args)

# Creating an instance of MyClass
my_object = MyClass()

# Calling the add method with different numbers of arguments
result1 = my_object.add(1)
result2 = my_object.add(1, 2)
result3 = my_object.add(1, 2, 3)

print(result1)  # Output: 1
print(result2)  # Output: 3
print(result3)  # Output: 6

import functools

class Calculator:

    # Complete the method to multiply integers
    def multiply(self, *args):
        if(len(args) == 0):
            raise ArithmeticError
        else:
            return functools.reduce(lambda x,y : x*y ,args)


calculator = Calculator()

# Using the different overloaded add methods
mul1 = calculator.multiply(2, 3)
mul2 = calculator.multiply(2, 3, 4)
mul3 = calculator.multiply(2, 3, 4, 5)

print("Multiplication1:", mul1)
print("Multiplication2:", mul2)
print("Multiplication3:", mul3)

class ShapeCalculator:
    # Calculate the area of shapes
    @staticmethod
    def calculate_area(length, width=-1):        
        return length * length if width == -1  else length * width


# Taking input from the user
square_side = 4 #int(input())
length, width  = (4,6) #map(int, input().split())

# Calculate the area of a square
square_area = ShapeCalculator.calculate_area(square_side)
# Calculate the area of a rectangle
rectangle_area = ShapeCalculator.calculate_area(length, width)

# Print the results
print(square_area)
print(rectangle_area)


### Method Overriding
class Animal:
    def make_sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def make_sound(self):
        print("Dog barks")

class Cat(Animal):
    def make_sound(self):
        print("Cat meows")


generic_animal = Animal()
dog = Dog()
cat = Cat()

generic_animal.make_sound()
dog.make_sound()
cat.make_sound()

class Shape:
    def calculate_area(self):
        return 0

    def calculate_perimeter(self):
        return 0


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width         

    def calculate_perimeter(self):
        return 2*(self.length + self.width)    
    

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side         


    def calculate_perimeter(self):
        return 2*(self.side + self.side)    



rectangle = Rectangle(4, 6)
square = Square(5)

rectangle_area = rectangle.calculate_area()
rectangle_perimeter = rectangle.calculate_perimeter()
square_area = square.calculate_area()
square_perimeter = square.calculate_perimeter()

print("Rectangle Area:", rectangle_area)
print("Rectangle Perimeter:", rectangle_perimeter)
print("Square Area:", square_area)
print("Square Perimeter:", square_perimeter)

class Vehicle:
    def accelerate(self):
        print("The vehicle accelerates.")


class Car(Vehicle):
    def __init__(self, initial_speed):
        super().__init__()
        self.speed = initial_speed

    def accelerate(self):
        self.speed += 10
        print(f"The car accelerates. Current speed: {self.speed} km/h")


class Bicycle(Vehicle):
    def __init__(self, initial_speed):
        super().__init__()
        self.speed = initial_speed

    def accelerate(self):
        self.speed += 5
        print(f"The bicycle accelerates. Current speed: {self.speed} km/h")



car = Car(20)  # Initial speed of the car is 20 km/h
bicycle = Bicycle(15)  # Initial speed of the bicycle is 15 km/h

car.accelerate()  # Accelerate the car
bicycle.accelerate()  # Accelerate the bicycle

class Vehicle:
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate

    def calculate_rental_cost(self, days):
        # Default calculation based on rental rate
        return days * self.rental_rate


class Car(Vehicle):
    def __init__(self, model, rental_rate, seats):
        super().__init__(model, rental_rate)
        self.seats = seats

    def calculate_rental_cost(self, days):
        # Override the method to calculate cost based on seats, days, and rental rate
        return self.seats * days * self.rental_rate
        # return self.seats * super().calculate_rental_cost(days)


# Write your code here
# Read input
model =  "Beat" #input()
rental_rate, seats, num_rental_days = (10, 5, 4) # map(int, input().split())

# Create a Car object
car = Car(model,rental_rate,seats)

# Calculate and display the rental cost
print("Rental Cost: ",car.calculate_rental_cost(num_rental_days))

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def get_book_info(self):
        return f'Title: "{self.title}", Author: {self.author}, Price: ${self.price}'

class FictionBook(Book):
    def __init__(self, title, author, price, genre):
        super().__init__(title, author, price)
        self.genre = genre

    def get_book_info(self):
        return f'{super().get_book_info()}, Genre: {self.genre}'


class NonFictionBook(Book):
    def __init__(self, title, author, price, topic):
        super().__init__(title, author, price)
        self.topic = topic

    def get_book_info(self):
        return f'{super().get_book_info()}, Topic: {self.topic}'


fiction_book = FictionBook("To Kill a Mockingbird", "Harper Lee", 14.99, "Drama")
non_fiction_book = NonFictionBook("A Brief History of Time", "Stephen Hawking", 19.99, "Cosmology")

# Display book information
print("Book Info:", fiction_book.get_book_info())
print("Book Info:", non_fiction_book.get_book_info())

def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()

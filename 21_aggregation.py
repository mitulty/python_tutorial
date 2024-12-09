# -*- coding: utf-8 -*-
# @Author: Mitul Tyagi
# @Date:   2024-12-05 23:48:51
# @Description: Aggregation
'''
- Aggregation is a form of object composition in which one class contains or is composed of one or more objects of another class. Aggregation represents 
  a "has-a" relationship between classes. It implies that one class (the whole or container) has objects of another class (the part or component). It
  enables the creation of complex objects by combining simpler objects.
- In Python, objects can be passed as parameters to functions or methods, allowing to manipulate or interact with those objects within the function. When 
  an object is passed as a parameter, the function receives a reference to the object, allowing it to access and modify the object's attributes.
- 
'''

class Address:
    def __init__(self, street, city, postal_code):
        self.street = street
        self.city = city
        self.postal_code = postal_code

    def display_address(self):
        print("Street:", self.street, ", City:", self.city, ", Postal Code:", self.postal_code)


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_info(self):
        print("Name:", self.name, ", Age:", self.age)
        print("Address:", end=" ")
        self.address.display_address()


person_address = Address("123 Main St", "Cityville", "12345")
person = Person("John Doe", 30, person_address)

person.display_info()

class Wheel:
    def __init__(self, wheel_type):
        self.type = wheel_type

    def print_type(self):
        print("Wheel Type:", self.type)

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.front_left_wheel = Wheel("Front Left")
        self.front_right_wheel = Wheel("Front Right")
        self.rear_left_wheel = Wheel("Rear Left")
        self.rear_right_wheel = Wheel("Rear Right")

    def print_info(self):
        print(f"Make: {self.make}, Model: {self.model}")
        self.front_left_wheel.print_type()
        self.front_right_wheel.print_type()
        self.rear_left_wheel.print_type()
        self.rear_right_wheel.print_type()


my_car = Car("Toyota", "Camry")
my_car.print_info()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


def print_person_info(p):
    print("Name:", p.get_name())
    print("Age:", p.get_age())


# Create a Person object
person = Person("Alice", 30)

# Call a method and pass the object as a parameter
print_person_info(person)

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width


# Method to calculate the area of a Rectangle object
def calculate_area(rect):
    # Write your code here
    return rect.length * rect.width
    
    
# Create a Rectangle object
rectangle = Rectangle(5, 3)

# Calculate and print the area of the rectangle
area = calculate_area(rectangle)
print("Area of the rectangle:", area)


class Circle:
    def __init__(self, radius):
        self.radius = radius

def modify_circle(circle):
    circle.radius = 10.0


my_circle = Circle(5.0)
print("Before: Radius =", my_circle.radius)
modify_circle(my_circle)
print("After: Radius =", my_circle.radius)

class Course:
    def __init__(self, course_name):
        self.course_name = course_name


class Student:
    def __init__(self, student_name):
        self.student_name = student_name
        self.courses = []

    def list_enrolled_courses(self):
        for course in self.courses:
            print(course.course_name, end=" ")
        print()


course1 = Course("Introduction to Programming")
course2 = Course("Data Structures")

student1 = Student("Alice")
student2 = Student("Bob")

student1.courses.extend([course1, course2])
student2.courses.append(course1)

print("Courses enrolled by Alice:", end=" ")
student1.list_enrolled_courses()

print("Courses enrolled by Bob:", end=" ")
student2.list_enrolled_courses()

def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()

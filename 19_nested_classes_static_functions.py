# -*- coding: utf-8 -*-
# @Author: Mitul Tyagi
# @Date:   2024-12-05 23:48:51
# @Description: Nested Classes and Static Functions
'''
- In Python, an inner class is a class that is defined inside another class. Inner classes are sometimes referred to as nested classes. Inner 
  classes can be useful for organizing code, encapsulating functionality, and maintaining a clear structure within a class. Inner classes have 
  access to the attributes and methods of the outer class. Key points about inner classes in Python:
    -> Inner classes are defined within the scope of the outer class.
    -> Inner classes can access the attributes and methods of the outer class.
    -> An instance of the inner class is typically created using an instance of the outer class.
    -> Inner classes are useful for encapsulating related functionality and maintaining a clean class structure.
- In Python, the return statement can be used to return the created object from the function. The primary advantage of using static functions 
  to create objects in Python is that it provides a centralized and controlled way to create objects within a class. This approach encapsulates 
  object creation details, promotes abstraction, allows for validation and customization, and simplifies object creation for users of the class.
- 
'''

class OuterClass:
    def __init__(self, outer_attr):
        self.outer_attr = outer_attr

    def outer_method(self):
        print("This is an outer method.")

    class InnerClass:
        def __init__(self, inner_attr):
            self.inner_attr = inner_attr

        def inner_method(self):
            print("This is an inner method.")

# Creating an instance of the outer class
outer_instance = OuterClass(outer_attr="Outer Attribute")

# Creating an instance of the inner class using the outer class instance
inner_instance = outer_instance.InnerClass(inner_attr="Inner Attribute")

# Accessing attributes and methods
print(outer_instance.outer_attr)  # Output: Outer Attribute
outer_instance.outer_method()      # Output: This is an outer method.

print(inner_instance.inner_attr)  # Output: Inner Attribute
inner_instance.inner_method()      # Output: This is an inner method.


class School:
    class Student:
        def __init__(self, name):
            self.name = name

        def display(self):
            print(self.name)

    def __init__(self, school_name, student):
        self.school_name = school_name
        self.student = student

    def display_school_info(self):
        print(self.school_name)
        self.student.display()

## Creating an inner/nested class object from the outter class
student = School.Student("Alice")
school = School("ABC School", student)

school.display_school_info()

## Methods returning objects.
class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def add(self, other):
        result_real = self.real + other.real
        result_imaginary = self.imaginary + other.imaginary
        return Complex(result_real, result_imaginary)


num1 = Complex(2.5, 3.0)
num2 = Complex(1.0, -1.5)

result = num1.add(num2)

print("Result: {} + {}i".format(result.real, result.imaginary))

class Name:
    def __init__(self):
        self.name = None  # Data member to store a name

    @staticmethod
    def concatenate_names(obj1, obj2):
        # Create a new Name object and set its name data member to the concatenated result
        result = Name()
        result.name = obj1.name + " " + obj2.name
        return result



# Create an instance of the Name class and set the name data member
name1 = Name()
name1.name = "Tom"

# Create another instance of the Name class and set the name data member
name2 = Name()
name2.name = "Jerry"

# Use the concatenate_names static method to concatenate the names
concatenated_name = Name.concatenate_names(name1, name2)
# Display the concatenated name using the name data member of the result
print(concatenated_name.name)



class Person:
    def __init__(self, name):
        self.name = name

    def create_person(self, new_name):
        return Person(new_name)


person = Person("Alice")
new_person = person.create_person("Bob")

print("Original Person's Name:", person.name)
print("New Person's Name:", new_person.name)

class Student:
    class Course:
        def __init__(self):
            self.course_name = ""

        def set_data(self, course_name):
            self.course_name = course_name

        def display(self):
            print(self.course_name)

    def __init__(self, name, course_name):
        self.name = name
        self.course = self.Course()
        self.course.set_data(course_name)

    def display(self):
        print(self.name)
        self.course.display()


# Take inputs
name, course_name = "Alice", "Geology" #input().split()

# Create a student and a course
student = Student(name, course_name)
course = student.Course()
course_another = Student.Course()
# Display student's name and course name
student.display()
course.display() # A new object created.
course_another.display() 

class Calculator:
    # Constructor to initialize the result to zero
    def __init__(self):
        self.result = 0

    # Method to set the result
    def set_result(self, value):
        self.result = value

    # Method to get the current result
    def get_result(self):
        return self.result        

    # Method to add two Calculator objects and return the result as a new Calculator object
    def add(self, other):
        sum_two_objects = self.result + other.result
        sum_obj = Calculator()
        sum_obj.set_result(sum_two_objects)
        return sum_obj
        


calc_a = Calculator()
calc_b = Calculator()

value_a, value_b = 12, 13 #list(map(int,input().split()))

calc_a.set_result(value_a)
calc_b.set_result(value_b)
result_calc = calc_a.add(calc_b)

print(result_calc.get_result())


def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()

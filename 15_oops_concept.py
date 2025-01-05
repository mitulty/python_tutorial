# -*- coding: utf-8 -*-
# @Author: Mitul Tyagi
# @Date:   2024-12-05 23:48:51
# @Description: OOP Concepts
'''
- Object-oriented programming aims to implement real-world entities like inheritance, hiding, polymorphism, etc. in programming. The main aim 
  of OOPs is to bind together the data and the functions that operate on them so that no other part of the code can access this data except those
  functions. It is an approach for modeling concrete, real world things. OOP models real-world entities as software objects that have some data 
  associated with them (also knwon as attributes) and can perform certain operations (called methods).
- Object-oriented programming (OOP) is a method of structuring a program by bundling related properties and behaviors into individual objects.
- Object-oriented programming is a programming paradigm that provides a means of structuring programs so that properties and behaviors are 
  bundled into individual objects. For example, an object could represent a person with properties like a name, age, and address and behaviors 
  such as walking, talking, breathing, and running. 
- Almost everything in Python is an object, with its properties and behaviors. A Class is like an object constructor, or a "blueprint" for 
  creating objects. 
- Classes allow to create user-defined data structures. Classes define functions called methods, which identify the behaviors and actions that 
  an object created from the class can perform with its data. A class is a blueprint for how to define something. It doesn't actually contain 
  any data. While the class is the blueprint, an instance is an object that's built from a class and contains real data. Attributes depict the 
  properties of an object. An instance attribute's value is specific to a particular instance of the class. On the other hand, class attributes 
  are attributes that have the same value for all class instances.
- An instance variable in Python is a variable that is defined within a class but outside any method. It is associated with a specific instance
  (object) of the class, meaning each instance of the class can have its own unique value for that variable.
- Python class names are written in CapitalizedWords notation by convention.
- Instance methods are functions that are defined inside a class and can only be called on an instance of that class. Just like .__init__(), an
  instance method always takes self as its first parameter.
- Writing a class in Python involves defining the structure and behavior of objects based on the principles of object-oriented programming. 
- Methods like .__init__() and .__str__() are called dunder methods because they begin and end with double underscores.
- The __init__ method is a special method that serves as the constructor. It is called when an object of the class is created. It initializes 
  the instance attributes. In our example, name and age are instance attributes.
- Attributes are variables that store data related to an instance of a class.
- Methods are functions defined within a class and operate on the instance of the class.
- An instances of a class can be created by calling the class name as if it were a function. This creates a new object with its own set of 
  attributes.
- Once instances are created, the code can access their attributes using dot notation (object.attribute).
- The self parameter in Python is a convention that represents the instance of the class. It is the first parameter in instance methods and is 
  automatically passed when calling the method.
- In Python, class declaration is done using the keyword class, followed by the class name. Python does not require explicit access modifiers 
  like "public." By default, all attributes and methods in a class are public
- In Python, access modifiers are used to control the visibility and accessibility of attributes and methods within a class. Python does not 
  have explicit keywords like "public," "private," or "protected". Instead, It relies on naming conventions to indicate the intended visibility 
  like-
    -> Public: By default, all attributes and methods in a class are considered public. They can be accessed and modified from outside the class.
    -> Protected: Attributes and methods intended for internal use within the class and its subclasses are often marked as protected by 
                  prefixing them with a single underscore (_).
    -> Private: Attributes and methods that should not be accessed from outside the class are conventionally marked as private by prefixing them
                with a double underscore (__).
- In Python, getter and setter methods are used to access and modify private data members(fields) of a class.
- Getter Method: A getter method allows you to retrieve the value of a private field.
- Setter Method: A setter method allows you to modify the value of a private field.

- In Python, a constructor is a special method that gets called when an object is created. Constructors are used to initialize the attributes 
  of an object. In Python, there are two types of constructors:
  -> Default Constructor (or __init__ method): It is automatically called when an object is created.
  -> Parameterized Constructor: A parameterized constructor allows to pass values to the constructor when creating an object. It allows to 
     initialize the attributes with the values provided during object creation.
  If a specific constructor is not defined in a class, the default constructor (with no parameters) is called automatically during object 
  creation.

- A copy constructor is a special constructor that creates a new object by copying the attributes of an existing object. In Python, it is 
  implemented using a special method called __copy__. 
- Static Variables (Class Attributes): In Python, class attributes can be used to simulate static variables shared among all instances of a 
  class.
- Python has three types of methods:
    -> Instance methods- These methods are associated with a specific instance of a class and can modify the data stored within that instance. They
                         can access both instance-specific data and class-level data. Instance methods are the most common type of method in 
                         Python classes. 
    -> Class methods - These methods are associated with the class rather than an instance and can access and modify class-level data. A class 
                       method does not require a specific instance.
    -> Static methods - These methods are similar to functions outside of the class and cannot access any instance or class data. They work like
                       regular functions but belong to the class's (and every instance's) namespace. 

- Static Methods: The @staticmethod decorator are used to define static methods that don't require access to the instance. Static methods do 
  not have access to instance-specific data and are called on the class rather than an instance. In Python, a static method is a method that 
  belongs to the class rather than to any specific instance of the class. A static method can be called on the class itself, without creating 
  an instance of the class. Static methods are commonly used for utility functions or operations that do not depend on the state of any 
  particular object.
- The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
- del keyword can be used to delete properties on objects. Also the entire object can be deleted using del keyword.

- All classes have a function called __init__(), which is always executed when the class is being initiated.
- The __str__() method controls what should be returned when the class object is represented as a string. If the __str__() function is not set,
  the string representation of the object is returned.
- The __del__() method is a known as a destructor method in Python. It is called when all references to the object have been deleted i.e when an 
  object is garbage collected. 
- The __dict__() methods gives the information about the attributes and methods of a class or an object.
'''
print("-----------------------------------Employee Class Example-------------------------------------------")
class Employee:
    country = "India" # static variables/ class attributes
    count = 0 # static variables/ class attributes
    def __init__(self, name, age):
        # self.__name =  name # This makes the name as a private instance attribute which can not be accessed outside the class. Line 108 will give an error.
        self.name =  name # instance attributes
        self._age = age # instance attributes
        Employee.count +=1
        
  # Instance method
    def description(self):
        return f"{self.name} is {self._age} years old"

    # Another instance method
    def from_country(self):
        return f"{self.name} is from {self.country}"
    
employ1 = Employee("Balram", 35)


print(Employee, "Name: ", employ1.name, "; Age: ",employ1._age, "; Origin: ",employ1.country)
print(employ1.description())
print(employ1.from_country())
print(Employee.description(employ1))

employ1.country = "Japan" # This creates a new instance attribute for employ1
Employee.country = "China" # This changes the country for all the instances to China
print(employ1.__dict__)
print(Employee.__dict__)

employ2 = Employee("Mohan",32)
print(employ2.__dict__) # This does not have an instance attribute named country
print(employ2.country) # Takes the class attributes
print("Total number of employees: ", Employee.count)

print("-----------------------------------Student Class Example-------------------------------------------")
class Student:
    __age = None
    def __init__(self,age):
        self.__age = age

# Creating object of Student class
s = Student(20)
# print(s.__age) # Error as __age is a private attribute and can not be accessed directly.

print("-----------------------------------MyClass Class Example-------------------------------------------")
class MyClass :
    __myField = None
    
    # Getter method for myField
    def getMyField(self): 
        return MyClass.__myField

    # Setter method for myField
    def setMyField(self , value): 
        MyClass.__myField = value


obj = MyClass()
# Using the setter method to set the value of myField
obj.setMyField(42)
# Using the getter method to retrieve the value of myField
value = obj.getMyField()
print("Value of myField: ", value)

print("-----------------------------------BankAccount Class Example-------------------------------------------")
class BankAccount :
    # Class Attributes/ Static Variables
    __accountNumber = None
    __accountHolder = None
    __balance = None
    
    def __init__(self, accountNumber, accountHolder): 
        # self is not used as these are class attributes. Using self will create instance attributes and the class attributes will not be updated.
        BankAccount.__accountNumber = accountNumber
        BankAccount.__accountHolder = accountHolder
        BankAccount.__balance = 0
    
    #setter
    def deposit(self , value): 
        BankAccount.__balance += value
        print(f"Deposited: ${value}")

    #setter    
    def withdraw(self , value): 
        BankAccount.__balance -= value
        print(f"Withdrawn: ${value}")

    #getter
    def getAccountInfo(self):
        print(f"Account Number: {BankAccount.__accountNumber}");
        print(f"Account Holder: {BankAccount.__accountHolder}");
        print(f"Balance: ${BankAccount.__balance}"); 

# Create a BankAccount object
account = BankAccount(12345, 'John Doe')

# Perform deposits and withdrawals and display account info
account.deposit(1000)
account.withdraw(500)
account.deposit(200)

# Display the final account information
account.getAccountInfo()

print("-----------------------------------Counter Class Example-------------------------------------------")
class Counter:
    __count = None
    
    def __init__(self, value):
        self.__count = value
    
    #Setter Function
    def increment(self):
        self.__count += 1
    
    # Getter Function
    def getCount(self): 
        return self.__count
    
    #Class Method
    @classmethod
    def print_class_attr(cls):
      print(cls.__count)
        
c1 = Counter(5)
c2 = c1 # Both c1 and c2 reference the same Counter object.

c1.increment()

print(c2.getCount())
Counter.print_class_attr()

print("-----------------------------------Rectangle Class Example-------------------------------------------")
class Rectangle:
    def __init__(self):
        self.length = 0
        self.breadth = 0

    def area(self):
        print(self.length * self.breadth)

    def perimeter(self):
        print(2 * (self.length + self.breadth))

r = Rectangle()

r.length =  10 #int(input())
r.breadth = 23 #int(input())

r.area()
r.perimeter()

print("-----------------------------------MyClass Class Example-------------------------------------------")
# Copy Constructor
class MyClass:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    # Copy constructor
    def __copy__(self):
        # new_object = type(self)(self.attribute1, self.attribute2) # This will also work
        new_object = MyClass(self.attribute1,self.attribute2)
        return new_object

# Creating an object of MyClass
original_obj = MyClass("value1", "value2")

# Using the copy constructor to create a new object
copied_obj = original_obj.__copy__()

#This is a shallow Coppy
print(id(copied_obj),id(original_obj))
print(id(copied_obj.attribute1),id(original_obj.attribute1))
# Displaying the attributes of the original and copied objects
print("Original Object: attribute1={}, attribute2={}".format(original_obj.attribute1, original_obj.attribute2))
print("Copied Object: attribute1={}, attribute2={}".format(copied_obj.attribute1, copied_obj.attribute2))

original_obj.attribute1 += "new value"
# Displaying the attributes of the original and copied objects
print("Original Object: attribute1={}, attribute2={}".format(original_obj.attribute1, original_obj.attribute2))
print("Copied Object: attribute1={}, attribute2={}".format(copied_obj.attribute1, copied_obj.attribute2))
print(id(copied_obj.attribute1),id(original_obj.attribute1))

print("-----------------------------------MyClass Class Example-------------------------------------------")
class MyClass:
    static_variable = 0
    # These will not work
    # __static_variable = 0
    # _static_variable = 0
    def __init__(self, value):
        self.value = value
        MyClass.static_variable += 1

# Accessing the static variable
print(MyClass.static_variable)
var = MyClass(13)
print(MyClass.static_variable)

print("-----------------------------------MyClass Class Example-------------------------------------------")
class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method.")

# Calling the static method
MyClass.static_method()

print("-----------------------------------BankAcount Class Example-------------------------------------------")
class BankAccount:
    total_balance = 0

    def __init__(self, amount):
        self.balance = amount
        BankAccount.total_balance += amount


amount1, amount2 = (10000,20000) #map(int, input().split())

account1 = BankAccount(amount1)
account2 = BankAccount(amount2)

print(BankAccount.total_balance)

print("-----------------------------------MathUtils Class Example-------------------------------------------")
class MathUtils:
    @staticmethod
    def square(num):
        return num * num

    @staticmethod
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * MathUtils.factorial(n - 1)


# Call the static methods directly using the class name
squared_value = MathUtils.square(5)
print("Square of 5 is:", squared_value)

factorial_value = MathUtils.factorial(5)
print("Factorial of 5 is:", factorial_value)

print("-----------------------------------Circle Class Example-------------------------------------------")
class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def get_area(self):
        return 3.14159 * self.radius * self.radius


# Create a circle using no parameter
c1 = Circle()
print("The area of circle c1 is", c1.get_area())

# Create a circle using one parameter
c2 = Circle(5.0)
print("The area of circle c2 is", c2.get_area())

print("-----------------------------------Cricket Class Example-------------------------------------------")
### Methods in Python Classes.
# instance methods
class Cricket:
    teamName = None

    def setTeamName(self, name):
        self.teamName = name
    
    def getTeamName(self):
        return self.teamName

c = Cricket()
c.setTeamName('India')
print(c.getTeamName())
print(Cricket.teamName)
print("-----------------------------------Cricket Class Example-------------------------------------------")
# class method
class Cricket:
  teamName = 'India'

  @classmethod
  def getTeamName(cls):
    return cls.teamName

c = Cricket()
print("Class Method using object: ",c.getTeamName())
print("Class Method using class: ",Cricket.getTeamName())
# print("Class Method using class: ",Cricket.getTeamName(c)) ## error

print("-----------------------------------Cricket Class Example-------------------------------------------")
# static method
class Cricket:
    teamName = 'India'  

    @staticmethod
    def utility():
        print("This is a static method.")

c1 = Cricket()
c1.utility()

Cricket.utility()

print("-----------------------------------Employee Class Example-------------------------------------------")
# Python program to illustrate destructor
class Employee:

    # Initializing
    def __init__(self):
        print('Employee created.')

    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, Employee deleted.')

obj = Employee()
del obj

print("-----------------------------------RecursiveFunction Class Example-------------------------------------------")

class RecursiveFunction:
    def __init__(self, n):
        self.n = n
        print("Recursive function initialized with n =", n)

    def run(self, n=None):
        if n is None:
            n = self.n
        if n <= 0:
            return
        print("Running recursive function with n =", n)
        self.run(n-1)

    def __del__(self):
        print("Recursive function object destroyed")

# Create an object of the class
obj = RecursiveFunction(5)

# Call the recursive function
obj.run()

# Destroy the object
del obj

def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()

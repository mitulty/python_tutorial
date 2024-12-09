# -*- coding: utf-8 -*-
# @Author: Mitul Tyagi
# @Date:   2024-12-05 23:48:51
# @Description: Inheritance
'''
- Inheritance allows to define a class that inherits all the methods and properties from another class. Parent class is the class being 
  inherited from, also called base class. Child class is the class that inherits from another class, also called derived class.
- To create a class that inherits the functionality from another class, the parent class is sent as a parameter when creating the child class.
- The child's __init__() function overrides the inheritance of the parent's __init__() function. To keep the inheritance of the parent's 
  __init__() function, a call is added to the parent's __init__() function.
- Python also has a super() function that will make the child class inherit all the methods and properties from its parent. By using the super()
  function, the name of the parent element is not to be used, it will automatically inherit the methods and properties from its parent.
- The super keyword is used to explicitly call a superclass constructor from a subclass constructor.
- The visibility of inherited members (attributes and methods) in Python depends on their access modifiers.

    |----------------------------------------------------------------------------------------------|
    | Member Visibility| Public (default) | Protected (_single)              | Private (__double)  |
    |------------------|------------------|----------------------------------|---------------------|
    | In Base Class    | Accessible       | Accessible                       | Accessible          |
    | In Derived Class | Accessible       | Accessible within subclass/module| Not Accessible      |
    |----------------------------------------------------------------------------------------------|

- Public (default): Members are accessible from anywhere, both within the class and outside the class.
- Protected (_single): Members are accessible within the class, within derived classes, and within the same module. However, they are 
  considered conventionally private, and their use outside the class or module is discouraged.
- Private (__double): Members are accessible only within the class. They are not accessible in derived classes or outside the class.
- There are five types of inheritance:
            -> Single inheritance
            -> Multilevel inheritance
            -> Hierarchical inheritance
            -> Multiple inheritance
            -> Hybrid inheritance
- Single inheritance is a type of inheritance in object-oriented programming where a class inherits from only one base class.
- Multilevel inheritance in Python involves creating a chain of classes where each class extends the previous one. In other words, a derived 
  class serves as the base class for another class. When instances of these classes are created, each class has access to its own methods as 
  well as the methods of its parent classes.
- In hierarchical inheritance, a single base class (parent class) is inherited by multiple derived classes (child classes). Each derived class
  shares common attributes and methods from the base class but may have its own additional attributes and methods.  This structure promotes 
  code reuse and organization, as shared functionality is centralized in the base class, and specific behaviors can be defined in the derived 
  classes.
- Multiple inheritance in Python allows a class to inherit attributes and methods from more than one base class. This means that a derived 
  class can inherit from two or more parent classes. While multiple inheritance can be powerful, it also requires careful design to avoid 
  potential issues such as the diamond problem (a situation where ambiguity arises if two base classes have a common ancestor). 
- Hybrid inheritance in Python is a combination of multiple and hierarchical inheritance. In this scenario, two or more classes are derived 
  from a single base class using hierarchical inheritance, and then a new class is derived from these subclasses using multiple inheritance.

- Method overriding in Python is a mechanism that allows a subclass to provide a specific implementation for a method that is already defined 
  in its superclass. The overriding method in the subclass should have the same name and parameters (if overridden), but it may provide a 
  different implementation.
- In Python, when an object of a derived class is created, the constructor of the base class is called before the constructor of the derived 
  class. This ensures that the base class is fully constructed before any additional construction specific to the derived class takes place. 
  This is known as constructor chaining. The desctructor call is in the reverse method.

- isinstance() function can be used to check if an object is an instance of a particular class.
- issubclass() function can be used to check is a class is a subclass of another class. 

- A class can be derived from more than one superclass in Python. This is called multiple inheritance. For example:
                        class SuperClass1:
                            # features of SuperClass1

                        class SuperClass2:
                            # features of SuperClass2

                        class MultiDerived(SuperClass1, SuperClass2):
                            # features of SuperClass1 + SuperClass2 + MultiDerived class
- The diamond problem is a typical problem that is faced in multiple inheritance in Python. It is essentially an ambiguity that is arisen when there
  are two classes say B and C that inherit / are derived from a single class A, and there is another class D, that is a class derived from multiple 
  inheritance and inherits from B as well as C. This ambiguity is resolved using method resolution order.  This method resolution order is essentially
  an order in which a particular method is searched for in the hierarchy of classes in the case of inheritance.
- In the case of multiple inheritance, a given attribute is first searched in the current class if it's not found then it's searched in the parent 
  classes. The parent classes are searched in a left-right fashion and each class is searched once.

- Method Resolution Order(MRO) it denotes the way a programming language resolves a method or attribute. Python supports classes inheriting from other
  classes. The class being inherited is called the Parent or Superclass, while the class that inherits is called the Child or Subclass. In python, 
  method resolution order defines the order in which the base classes are searched when executing a method. First, the method or attribute is searched 
  within a class and then it follows the order specified while inheriting. This order is also called Linearization of a class and set of rules are called
  MRO(Method Resolution Order). While inheriting from another class, the interpreter needs a way to resolve the methods that are being called via an 
  instance.
- For a diamond inheritance where B and C inherits from A and D inherits from B and C the MRO is D-> B-> C-> A. The super() call always follow the MRO.
- To get the method resolution order of a class either __mro__ attribute or mro() method can be used.
'''
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")
x.printname()

class Student(Person):
    pass

x = Student("Mike", "Olsen")
x.printname()

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

x = Student("Charles", "Chaufer")
x.printname()

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

x = Student("John", "Smith")
x.printname()  

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

x = Student("Mike", "Olsen", 2019)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

## Single Inheritance
# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# Derived class inheriting from Animal
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

# Creating an instance of the derived class
dog_instance = Dog("Buddy")

# Calling methods from the base and derived classes
dog_instance.speak()  # This will call the overridden method in Dog class

## Multilevel Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks.")

class Labrador(Dog):
    def swim(self):
        print(f"{self.name} can swim.")

# Creating instances of the classes
animal = Animal("Generic Animal")
dog = Dog("Buddy")
labrador = Labrador("Max")

# Calling methods
animal.speak()      # Output: Generic Animal makes a sound.
dog.speak()         # Output: Buddy makes a sound.
dog.bark()          # Output: Buddy barks.
labrador.speak()    # Output: Max makes a sound.
labrador.bark()     # Output: Max barks.
labrador.swim()     # Output: Max can swim.

## Hierarchical inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

class Bird(Animal):
    def speak(self):
        return f"{self.name} sings beautifully!"

# Creating objects of the derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweetie")

# Calling the speak method on each object
print(dog.speak())   # Output: Buddy says Woof!
print(cat.speak())   # Output: Whiskers says Meow!
print(bird.speak())  # Output: Tweetie sings beautifully!

## Multiple Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Flyer:
    def fly(self):
        return f"{self.name} is flying!"

class Bird(Animal, Flyer):
    def speak(self):
        return f"{self.name} says Tweet!"

class Bat(Animal, Flyer):
    def speak(self):
        return f"{self.name} says Squeak!"

# Creating instances of derived classes
parrot = Bird("Parrot")
bat = Bat("Bat")

# Using methods from both base classes
print(parrot.speak())  # Output: Parrot says Tweet!
print(parrot.fly())    # Output: Parrot is flying!

print(bat.speak())     # Output: Bat says Squeak!
print(bat.fly())       # Output: Bat is flying!


## Hybrid
# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Subclasses using hierarchical inheritance
class Mammal(Animal):
    def give_birth(self):
        return f"{self.name} is giving birth to live young."

class Bird(Animal):
    def lay_eggs(self):
        return f"{self.name} is laying eggs."

# Derived class using multiple inheritance
class Platypus(Mammal, Bird):
    def speak(self):
        return f"{self.name} says Quack!"

# Example usage
platypus_obj = Platypus("Perry")

print(platypus_obj.speak())        # Output: Perry says Quack!
print(platypus_obj.give_birth())   # Output: Perry is giving birth to live young.
print(platypus_obj.lay_eggs())     # Output: Perry is laying eggs.


## Method Overriding
# Base class
class Animal:
    def make_sound(self):
        print("Animal makes a sound")

# Subclass 1
class Dog(Animal):
    def make_sound(self):
        print("Dog barks")

# Subclass 2
class Cat(Animal):
    def make_sound(self):
        print("Cat meows")

animal1 = Dog()
animal2 = Cat()

animal1.make_sound()  # Calls Dog's make_sound method
animal2.make_sound()  # Calls Cat's make_sound method

##Vehicle class Hierarchy
# Base class
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        print("Starting the", self.make, self.model)

    def stop(self):
        print("Stopping the", self.make, self.model)

# Derived class inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, make, model, numberOfDoors):
        super().__init__(make, model)
        self.numberOfDoors = numberOfDoors

    def honk(self):
        print("Honking the horn of the", self.make, self.model)


# Create an instance of the Vehicle class
generic_vehicle = Vehicle("Generic", "Vehicle")
generic_vehicle.start()
generic_vehicle.stop()

# Create an instance of the Car class
my_car = Car("Toyota", "Camry", 4)
my_car.start()
my_car.honk()
my_car.stop()

##Hierarchical Inheritance in Vehicle Classes
# Base class
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        print("Starting the", self.make, self.model)

    def stop(self):
        print("Stopping the", self.make, self.model)

# Derived class Car inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, make, model, numberOfDoors):
        super().__init__(make, model)
        self.numberOfDoors = numberOfDoors

    def honk(self):
        print("Honking the horn of the", self.make, self.model)

# Derived class Motorcycle inheriting from Vehicle
class Motorcycle(Vehicle):
    def __init__(self, make, model, engineType):
        super().__init__(make, model)
        self.engineType = engineType

    def wheelie(self):
        print("Performing a wheelie on the", self.make, self.model)

# Create an instance of the Car class
my_car = Car("Toyota", "Camry", 4)
my_car.start()
my_car.honk()
my_car.stop()

# Create an instance of the Motorcycle class
my_motorcycle = Motorcycle("Harley-Davidson", "Sportster", "4-stroke")
my_motorcycle.start()
my_motorcycle.wheelie()
my_motorcycle.stop()

## Animal class inheritance
# Base class Animal
class Animal:
    def __init__(self, name):
        self.name = name

# Derived class Dog
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def display_info(self):
        print(self.name)
        print(self.breed)

# Read input for name and breed
name = "Tom" #input()
breed = "Labrador" #input()

# Create a Dog object
my_dog = Dog(name, breed)

# Display information about the Dog
my_dog.display_info()

## Student and Postgraduate
# Base class
class Student:
    def __init__(self, student_name):
        self.student_name = student_name

    def display_details(self):
        print(self.student_name)


# Graduate class (inherits from Student)
class Graduate(Student):
    def __init__(self, student_name, graduation_year):
        super().__init__(student_name)
        self.graduation_year = graduation_year

    def display_details(self):
        super().display_details()
        print(self.graduation_year)


# Postgraduate class (inherits from Graduate)
class Postgraduate(Graduate):
    def __init__(self, student_name, graduation_year, thesis_topic):
        super().__init__(student_name, graduation_year)
        self.thesis_topic = thesis_topic

    def display_details(self):
        super().display_details()
        print(self.thesis_topic)


# Create instances of Student and Postgraduate
student = Student("Alice")
postgraduate = Postgraduate("Carol", 2025, "Quantum Mechanics")

# Display details of each student type
student.display_details()
print()
postgraduate.display_details()


### Examples of Multiple Inheritance

# creating class for father
class Dad():
	# writing a method for parent class 1
	def singing(self):
		print("Dad sings well")
		
# creating a class for mother
class Mom():
	# method for parent class 2
	def coding(self):
		print("Mom codes well")

# creating derived class
class Child(Dad, Mom):
	def playing(self):
		print("Kid loves to play")

# creating object of the new derived class
child = Child()
# calling methods of parent classes and derived class
child.singing()
child.coding()
child.playing()		

## The Diamond Problem
class Person:
	def display(self):
		print("Person called")
	
class Father(Person):
	def display(self):
		print("Father called")
	
class Mother(Person):
	def display(self):
		print("Mother called")
	
class Child(Father, Mother):
	pass
	
child_obj = Child()
child_obj.display()

## Using super()
# creating person class 
class Person():
	pass

# father class has attribute - father_name
class Father(Person):
	father_name = ""
	def father(self):
		print(self.name)

# mother class with attribute mother_name
class Mother(Person):
	mother_name = ""
	def mother(self):
		print(self.name)

# creating derived child class
class Child(Father, Mother):
	def parents(self):
		# Using super() method to access parent classes
		super().__init__()
		print("Father :", self.father_name)
		print("Mother :", self.mother_namename)

# creating child object
child = Child()
child.father_name = "Atharv"
child.mother_namename = "Gauri"
child.parents()

## Method is overriden in both the base classes
# creating parent class
class ParentClass():
	# adding function method in parent class
	def function(self):
		print("In Parent Class")
		# ... 
		
# Creating base class 1 derived from parent class	
class BaseClass1(ParentClass):
	# overriding the parent class method - function
	def function(self):
		print("In Base Class 1")
		# ...
		
# creating second base class derived from parent class	
class BaseClass2(ParentClass):
	# overriding the method again
	def function(self):
		print("In Base Class 2")
		
# creating child class derived from both base classes to test the overridden method - function
class ChildClass(BaseClass1, BaseClass2):
	pass

child_object = ChildClass()
child_object.function()

## Method is overriden in one of the classes
# creating the parent class and adding a method - function
class ParentClass():
	def function(self):
		print("In Parent Class")
		
# creating the base class derived from parent class, not overriding the method in this class
class BaseClass1(ParentClass):
	pass
		
# creating the second base class derived from the parent class, overriding the method - function from the parent class
class BaseClass2(ParentClass):
	# method overriding
	def function(self):
		print("In Base Class 2")
		
# creating final child class derived from base class 1 and base class 2 to test method overriding 
class ChildClass(BaseClass1, BaseClass2):
	pass

child_object = ChildClass()
child_object.function()

#when every class defines the same method
class ParentClass():
	def function(self):
		print("In Parent Class")
		
class BaseClass1(ParentClass):
	def function(self):
		print("In Base Class 1")
		
class BaseClass2(ParentClass):
	def function(self):
		print("In Base Class 2")
		
class ChildClass(BaseClass1, BaseClass2):
	def function(self):
		print("In Child Class")

child_object = ChildClass()
child_object.function()

print("MRO of Child: ",ChildClass.mro())
print("MRO of Child: ",ChildClass.__mro__)
class Tokenizer:
    """Tokenize text"""
    def __init__(self, text):
        print('Start Tokenizer.__init__()')
        self.tokens = text.split()
        print('End Tokenizer.__init__()')


class WordCounter(Tokenizer):
    """Count words in text"""
    def __init__(self, text):
        print('Start WordCounter.__init__()')
        super().__init__(text)
        self.word_count = len(self.tokens)
        print('End WordCounter.__init__()')


class Vocabulary(Tokenizer):
    """Find unique words in text"""
    def __init__(self, text):
        print('Start init Vocabulary.__init__()')
        super().__init__(text)
        self.vocab = set(self.tokens)
        print('End init Vocabulary.__init__()')


class TextDescriber(WordCounter, Vocabulary):
    """Describe text with multiple metrics"""
    def __init__(self, text):
        print('Start init TextDescriber.__init__()')
        super().__init__(text)
        print('End init TextDescriber.__init__()')


td = TextDescriber('row row row your boat')
print('--------')
print(td.tokens)
print(td.vocab)
print(td.word_count)


def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()

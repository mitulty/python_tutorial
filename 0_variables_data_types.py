# -*- coding: utf-8 -*-
# @Author: Mitul Tyagi
# @Date:   2024-12-05 23:48:51
# @Description: Variables and Data Types

'''
- Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.
- Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and
  functional programming. It was created by Guido van Rossum, and released in 1991. It is used for web-development, software development, scripting, machine learning
  and many other applications.
- Python is meant to be an easily readable language. Its formatting is visually uncluttered and often uses English keywords where other languages use punctuation. 
  Unlike many other languages, it does not use curly brackets to delimit blocks, and semicolons after statements are allowed but rarely used. It has fewer syntactic 
  exceptions and special cases than C or Pascal. Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or 
  parentheses.
- Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use 
  curly-brackets for this purpose. Python uses indentation to indicate a block of code. Python uses whitespace indentation, rather than curly brackets or keywords, to 
  delimit blocks. An increase in indentation comes after certain statements; a decrease in indentation signifies the end of the current block. The recommended indent 
  size is four spaces.
- Python syntax is like grammar for this programming language. Syntax refers to the set of rules that defines how to write and organize code so that the Python 
  interpreter can understand and run it correctly. These rules ensure that the code is structured, formatted, and error-free.
  
- Variables in python are essentially named references pointing to objects in memory. The type of the variable is not required to be declared explicitly. Based on the 
  value assigned, Python will dynamically determine the type.
- Python Variable is containers that store values. Python is not "statically typed". A variable is created the moment a valus is assigned to it. A Python variable 
  is a name given to a memory location. It is the basic unit of storage in a program. The value stored in a variable can be changed during program execution. A 
  Variable in Python is only a name given to a memory location, all the operations done on the variable effects that memory location.
- Casting can be done to specify the type of the variable.
- Python allows assigning a single value to several variables simultaneously with “=” operators. It allows adding different values in a single line with “,” operators.
- Local variables in Python are the ones that are defined and declared inside a function. These can not be used outside the function whereas global variables in Python
  are the ones that are defined and declared outside a function.
- Python global is a keyword that allows a user to modify a variable outside of the current scope. It is used to create global variables from a non-global scope i.e 
  inside a function. Global is not needed for printing and accessing. It is only used when the value of the variable is to be changed.
- If a variable is assigned a value anywhere within the function's body, it's assumed to be local unless explicitly declared as global. Variables that are only 
  referenced inside a function are implicitly global. There is no need to use a global keyword in Python outside a function.

- The Python print() function is often used to output variables. Multiple variables with comma separated values can be used.

 
- In Python, identifiers are unique names that are assigned to variables, functions, classes, and other entities. They are used to uniquely identify the entity within 
  the program. They should start with a letter (a-z, A-Z) or an underscore "_" and can be followed by letters, numbers, or underscores.
- Identifiers can be composed of alphabets (either uppercase or lowercase), numbers (0-9), and the underscore character (_). They shouldn't include any special 
  characters or spaces. The starting character of an identifier must be an alphabet or an underscore. Within a specific scope or namespace, each identifier should have
  a distinct name to avoid conflicts. However, different scopes can have identifiers with the same name without interference. Identifier names are case-sensitive.

- Keywords in Python are reserved words that have special meanings and serve specific purposes in the language syntax. They cannot be used as identifiers (names for 
  variables, functions, classes, etc.). These are (obtained from keyword.kwlist):
  ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 
  'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'].

- Comments in Python are statements written within the code. They are meant to explain, clarify, or give context about specific parts of the code. The purpose of 
  comments is to explain the working of a code, they have no impact on the execution or outcome of a program. Single line comments are preceded by the "#" symbol. 
  Everything after this symbol on the same line is considered a comment. Python doesn't have a specific syntax for multi-line comments. However, programmers often 
  use multiple single-line comments, one after the other, or sometimes triple quotes, even though they're technically string literals. Python ignores the string 
  literals that are not assigned to a variable.

- Writing a long statement in a code is not feasible or readable. Breaking a long line of code into multiple lines makes is more readable. This can be done using 
  backslash (\). Using a backslash does have some pitfalls, such as if there's a space after the backslash, it will result in a syntax error.
- In Python, statements are typically written on a single line. However, there are scenarios where writing a statement on multiple lines can improve readability or is
  required due to the length of the statement. This continuation of statements over multiple lines is supported in Python in various ways:
  -> Python implicitly supports line continuation within parentheses (), square brackets [], and curly braces {}. This is often used in defining multi-line lists, 
     tuples, dictionaries, or function arguments.
  -> Backslash '\' can be used explicitly to indicate that a statement should continue on the next line.
- The Python plus operator + provides a convenient way to add a value if it is a number and concatenate if it is a string. If a variable is already created it assigns
  the new value back to the same variable.
  
- In Python, literals are data types that store raw data for a software's source code. They are the foundation of syntax and are used to directly denote data within 
  code. Literals can hold any value type, including strings, numbers, and more.
        -> String literals: Represent a sequence of characters in single or double quotes, such as "hello" or "john". A single chatacter is a literal too.
        -> Numeric literals: Represent numbers, such as integers, floating-point numbers, or complex numbers
        -> Boolean literals: Represent the Boolean values True and False
        -> None literals: Represent a null value or absence of a value
        -> Sequence literals: Represent a sequence of lists and tuples
        -> Set literals: Represent sets, which are collections of unique elements
        -> Mapping literals: Represent mappings of key-value pairs, such as dictionaries
        -> Bytes and Bytearray literals: Represent a sequence of bytes 
- Python contains one special literal(None). None is used to define a null variable. If None is compared with anything else other than a None, it will return false.

- Data types are the classification or categorization of data items. It represents the kind of value that tells what operations can be performed on a particular data.
  Since everything is an object in Python programming, data types are actually classes and variables are instances (object) of these classes. Following are the
  different types: Numbers, Sequence, Boolean, Set and Dictionaries.
- Variables can store data of different types, and different types can do different things. Python has the following data types built-in by default, in these categories:
                                                                    Text Type:	    str
                                                                    Numeric Types:	int, float, complex
                                                                    Sequence Types:	list, tuple, range
                                                                    Mapping Type:	dict
                                                                    Set Types:	    set, frozenset
                                                                    Boolean Type:	bool
                                                                    Binary Types:	bytes, bytearray, memoryview
                                                                    None Type:	    NoneType

- Every value has a datatype, and variables can hold values. The storage method for each of the standard data types that Python provides is specified by Python. In 
  Python, the data type is set when the code assigns a value to a variable.
- The constructor functions can be used to specfiy the data type. These are str(), int(), float(), complex(), list(), tuple(), range(), dict(), set(), bool(), bytes(),
  frozenset(), bytearray(), and memoryview().
- Python offers the type() function to determine a variable's data type. The instance () capability is utilized to check whether an item has a place with a specific 
  class.
- Numeric values can be integers, complex numbers and floats. The sequence type includes Strings, Lists and Tuples.
- Numeric values are stored in numbers. The whole number, float, and complex qualities have a place with a Python Numbers datatype.
- Python supports three kinds of numerical data.
    -> Int: Whole number worth can be any length, like numbers 10, 2, 29, - 20, - 150, and so on. An integer can be any length you want in Python. Its worth has a 
            place with int.
    -> Float: Float stores drifting point numbers like 1.9, 9.902, 15.2, etc. It can be accurate to within 15 decimal places.
    -> Complex: An intricate number contains an arranged pair, i.e., x + iy, where x and y signify the genuine and non-existent parts separately. The complex numbers 
                like 2.14j, 2.0 + 2.3j, etc.
  One type can be converted to other using the constructors. Complex numbers can not be converted to others.

- Booleans represent one of two values: True or False. A condition with relational operators gives a boolean result. The bool() function allows to evaluate any value, 
  and gives True or False in return. Almost any value is evaluated to True if it has some sort of content. Any string is True, except empty strings. Any number is True,
  except 0. Any list, tuple, set, and dictionary are True, except empty ones.
- In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value 
  False evaluates to False.
- One more value, or object in this case, evaluates to False, and that is if the code has an object that is made from a class with a __len__ function that returns 
  0 or False. Functions can return a Boolean Value.
- Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain 
  data type.

- A variable is only available from inside the region it is created. This is called scope. A variable created inside a function belongs to the local scope of that 
  function, and can only be used inside that function. This is called a local variable. The local variable can be accessed from a function within the function.
- A variable created in the main body of the Python code is a global variable and belongs to the global scope. Global variables are available from within any scope, 
  global and local. The global keyword makes the variable global. To change the value of a global variable inside a function, refer to the variable by using the global
  keyword.
- The nonlocal keyword is used to work with variables inside nested functions. The nonlocal keyword makes the variable belong to the outer function.

'''

x = 15

def change():

    # using a global keyword
    global x

    # increment value of a by 5
    x = x + 5
    print("Value of x inside a function :", x)


change()
print("Value of x outside a function :", x)


# numberic
var = 123
print("Numeric data : ", var)

# type casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Sequence Type
String1 = 'Welcome to the Geeks World'
print("String with the use of Single Quotes: ")
print(String1)

# strings
x = "John"
# is the same as
x = 'John'

# Boolean
print(type(True))
print(type(False))
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print(bool("Hello"))
print(bool(15))

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#type() and isinstance()
a = 5  
print("The type of a: ", type(a))  
  
b = 40.5  
print("The type of b: ", type(b))  
  
c = 1+3j  
print("The type of c: ", type(c))  
print(" c is a complex number", isinstance(1+3j,complex))  

# Boolean Values from Relational Operators
print(10 > 9)
print(10 == 9)
print(10 < 9)


### Literals

# integer literal

# Binary Literals
a = 0b10100

# Decimal Literal
b = 50

# Octal Literal
c = 0o320

# Hexadecimal Literal
d = 0x12b

print(a, b, c, d)

# Float Literal
e = 24.8
f = 45.0

print(e, f)

z = 7 + 5j

# real part is 0 here.
k = 7j

print(z, k)

## Boolean Literals
a = (1 == True)
b = (1 == False)
c = True + 3
d = False + 7

print("a is", a)
print("b is", b)
print("c:", c)
print("d:", d)

### Scope
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

x = 300

def myfuncglobal():
  global x
  x = 200

myfuncglobal()

print(x)

def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

def main():
    print("Hello, World!")
    
    #indentation
    if 10 > 5:
        print("This is true!")
        print("I am tab indentation")

    print("I have no indentation")

    # I am single line comment

    """ Multi-line comment used
    print("Python Comments") """
    
    # sample comment
    name = "geeksforgeeks"
    print(name)
    
    # Python program to demonstrate
    # multiline comments
    print("Multiline comments")
    
    'Single-line comments using string literals'

    """ Python program to demonstrate
    multiline comments"""
    print("Multiline comments")
    
    Var = "Geeksforgeeks"
    print(Var) 
    
    # valid variable name
    geeks = 1
    Geeks = 2
    Ge_e_ks = 5
    _geeks = 6
    geeks_ = 7
    _GEEKS_ = 8

    print(geeks, Geeks, Ge_e_ks)
    print(_geeks, geeks_, _GEEKS_)
    
    # An integer assignment
    age = 45

    # A floating point
    salary = 1456.8

    # A string
    name = "John"

    print(age)
    print(salary)
    print(name)

    # declaring the var
    Number = 100

    # display
    print( Number)
    
    # re-declare the var
    Number = 120.3
  
    print("After re-declare:", Number)
    
    # Assigning multiple variables with the same value. They point to the same location.
    a = b = c = 10

    print(a)
    print(b)
    print(c)

    x, y, z = "Orange", "Banana", "Cherry"
    print(x)
    print(y)
    print(z)
    
    a, b, c = 1, 20.2, "GeeksforGeeks"

    print(a)
    print(b)
    print(c)

    #Unpacking from lists, tuples, etc.
    fruits = ["apple", "banana", "cherry"]
    x, y, z = fruits
    print(x)
    print(y)
    print(z)
    
    # Redefining a variable.
    a = 10
    a = "GeeksforGeeks"

    print(a)

    # + Operator on numbers
    a = 10
    b = 20
    print(a+b)

    # + Operator on strings. It concatenates the two.
    a = "Geeksfor"
    b = "Geeks"
    print(a+b)
    

if __name__ == "__main__":
    main()

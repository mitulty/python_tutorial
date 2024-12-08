# -*- coding: utf-8 -*-
# @Author: Mitul Tyagi
# @Date:   2024-12-05 23:48:51
# @Description: Comprehensions
'''
- A function is a block of code which only runs when it is called. A data called as parameters can be passed to the function. A function can return data as a result.
- In Python a function is defined using the def keyword. A function is called using the function name followed by parenthesis. Information can be passed into functions
  as arguments. Arguments are specified after the function name, inside the parentheses. Comma separated arguments are added.
- The terms parameter and argument can be used for the same thing: information that are passed into a function.
- From a function's perspective a parameter is the variable listed inside the parentheses in the function definition and an argument is the value that is sent to the 
  function when it is called.
- By default, a function must be called with the correct number of arguments. If the number of arguments is not known then a * before the parameter name can be used. 
  This will receive a tuple of arguments.
- Arbitrary Arguments are often shortened to *args in Python documentations.
- The arguments can also be send using the key = value syntax and the order of the arguments does not matter.
- Adding two asterisk (**) before the parameter name in the function definition will receive a dictionary of arguments.
- The phrase Keyword Arguments are often shortened to kwargs in Python documentations.
- A default value can be given to the function. If it is called without the value then the default value will be used.
- Any data types of argument can be passed to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
- The return statment returns a value from the function.
- The function definitions cannot be empty, but if you for some reason there is a function definition with no content, put in the pass statement to avoid getting an 
  error.
- To specify that a function can have only positional arguments and not keyword arguments , / is added after the arguments.
- To specify that a function can have only keyword arguments *, is added before the arguments.
- Any argument before the / , are positional-only, and any argument after the *, are keyword-only when they are combined together.
- The required positional argumtes have to come before the keyword arguments.

- Python also accepts function recursion, which means a defined function can call itself. Recursion is a common mathematical and programming concept. It means that a 
  function calls itself. If the recursion is not ended correctly then it becomes an infinite execution of function.

- Closures in Python help to invoke functions outside their scope.
'''
def my_function():
  print("Hello from a function")

my_function()

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Zen")


# *argrs to get tuples
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# key = value format
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# **kwargs to get a dictionary
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

def myfunction():
  pass

def my_function(x, /):
  print(x)

my_function(3)

def my_function(*, x):
  print(x)

my_function(x = 3)

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)

def hello_func(greetings, name = "You"):
    return '{},{}'.format(greetings,name)

print(hello_func("Hi"))
print(hello_func("Hi", "morack"))

def student_info(*args, **kwargs):
    print(args) # Accepts positional arguments as tuples
    print(kwargs) # Accepts keyword arguments as dictionaries
    
student_info('Math','Art',name = 'John', age = 22)
# student_info(name = 'John', age = 22,'Math','Art') # This is an error.

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 23}

student_info(courses,info) # courses and info both will be positional arguments and will become tuples
student_info(courses,data = info) # courses will be a positional arguments and will become tuple whereas info will be keyword argument and will become a dictionary
student_info(*courses,*info) # Both courses and info will be passed as positional arguments and will be come a tuple.
# student_info(**courses, **info) # error as courses is not a key, value
student_info(**info) # info will become a keyword argument and will be a dictionary. There will be no positional argument.
student_info(*courses, **info) # courses will be a positional argument and will become a tuple whereas info will be a keyword argument and will be become a dictionary.

# closures 
def outerFunction(text): 
 
    def innerFunction(): 
        print(text) 
 
    # returning function WITHOUT parenthesis
    return innerFunction  
 
 
def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()
    myFunction = outerFunction('Hey!') 
    myFunction() 

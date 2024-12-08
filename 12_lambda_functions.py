# -*- coding: utf-8 -*-
# @Author: Mitul Tyagi
# @Date:   2024-12-05 23:48:51
# @Description: Lambda Functions
'''
- A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression. The syntax of a lambda function
  is -> lambda arguments : expression. The expression is executed and the result is returned.
- Lambda functions are used when an anonymous function is required for a short period of time.
- A function is called Higher Order Function if it contains other functions as a parameter or returns a function as an output i.e, the functions that operate with 
  another function are known as Higher order Functions. It is worth knowing that this higher order function is applicable for functions and methods as well that takes 
  functions as a parameter or returns a function as a result. Python too supports the concepts of higher order functions.
- In Python, a function can be assigned to a variable. This assignment does not call the function, instead a reference to that function is created.
- Functions are like objects in Python, therefore, they can be passed as argument to other functions. They can also be returned from another functions.
'''

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

# Python program to illustrate functions can be treated as objects 
def shout(text): 
    return text.upper() 
  
print(shout('Hello')) 
  
# Assigning function to a variable
yell = shout 
  
print(yell('Hello'))

# Python program to illustrate functions can be passed as arguments to other functions 
def shout(text): 
    return text.upper() 
  
def whisper(text): 
    return text.lower() 
  
def greet(func): 
    # storing the function in a variable 
    greeting = func("Hi, I am created by a function passed as an argument.") 
    print(greeting)  
  
greet(shout) 
greet(whisper)


# Functions can return another function   
def create_adder(x): 
    def adder(y): 
        return x + y 
  
    return adder 
  
add_15 = create_adder(15) 
  
print(add_15(10))

def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
# @Author: Mitul Tyagi
# @Date:   2024-12-05 23:48:51
# @Description: Decorators
'''
- Error in Python can be of two types i.e. Syntax errors and Exceptions. Errors are problems in a program due to which the program will stop the execution. On the other
  hand, exceptions are raised when some internal events occur which change the normal flow of the program. In Python, there are several built-in Python exceptions that
  can be raised when an error occurs during the execution of a program.
    -> SyntaxError: This exception is raised when the interpreter encounters a syntax error in the code, such as a misspelled keyword, a missing colon, or an 
                    unbalanced parenthesis.
    -> TypeError: This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer.
    -> NameError: This exception is raised when a variable or function name is not found in the current scope.
    -> IndexError: This exception is raised when an index is out of range for a list, tuple, or other sequence types.
    -> KeyError: This exception is raised when a key is not found in a dictionary.
    -> ValueError: This exception is raised when a function or method is called with an invalid argument or input, such as trying to convert a string to an integer 
                   when the string does not represent a valid integer.
    -> AttributeError: This exception is raised when an attribute or method is not found on an object, such as trying to access a non-existent attribute of a class 
                       instance.
    -> IOError: This exception is raised when an I/O operation, such as reading or writing a file, fails due to an input/output error.
    -> ZeroDivisionError: This exception is raised when an attempt is made to divide a number by zero.
    -> ImportError: This exception is raised when an import statement fails to find or load a module.
- Exceptions are raised when the program is syntactically correct, but the code results in an error. This error does not stop the execution of the program, however, it 
  changes the normal flow of the program.
- Syntax Error: As the name suggests this error is caused by the wrong syntax in the code. It leads to the termination of the program.
- Try and except statements are used to catch and handle exceptions in Python. Statements that can raise exceptions are wrapped inside the try block and the statements
  that handle the exception are written inside except block. A try statement can have more than one except clause, to specify handlers for different exceptions. The else
  clause can also be used in Python. The code enters the else block only if the try clause does not raise an exception.
- Python provides a keyword finally, which is always executed after the try and except blocks. The final block always executes after the normal termination of the try 
  block or after the try block terminates due to some exception. The code within the finally block is always executed.
- The raise statement allows the programmer to force a specific exception to occur. The sole argument in raise indicates the exception to be raised. This must be 
  either an exception instance or an exception class (a class that derives from Exception).
'''

a = [1, 2, 3]
try: 
    print ("Second element = %d" %(a[1]))
    print ("Fourth element = %d" %(a[3]))

except:
    print ("An error occurred")

def fun(a):
    if a < 4:

        b = a/(a-3)
    print("Value of b = ", b)
    
try:
    fun(3)
    fun(5)
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")
    

def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

try:
    k = 5//0 
    print(k)

except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    print('This is always executed')
    
try: 
    raise NameError("Hi there")
except NameError:
    print ("An exception")
    raise


def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
# @Author: Mitul Tyagi
# @Date:   2024-12-05 23:48:51
# @Description: Map, Reduce and Filter Functions.
'''
- The map() function is used to apply a given function to every item of an iterable, such as a list or tuple, and returns a map object (which is an iterator).
- The syntax for the map() function is as follows: map(function, iterable). The iterator can be converted to a list or tuple using constructors.
- The map() function can be used with multiple iterables if the function takes more than one argument.

- The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not. It is used to select certain pieces
  of data from a list, tuple, or other collection of data. The syntax is filter(function, iterable). The filter function will only return the data for the function is
  True. It returns an iterator object which can be converted to list or tuples using constructurs.
  
- The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.This 
  function is defined in "functools" module.
- The reduce() can also be combined with operator functions to achieve the similar functionality as with lambda functions and makes the code more readable.
'''

s = ['1', '2', '3', '4']
res = map(int, s)
print(list(res))

a = [1, 2, 3, 4]

# Using custom function in "function" parameter
# This function is simply doubles the provided number
def double(val):
  return val*2

res = list(map(double, a))
print(res)


a = [1, 2, 3, 4]

# Using lambda function in "function" parameter
# to double each number in the list
res = list(map(lambda x: x * 2, a))
print(res)


a = [1, 2, 3]
b = [4, 5, 6]
res = map(lambda x, y: x + y, a, b)
print(list(res))


ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)
  
countries = ["India", "", "Argentina", "France", "Spain", "", "Australia"]
print(list(filter(lambda x: x != "", countries)))
print(list(filter(None, countries)))

# importing functools for reduce()
import functools

# initializing list
lis = [1, 3, 5, 6, 2]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a+b, lis))

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))

# importing operator for operator functions
import operator

# initializing list
lis = [1, 3, 5, 6, 2]

# using reduce to compute sum of list
# using operator functions
print("The sum of the list elements is : ", end="")
print(functools.reduce(operator.add, lis))

# using reduce to compute product
# using operator functions
print("The product of list elements is : ", end="")
print(functools.reduce(operator.mul, lis))

# using reduce to concatenate string
print("The concatenated product is : ", end="")
print(functools.reduce(operator.add, ["geeks", "for", "geeks"]))

def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()

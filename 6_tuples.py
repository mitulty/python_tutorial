# -*- coding: utf-8 -*-
# @Author: Mitul Tyagi
# @Date:   2024-12-05 23:48:51
# @Description: Tuples
'''
- Tuples are used to store multiple items in a single variable. A tuple is a collection which is ordered and unchangeable. Tuple items are ordered, unchangeable, and 
  allow duplicate values. Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
- Tuples are ordered that is the items have a defined order, and that order will not change.
- Tuples are unchangeable/immutable, meaning that the code cannot change, add or remove items after the tuple has been created.
- Since tuples are indexed, they can have items with the same value.
- The len() function gives the number of elements in the tuple.
- To create a tuple with only one item, a comma is added after the item, otherwise Python will not recognize it as a tuple.
- Tuple items can be of any data type. A tuple can contain different data types. It is also possible to use the tuple() constructor to make a tuple.

- Tuple items can be accessed using the indexs inside the square brackets. The first item has index zero. Negative indexing means start from the end.
- A range of indexes can be specified by specifying where to start and where to end the range. When specifying a range, the return value will be a new tuple with the 
  specified items. 
- By leaving out the start value, the range will start at the first item. By leaving out the end value, the range will go on to the end of the list. Specifing negative
  indexes start the search from the end of the list. To determine if a specified item is present in a list the in keyword used.
  
- Tuples can be updated by changing them to lists, updating the list and then converting back to tuples.
- The del keyword can delete the tuple completely.
- A tuple can be added to another tuple using the + operator.

- Creating and assigning values to a tuple is called packing a tuple. To extract the values into variables is called unpacking. The number of variables must match the
  number of values in the tuple, if not, the code must use an asterisk to collect the remaining values as a list.
  
- For loop can be used to loop through the tuple items. To loop through the tuple items by referring to their index number, the range() and len() functions can be used 
  to create a suitable iterable. While loops can be used too. List Comprehension offers the shortest syntax for looping through lists.
- The enumerate function can be used in for loops. It returns two values: the index and the tuple element. A start index can be mentioned for looping.

- To join two or more tuples the + operator can be used. To multiply the content of a tuple a given number of times, the * operator is used.

- Python has two built-in methods that can be used on tuples.
- The count() method returns the number of times a specified value appears in the tuple.
- The index() method finds the first occurrence of the specified value. It raises an exception if the value is not found.

'''

thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(len(thistuple))

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

tuple1 = ("abc", 34, True, 40, "male")

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

empty_tuple = tuple()
print("Empty List Tuple tuple(): ",empty_tuple, len(empty_tuple), type(empty_tuple))

empty_tuple = ()
print("Empty Tuple Using (): ",empty_tuple, len(empty_tuple), type(empty_tuple))

# indexing and slicing tuples
print("------------------Indexin and Slicing--------------------------------")
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
  
# updating tuples using lists
print("------------------Updating Tuples--------------------------------")
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

del thistuple

# Unpacking
print("------------------Unpacking Tuples--------------------------------")

fruits = ("apple", "banana", "cherry")

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# Looping
print("------------------Looping Tuples--------------------------------")
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
  
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
  
for index, item in enumerate(thistuple):
  print(index,item)

for index, item in enumerate(thistuple, start = 1):
  print(index,item)
  
# Concatenation
print("------------------ + and * on Tuples--------------------------------")
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)


# count method
print("------------------ count method --------------------------------")
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

# index method
print("------------------ index method --------------------------------")
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)
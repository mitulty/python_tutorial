# -*- coding: utf-8 -*-
# @Author: Mitul Tyagi
# @Date:   2024-12-05 23:48:51
# @Description: Lists
'''
- There are four collection data types in the Python programming language:
    -> List is a collection which is ordered and changeable. Allows duplicate members.
    -> Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    -> Set is a collection which is unordered, unchangeable, and unindexed. No duplicate members.
    -> Dictionary is a collection which is ordered and changeable. No duplicate members.

- Lists are used to store multiple items in a single variable. Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are 
  Tuple, Set, and Dictionary, all with different qualities and usage. Lists are created using square brackets. List items are ordered, changeable, and allow duplicate 
  values. List items are indexed, the first item has index [0], the second item has index [1] etc.
- Lists are ordered that is  the items have a defined order, and that order will not change. If a new item is added to a list, the new item will be placed at the end 
  of the list.  There are some list methods that will change the order, but in general: the order of the items will not change.
- The list is mutable, meaning that the code can change, add, and remove items in a list after it has been created. Since lists are indexed, lists can have items with
  the same value. The len() function tells the number of elements in the list. List items can be of any data type. A list can contain different data types.
- It is also possible to use the list() constructor when creating a new list.
- List items are indexed and can be accessed by referring to the index number. The first item has index 0. Negative indexing means start from the end. -1 refers to 
  the last item, -2 refers to the second last item etc.
- A range of indexes can be specified by specifying where to start and where to end the range. When specifying a range, the return value will be a new list with the 
  specified items. 
- By leaving out the start value, the range will start at the first item. By leaving out the end value, the range will go on to the end of the list. Specifing 
  negative indexes start the search from the end of the list. To determine if a specified item is present in a list the 'in' keyword is used.
- To change the value of a specific item, the index number is used.

- The insert() method inserts an item at the specified index.
- The append() method adds an item to the end of the list.
- The extend() method appends elements from another list to the current list. The elements will be added to the end of the list. The extend() method does not have to 
  append lists only, any iterable object (tuples, sets, dictionaries etc.) can be specified.

- The remove() method removes the specified item. If there are more than one item with the specified value, the remove() method removes the first occurrence.
- The pop() method removes the specified index. If no index is specified then the last element is removed. It returns the removed value.
- The del keyword also removes the specified index. The del keyword can also delete the list completely.
- The clear() method empties the list. The list still remains, but it has no content.

- For loop can be used to loop through the list items. To loop through the list items by referring to their index number, the range() and len() functions can be used 
  to create a suitable iterable. While loops can be used too. List Comprehension offers the shortest syntax for looping through lists.
- The enumerate function can be used in for loops. It returns two values: the index and the list element. A start index can be mentioned for looping.

- List objects have a sort() method that will sort the list alphanumerically, ascending, by default. To sort descending the keyword argument reverse = True is used.
  By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters. The str.lower can be used to have a case-
  insensitive sort function.
- The reverse() method reverses the current sorting order of the elements.
- The reverse() and sort() methods do the inplace operation. The sorted() function will return a new list.

- list1 = list2 will not copy the lists. It will create a reference to the original list. Any changes made in list2 will automatically also be made in list1. The 
  built-in copy() method can be used to copy a list. Another way to make a copy is to use the built-in method list(). The slice operator [:] can be used too.
- The copy method will do a shallow copy or a one-level deepcopy.
  
- There are several ways to join, or concatenate, two or more lists in Python. The + operator joins two lists. Another way to join two lists is by appending all the 
  items from list2 into list1, one by one. The extend() method also can be used where the purpose is to add elements from one list to another list.

- The count() method returns the number of elements with the specified value.

- The index() method returns the index of the first element with the specified value. It only returns the first occurence of the value. If no element found then it
  it returns a valueError.
  
- The in/not in operator can be used to check the presence or absence of an element in a list. It returns a True or False.

- The min(), max() and sum() functions can be used for lists of numbers to get useful information.

- The join() method of string converts a list into a string. It takes the form "string_used".join(list).

- Basic operations and methods:
  |-------------------|---------------------|---------------------------|
  |   Operation       |    Average Case     |    Amortised Worst Case   |
  |-------------------|---------------------|---------------------------|
  |     Append        |       O(1)          |       O(1)/O(N)           |
  |-------------------|---------------------|---------------------------|
  |     Clear         |       O(1)          |       O(1)                |
  |-------------------|---------------------|---------------------------|
  |     Containment   |       O(N)          |       O(N)                |
  |-------------------|---------------------|---------------------------|
  |     Copy          |       O(N)          |       O(N)                |
  |-------------------|---------------------|---------------------------|
  |     Delete        |       O(N)          |       O(N)                |
  |-------------------|---------------------|---------------------------|
  |     Extend        |       O(N)          |       O(N)                |
  |-------------------|---------------------|---------------------------|
  |     Equality      |       O(N)          |       O(N)                |
  |-------------------|---------------------|---------------------------|
  |   Access by Index |       O(1)          |       O(1)                |
  |-------------------|---------------------|---------------------------|
  |     Iteration     |       O(N)          |       O(N)                |
  |-------------------|---------------------|---------------------------|
  |     Length        |       O(1)          |       O(1)                |
  |-------------------|---------------------|---------------------------|
  |     Multiply      |       O(k*N)        |       O(k*N)              |
  |-------------------|---------------------|---------------------------|
  |     Min, Max      |       O(N)          |       O(N)                |
  |-------------------|---------------------|---------------------------|
  |     Pop from end  |       O(1)          |       O(1)                |
  |-------------------|---------------------|---------------------------|
  |  Pop intermediate |       O(N)          |       O(N)                |
  |-------------------|---------------------|---------------------------|
  |     Remove        |       O(N)          |       O(N)                |
  |-------------------|---------------------|---------------------------|
  |     Reverse       |       O(N)          |       O(N)                |
  |-------------------|---------------------|---------------------------|
  |     Slice         |       O(k)          |       O(k)                |
  |-------------------|---------------------|---------------------------|
  |     Sort          |       O(N*logN)     |       O(N*logN)           |
  |-------------------|---------------------|---------------------------|
  |   Store by Index  |       O(1)          |       O(1)                |
  |-------------------|---------------------|---------------------------|
  |     Count         |       O(N)          |       O(N)                |
  |-------------------|---------------------|---------------------------|
  |     Index         |       O(N)          |       O(N)                |
  |-------------------|---------------------|---------------------------|

'''
print("------------------Creating Lists--------------------------------")
thislist = ["apple", "banana", "cherry"]
print(thislist) # ["apple", "banana", "cherry"]

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist) #["apple", "banana", "cherry", "apple", "cherry"] 
print(len(thislist)) # 5

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list1 = ["abc", 34, True, 40, "male"]
mylist = ["apple", "banana", "cherry"]
print(type(mylist)) # <class 'list'>

# list() constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist) # ["apple", "banana", "cherry"]

empty_list = list()
print("Empty List using list(): ",empty_list, len(empty_list), type(empty_list)) # Empty List using list():  [] 0 <class 'list'>

empty_list = []
print("Empty List Using []: ",empty_list, len(empty_list), type(empty_list)) # Empty List Using []:  [] 0 <class 'list'>
#indexing and slicing
print("------------------Indexin and Slicing--------------------------------")
thislist = ["apple", "banana", "cherry"]
print(thislist[1]) # banana
print(thislist[-1]) # cherry

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # ['cherry', 'orange', 'kiwi']
print(thislist[-4:-1]) # ['orange', 'kiwi', 'melon']
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") # Yes, 'apple' is in the fruits list

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrent"
print(thislist) # ['apple', 'blackcurrent', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) # ['apple', 'watermelon']

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) # ['apple', 'blackcurrant', 'watermelon', 'cherry']

#insert method
print("------------------Insert Method--------------------------------")
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) # ['apple', 'banana', 'watermelon', 'cherry']

# append method
print("------------------Append Method--------------------------------")
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) # ['apple', 'banana', 'cherry', 'orange']

# extend method
print("------------------Extend Method--------------------------------")
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

thislist = ["apple", "banana", "cherry"] #list
thistuple = ("kiwi", "orange") # tuple
thislist.extend(thistuple)
print(thislist) # ['apple', 'banana', 'cherry', 'kiwi', 'orange']

# remove method
print("------------------Remove Method--------------------------------")
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) # ['apple', 'cherry']

# pop method
print("------------------Pop Method--------------------------------")
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) # ['apple', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) # ['apple', 'banana']

# del 
print("------------------del --------------------------------")
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) # ['banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
del thislist

# clear method
print("------------------Clear Method--------------------------------")
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) # []

# For and While loops for looping through lists
print("------------------Loops--------------------------------")
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  
for index, item in enumerate(thislist):
  print(index,item)

for index, item in enumerate(thislist, start = 1):
  print(index,item)
  
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# List comprehension to loop through the lists.  
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# sort() mehthod
print("------------------Sort Method--------------------------------")
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) # ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist) # [23, 50, 65, 82, 100]

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist) # ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist) # [100, 82, 65, 50, 23]

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist) # [50, 65, 23, 82, 100]

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) # ['banana', 'cherry', 'Kiwi', 'Orange']

#sorted() function
print("------------------Sorted Function--------------------------------")
thislist = ["banana", "Orange", "Kiwi", "cherry"]
new_sorted_list = sorted(thislist)
print("New Sorted List: ",new_sorted_list)

# reverse() method
print("------------------Reverse Method--------------------------------")
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) # ['cherry', 'Kiwi', 'Orange', 'banana']

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist = thislist[::-1]
print(thislist) # ['cherry', 'Kiwi', 'Orange', 'banana']
# copy() method
print("------------------Copy Method--------------------------------")
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist) # ['apple', 'banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist) # ['apple', 'banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist) # ['apple', 'banana', 'cherry']

# Joining two lists
print("------------------Joining Lists--------------------------------")
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3) # ['a', 'b', 'c', 1, 2, 3]

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1) # ['a', 'b', 'c', 1, 2, 3]

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1) # ['a', 'b', 'c', 1, 2, 3]

#count method()
print("------------------Count Method--------------------------------")
fruits = ['apple', 'banana', 'cherry','kiwi','cherry']
print(fruits.count("cherry")) # 1

#index() method
print("------------------Index Method--------------------------------")
fruits = [4, 55, 64, 32, 16, 32]

print(fruits.index(32)) # 3

# in/not in operator
print("------------------in/not in operators--------------------------------")
print( 4 in fruits) # True
print( 4 not in fruits) # False
print( 41 in fruits) # False
print( 41 not in fruits) # True

# min, max, and sum functions
print("------------------min/max/sum functions--------------------------------")
list_nums = [1, 3, 5, 6, 7]
print("Minimum Value: ",min(list_nums)) # Minimum Value:  1
print("Maximum Value: ",max(list_nums)) # Maximum Value:  7
print("Sum: ",sum(list_nums)) # Sum: 22

# join() method
print("------------------Join Method--------------------------------")
fruits = ['apple', 'banana', 'cherry']
fruits_str = " - ".join(fruits)
print(fruits_str) # apple - banana - cherry

# the split() method
print("------------------Split Method--------------------------------")
fruits_list = fruits_str.split(" - ")
print(fruits_list) # ['apple', 'banana', 'cherry']
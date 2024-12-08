# -*- coding: utf-8 -*-
# @Author: Mitul Tyagi
# @Date:   2024-12-05 23:48:51
# @Description: Sets
'''
- Sets are used to store multiple unique items in a single variable. A set is a collection which is unordered, unchangeable, and unindexed. Though the items can be 
  added or removed. Sets are written with curly brackets. Sets are unordered, that is the order of the items is not fixed. Set items are unordered, unchangeable, and 
  do not allow  duplicate values. Set items can not be indexed.
- The values True and 1 are considered the same value in sets, and are treated as duplicates. The values False and 0 are considered the same value in sets, and are 
  treated as duplicates.
- It is also possible to use the set() constructor to make a set.
- The len() function can be used to get the number of elements in the set.
- Set items can be of any data type. A set can contain different data types.

- Set items can not be accessed but can be looped through. The in/not in operators can be used to check the existence of an item.

- To add one item to a set the add() method is used.
- To add items from another set into the current set, the update() method is used. The object in the update() method does not have to be a set, it can be any iterable
  object (sets, lists, dictionaries etc.).

- To remove an item in a set, the remove(), or the discard() method is used. If the item to remove does not exist, remove() will raise an error. If the item to remove 
  does not exist, discard() will NOT raise an error.
- The pop method can be used but will remove a random item. The return value of the pop() method is the removed item.
- The clear() method empties the set. The del keyword will delete the set completely.

- The values True and 1 are considered the same value. The same goes for False and 0.

- There are several ways to join two or more sets in Python.
    -> The union() and update() methods joins all items from both sets.
    -> The intersection() method keeps ONLY the duplicates.
    -> The difference() method keeps the items from the first set that are not in the other set(s).
    -> The symmetric_difference() method keeps all items EXCEPT the duplicates.

- The union() method returns a new set with all items from both sets. The | operator instead of the union() method can also be used. All the joining methods and 
  operators can be used to join multiple sets. When using a method, just add more sets in the parentheses, separated by commas. The union() method allows to join 
  a set with other data types, like lists or sets. The result will be a set. The | operator only allows you to join sets with sets, and not with other data types 
  like the union() method can.
  
- The update() method inserts all items from one set into another. It changes the original set, and does not return a new set. Both union() and update() will exclude
  any duplicate items.

- The intersection() method will return a new set, that only contains the items that are present in both sets. The & operator can also be used instead of the 
  intersection() method. The & operator only allows you to join sets with sets, and not with other data types like the intersection() method can.

- The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

- The difference() method will return a new set that will contain only the items from the first set that are not present in the other set. The - operator can be used 
  instead of the difference() method. The - operator only allows you to join sets with sets, and not with other data types like the difference() method can.
- The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning 
  a new set.

- The symmetric_difference() method will keep only the elements that are NOT present in both sets. The ^ operator can be used instead of the symmetric_difference() 
  method. The ^ operator only allows you to join sets with sets, and not with other data types like the symmetric_difference() method can.
- The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.

- The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False. The <= operator instead can be used.
- <= returns whether another set contains this set or not. < returns whether all items in this set is present in other, specified set(s).

- The issuperset() method returns True if all items in the specified set exists in the original set, otherwise it returns False. The >= operator instead can be used.
- >= returns whether this set contains another set or not. 	> returns whether all items in other, specified set(s) is present in this set.

'''

thisset = {"apple", "banana", "cherry"}
print(thisset)
print(len(thisset))
print(type(thisset))

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

empty_set = set()
print("Empty List set set(): ",empty_set, len(empty_set), type(empty_set))

empty_set = {} # This is a dict
print("Empty set Using {} (this will be a dict): ",empty_set, len(empty_set), type(empty_set))

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

set1 = {"abc", 34, True, 40, "male"}

thisset = {"apple", "banana", "cherry"}


#Loops
print("------------------Loops--------------------------------")
for x in thisset:
  print(x)
  
# in/not in operator
print("------------------in/not in--------------------------------")
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)

# add() method
print("------------------add method--------------------------------")
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# update() method
print("------------------update method--------------------------------")
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

# remove() method
print("------------------remove method--------------------------------")
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# discard() method
print("------------------discard method--------------------------------")
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# pop() method
print("------------------pop method--------------------------------")
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# clear() method
print("------------------clear method--------------------------------")
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# del keyword
print("------------------del keyword--------------------------------")
thisset = {"apple", "banana", "cherry"}
del thisset

#union method
print("------------------union method--------------------------------")
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

# update method
print("------------------ update method--------------------------------")
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# intersection method
print("------------------ intersection method--------------------------------")
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

x = {"a", "b", "c", 3}
y = (1, 2, 3)

z = x.intersection(y)
print(z)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

# intersection_udpate method
print("------------------ intersection_udpate method--------------------------------")
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print(set1, set2)
set1.intersection_update(set2)
print(set1)

# difference method
print("------------------ difference method--------------------------------")
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)

x = {"a", "b", "c"}
y = ("a",1, 2, 3)

z = x.difference(y)
print(z)

# difference_update method
print("------------------ difference_update method--------------------------------")
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)

# symmetric_differences method
print("------------------ symmetric_differences method--------------------------------")
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)

# symmetric_difference_update method
print("------------------ symmetric_difference_update method--------------------------------")
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)

# isdisjoint method
print("------------------ isdisjoint method--------------------------------")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)

# issubset method
print("------------------ issubset method--------------------------------")
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

# issuperset method
print("------------------ issuperset method--------------------------------")
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = y.issuperset(x)
print(z)
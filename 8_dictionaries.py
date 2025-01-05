# -*- coding: utf-8 -*-
# @Author: Mitul Tyagi
# @Date:   2024-12-05 23:48:51
# @Description: Dictionaries
'''
- Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered, changeable and do not allow duplicates. As of Python 
  version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
- Dictionaries are written with curly brackets, and have keys and values. Dictionary items are presented in key:value pairs, and can be referred to by using the key
  name. Dictionaries cannot have two items with the same key. Duplicating values will overwrite existing values.
- To determine how many items a dictionary has, use the len() function.
- The values in dictionary items can be of any data type.
- It is also possible to use the dict() constructor to make a dictionary.

- To access the element, the key name is used. The get() method will also do the same. It returns a None if the element is not present. A default value can be give
  instead of getting None.

- The keys() method will return a list of all the keys in the dictionary. The list of the keys is a view of the dictionary, meaning that any changes done to the 
  dictionary will be reflected in the keys list.
- The values() method will return a list of all the values in the dictionary. The list of the values is a view of the dictionary, meaning that any changes done to the
  dictionary will be reflected in the values list.
- The items() method will return each item in a dictionary, as tuples in a list.The returned list is a view of the items of the dictionary, meaning that any changes 
  done to the dictionary will be reflected in the items list.
- To determine if a specified key is present in a dictionary the in keyword is used.

- The key name can be used to update the element. The update() method will update the dictionary with the items from the given argument. The argument must be a 
  dictionary, or an iterable object with key:value pairs.

- Adding an item to the dictionary is done by using a new index key and assigning a value to it. The update() method will update the dictionary with the items from a 
  given argument. If the item does not exist, the item will be added. The argument must be a dictionary, or an iterable object with key:value pairs. 

- The pop() method removes the item with the specified key name. 
- The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead).
- The del keyword removes the item with the specified key name. The del keyword can also delete the dictionary completely.
- The clear() method empties the dictionary.

- When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

- A dictionary can not be copied using dict1=dict2. To make a copy of a dictionary with the copy() method is used.
- Another way to make a copy is to use the built-in function dict().

- A dictionary can contain dictionaries, this is called nested dictionaries. To access items from a nested dictionary, the name of the dictionaries, starting with the 
  outer dictionary is used.

- The setdefault() method returns the value of the item with the specified key. If the key does not exist, insert the key, with the specified value.

- The fromkeys() method returns a dictionary with the specified keys and the specified value.
-
  |-------------------|---------------------|---------------------------|
  |   Operation       |    Average Case     |      Amortised Worst Case |
  |-------------------|---------------------|---------------------------|
  |      Clear        |        O(1)         |         O(1)              |
  |-------------------|---------------------|---------------------------|
  |      Get          |        O(1)         |         O(1)              |
  |-------------------|---------------------|---------------------------|
  |    Iteration      |        O(N)         |         O(N)              |
  |-------------------|---------------------|---------------------------|
  |      Length       |        O(1)         |         O(1)              |
  |-------------------|---------------------|---------------------------|
  |      pop()        |        O(1)         |         O(1)              |
  |-------------------|---------------------|---------------------------|
  |      popitem()    |        O(1)         |         O(1)              |
  |-------------------|---------------------|---------------------------|
  |      keys()       |        O(1)         |         O(1)              |
  |-------------------|---------------------|---------------------------|
  |      values()     |        O(1)         |         O(1)              |
  |-------------------|---------------------|---------------------------|
  |      items()      |        O(1)         |         O(1)              |
  |-------------------|---------------------|---------------------------|
  |      update()     |        O(1)         |         O(1)              |
  |-------------------|---------------------|---------------------------|
  |      clear()      |        O(1)         |         O(1)              |
  |-------------------|---------------------|---------------------------|
  |      copy()       |        O(1)         |         O(1)              |
  |-------------------|---------------------|---------------------------|
       del dict[key]  |        O(1)         |         O(1)              |
  |-------------------|---------------------|---------------------------|
  |    key in dict    |        O(1)         |         O(1)              |
  |-------------------|---------------------|---------------------------|
  
'''
print("------------------Creating Dictionaries--------------------------------")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))
print(type(thisdict))

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

# Accessing values
print("-------------------------------Accessing Values-------------------------")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
x = thisdict.get("model")
print(x)
x = thisdict.get("color")
print(x)
x = thisdict.get("color","Not Found")
print(x)

# keys() method
print("-------------------------------keys() method-------------------------")
x = thisdict.keys()
print(x)

# values() method
print("-------------------------------values() method-------------------------")
x = thisdict.values()
print(x)

# items() method
print("-------------------------------items() method-------------------------")
x = thisdict.items()
print(x)

# the in keyword.
print("-------------------------------in operator-------------------------")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# updating the dictionary
print("-------------------------------updating the dictionary-------------------------")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red","country":"japan"})
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict |= {"color": "yello","country":"korea"}
print(thisdict)

# adding a new element to the dictionary
print("-------------------------------adding a new element to the dictionary-------------------------")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

# pop() method
print("-------------------------------pop() method-------------------------")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
popped = thisdict.pop("model")
print(thisdict)
print(popped)

# popitem() method
print("-------------------------------popitem() method-------------------------")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

del thisdict["model"]
del thisdict

# clear() method
print("-------------------------------clear() method-------------------------")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

# Loops
print("-------------------------------Looping------------------------")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
  
for x in thisdict:
  print(thisdict[x])
  
for x in thisdict.values():
  print(x)
  
for x in thisdict.keys():
  print(x)

for x, y in thisdict.items():
  print(x, y)
  
# copy() method
print("-------------------------------copy() method-------------------------")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# Nested Dictionaries
print("-------------------------------Nested dictionaries-------------------------")
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])

# setdefault() method
print("-------------------------------setdefault() method-------------------------")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(car)
x = car.setdefault("model", "Bronco")
print(x)
x = car.setdefault("color", "white")
print(x)

print(car)
# fromkeys() method
print("-------------------------------fromkeys() method-------------------------")
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)
print(thisdict)

z = ('key1', 'key2', 'key3')

thisdict = dict.fromkeys(z)
print(thisdict)

w = ('key1', 'key2', 'key3')

thisdict = dict.fromkeys(w,'unknown')
print(thisdict)
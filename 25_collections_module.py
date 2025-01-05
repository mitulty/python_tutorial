# -*- coding: utf-8 -*-
# @Author: Mitul Tyagi
# @Date:   2024-12-14 02:52:48
# @Decription: Collections Module
'''
- Python programming language has four collection data types- list, tuple, sets, and dictionary. But python also comes with a built-in module known as 
  collections which have specialized data structures which basically covers for the shortcomings of the four data types.
- These are: namedtuple, dqueue, Chainmap, Counter, OrderedDict, defaultdict, UserDict, UserList and UserString.
- namedtuple(): It returns a tuple with a named entry, which means there will be a name assigned to each value in the tuple. It overcomes the problem of 
  accessing the elements using the index values. 
- deque(): deque pronounced as 'deck' is an optimized list to perform insertion and deletion easily. Deque (Doubly Ended Queue) is the optimized list for
  quicker append and pop operations from both sides of the container. It provides O(1) time complexity for append and pop operations as compared to the 
  list with O(n) time complexity.

- ChainMap: It is a dictionary-like class which is able to make a single view of multiple mappings. It basically returns a list of several other 
  dictionaries.
- Counter: It is a dictionary subclass which is used to count hashable objects.

- OrderedDict: It is a dictionary subclass which remembers the order in which the entries were added. It behaves like a hashh map like dictionary.

- defaultdict: It is a dictionary subclass which calls a factory function to supply missing values. In general, it does not throw any errors when a 
  missing key value is called in a dictionary.
- UserDict: This class acts as a wrapper around dictionary objects. The need for this class came from the necessity to subclass directly from dict. It 
  becomes easier to work with this class as the underlying dictionary becomes an attribute.
- UserList: This class acts like a wrapper around the list-objects. It is a useful base class for other lists like classes which can inherit from them and
  override the existing methods or even add fewer new ones as well.

- Methods of deque:
    -> append(x): Adds x to the right end of the deque.{O(1)}
    -> appendleft(x): Adds x to the left end of the deque. {O(1)}
    -> extend(iterable): Adds all elements from the iterable to the right end.{O(k)}
    -> extendleft(iterable): Adds all elements from the iterable to the left end (in reverse order). {O(k)}
    -> remove(value): Removes the first occurrence of the specified value from the deque. If value is not found, it raises a ValueError. {O(N)}
    -> pop(): Removes and returns an element from the right end. {O(1)} 
    -> popleft(): Removes and returns an element from the left end. {O(1)}
    -> clear(): Removes all elements from the deque. {O(1)}
    -> rotate(): Rotates the deque n steps to the right. If n is negative, rotates to the left. {O(k)}
    -> count(value): Counts the number of occurrences of value in the deque. {O(N)}
    -> index(value): Returns the index of the first occurrence of value in the deque. Raises ValueError if not found. {O(N)}
    -> reverse(): Reverses the elements of the deque in place. {O(N)}

- The bytearray() method returns a bytearray object in Python which is an array of given bytes. It gives a mutable sequence of integers in the range 0 <= x < 256. 
'''
from collections import namedtuple

a = namedtuple('courses' , 'name , tech')
s = a('data science' , 'python')
print(s)

# Declaring namedtuple()
Student = namedtuple('Student',['name','age','DOB'])
    
# Adding values
S = Student('Nandini','19','2541997')
    
# Access using index
print ("The Student age using index is : ",end ="")
print (S[1])
    
# Access using name
print ("The Student name using keyname is : ",end ="")
print (S.name)

 
from collections import deque
 
a = ['d' , 'u' , 'r' , 'e' , 'k']
a1 = deque(a)
print(a1)

a1.append('a')
print(a1)
# the output will be deque([ 'd' , 'u' , 'r' , 'e' , 'k' , 'a' ])
a1.appendleft('e')
print(a1)
# the output will be deque(['e' , 'd' , 'u' , 'r' , 'e' , 'k' , 'a' ])

a1.pop()
print(a1)
#the output will be deque([ 'e' , 'd' , 'u' , 'r' , 'e' , 'k' ])
a1.popleft()
print(a1)
#the output will be deque([ 'd' , 'u' , 'r' , 'e' , 'k' ])



from collections import ChainMap
a = { 1: 'edureka' , 2: 'python'}
b = {3: 'data science' , 4: 'Machine learning'}
c = ChainMap(a,b)
print(c)
#the output will be ChainMap[{1: 'edureka' , 2: 'python'} , {3: 'data science' , 4: 'Machine learning'}]
a1 = { 5: 'AI' , 6: 'neural networks'}
c1 = c.new_child(a1)
print(c1)
#the output will be ChainMap[{1: 'edureka' , 2: 'python'} , {3: 'data science' , 4: 'Machine learning'}, { 5: 'AI' , 6: 'neural networks'}]



from collections import Counter
a = [1,1,1,1,2,3,3,4,3,3,4]
c = Counter(a)
print(c)
#the output will be Counter = ({1:4 , 2:1 , 3:4 , 4:2})
# Creation of a Counter Class object using string as an iterable data container
x = Counter("geeksforgeeks")

# printing the elements of counter object
for i in x.elements():
    print (i, end = " ")
print()

from collections import OrderedDict
od = OrderedDict()
od[1] = 'e'
od[2] = 'd'
od[3] = 'u'
od[4] = 'r'
od[5] = 'e'
od[6] = 'k'
od[7] = 'a'
print(od)
#the output will be OrderedDict[(1 , 'e'), (2 , 'd') , (3 , 'u'), (4 , 'r'), (5 , 'e'), (6 , 'k'), (7 , 'a')]
od.move_to_end(3)
print(od)
#the output will be OrderedDict[(1 , 'e'), (2 , 'd') , (4 , 'r'), (5 , 'e'), (6 , 'k'), (7 , 'a'), (3 , 'u')]
od.popitem(last=True) 
print(od)
#the output will be OrderedDict[(1 , 'e'), (2 , 'd') , (4 , 'r'), (5 , 'e'), (6 , 'k'), (7 , 'a'), ]
od.popitem(last=False) 
print(od)
#the output will be OrderedDict[(2 , 'd') , (4 , 'r'), (5 , 'e'), (6 , 'k'), (7 , 'a'), ]

from collections import defaultdict
d = defaultdict(int)
#we have to specify a type as well.
d[1] = 'edureka'
d[2] = 'python'
print(d[3])
#it will give the output as 0 instead of keyerror.

str = "Geeksforgeeks"
 
# encoding the string with unicode 8 and 16
array1 = bytearray(str, 'utf-8')
array2 = bytearray(str, 'utf-16')
 
print(array1)
print(array2)

def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()

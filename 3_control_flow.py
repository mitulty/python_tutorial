# -*- coding: utf-8 -*-
# @Author: Mitul Tyagi
# @Date:   2024-12-05 23:48:51
# @Description: Control Flow
'''
- Python supports the usual logical conditions from mathematics. These conditions can be used in several ways, most commonly in "if statements" and loops. These are:
            Equals: a == b
            Not Equals: a != b
            Less than: a < b
            Less than or equal to: a <= b
            Greater than: a > b
            Greater than or equal to: a >= b
- An "if statement" is written by using the if keyword. The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
  The else keyword catches anything which isn't caught by the preceding conditions. Nested if statments can be written.
- The if statements cannot be empty, but if for some reason an if statement has no content, the pass statement is used to avoid getting an error.

- Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this 
  purpose.
- The and keyword is a logical operator, and is used to combine conditional statements.
- The or keyword is a logical operator, and is used to combine conditional statements.
- The not keyword is a logical operator, and is used to reverse the result of the conditional statement.

- Python has two primitive loop commands: while loops and for loops.

- With the while loop we can execute a set of statements as long as a condition is true. The while
  loop requires relevant variables to be ready. The break statement can be used to stop the execution of the loop even if the condition is true. With the continue 
  statement the current iteration can be skipped and the next iteration can be executed.

- A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). With the for loop the code can execute a set of 
  statements, once for each item in a list, tuple, set etc. The for loop does not require an indexing variable to set beforehand. Even strings are iterable objects, 
  they contain a sequence of characters. With the break statement the code can stop the loop before it has looped through all the items. With the continue statement 
  the code can stop the current iteration of the loop, and continue with the next.

- The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number. It can be used to 
  to loop through a set of code a specified number of times. The range() function defaults to 0 as a starting value, however it is possible to specify the starting 
  value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6). The range() function defaults to increment the sequence by 1, however
  it is possible to specify the increment value by adding a third parameter: range(2, 30, 3). The general syntax is range(start, end, step). Start and Step are 
  optionals.
- The else keyword in a for loop specifies a block of code to be executed when the loop is finished. The else block will NOT be executed if the loop is stopped by a 
  break statement.

- A nested loop is a loop inside a loop. The "inner loop" will be executed one time for each iteration of the "outer loop". The for loops cannot be empty, but if for 
  some reason the code has a for loop with no content, put in the pass statement to avoid getting an error.



'''
print("------------------If-Elif-Else Statements--------------------------------")
a = 33
b = 200
if b > a:
  print("b is greater than a")

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

if a > b or a > c:
  print("At least one of the conditions is True")

if not a > b:
  print("a is NOT greater than b")

if b > a:
  pass

print("------------------While loop--------------------------------")
i = 1
while i < 6:
  print(i)
  i += 1

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

print("------------------For loop--------------------------------")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

print("------------------Range--------------------------------")
for x in range(6):
  print(x)   #  range(6) is not the values of 0 to 6, but the values 0 to 5.

for x in range(2, 6):
  print(x)

for x in range(2, 30, 3):
  print(x)

for x in range(6):
  print(x)
else:
  print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

for x in [0, 1, 2]:
  pass
    
def main():
    pass

if __name__ == "__main__":
    main()

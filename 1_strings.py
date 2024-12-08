# -*- coding: utf-8 -*-
# @Author: Mitul Tyagi
# @Date:   2024-12-05 23:48:51
# @Description: Strings
'''
- String variables can be declared either by using single or double quotes. 'hello' is the same as "hello". These can be displayed using print() function. The code can
  use quotes inside a string, as long as they don't match the quotes surrounding the string. Assigning a string to a variable is done with the variable name followed 
  by an equal sign and the string. The code can assign a multiline string to a variable by using three quotes.
- Strings in Python are arrays of bytes representing unicode characters. However, Python does not have a character data type, a single character is simply a string 
  with a length of 1. Square brackets can be used to access elements of the string. Strings are arrays and can be looped using for loop. To get the length of a string, 
  the len() function is used. 
- To check if a certain phrase or character is present in a string, the keyword in can be used. To check if a certain phrase or character is NOT present in a string, 
  the code can use the keyword not in.
- A range of characters can be returned by using the slice syntax. Specify the start index and the end index, separated by a colon, to return a part of the string.
  By leaving out the start index, the range will start at the first character. By leaving out the end index, the range will go to the end. Negative indexes can be used
  to start the slice from the end of the string.
- Python has a set of built-in methods that can be used on strings.
  -> The upper() method returns the string in upper case.
  -> The lower() method returns the string in lower case.
  -> The swapcase()	method swaps cases, lower case becomes upper case and vice versa.
  -> The strip() method removes any whitespace from the beginning or the end.
  -> The replace() method replaces a string with another string.
  -> The split() method splits the string into substrings if it finds instances of the separator. It returns a list where the text specified between the specified 
     separator becomes the list items.
  -> The find() method searches the string for a specified value and returns the position of where it was found. Retruns -1 if no character found.
  -> The index() method searches the string for a specified value and returns the position of where it was found. Retruns -1 if no character found.
  -> The join() method joins the elements of an iterable to the end of the string.
  -> The rfind() method	searches the string for a specified value and returns the last position of where it was found. Retruns -1 if no character found.
  -> The rindex() method searches the string for a specified value and returns the last position of where it was found. Retruns -1 if no character found.
  -> The zfill() method fills the string with a specified number of 0 values at the beginning.
  -> The capitalize() method capitalizes the first character.
  -> The isdigit() method returns True if the string contains only digits.
  -> The isalpha() method returns True if the all characters are alphabets.
  -> The isalphanum() method return True if the characters are alphabets and digits.
  -> The count() method returns the number of times a character is present in the number.
  -> The reverse() method returns the reverse string.
- To concatenate, or combine, two strings the + operator is used.
- Strings and numbers can be combined by using f-strings or the format() method!.To specify a string as an f-string, simply put an f in front of the string literal, 
  and add curly brackets {} as placeholders for variables and other operations. A placeholder can contain variables, operations, functions, and modifiers to format the
  value. A placeholder can include a modifier to format the value. A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means 
  fixed point number with 2 decimals. A placeholder can contain Python code, like math operations. To insert characters that are illegal in a string, an escape character
  is used. An escape character is a backslash \ followed by the character to be inserted. Some of the escape characters: \', \\, \n, \r, \t, \b, \f, \ooo, and \xhh.
- String indexing allows accessing elements of a string using the pattern [start:end:step]. The start and end are the index values which can be negative ( from the end).
  The step tells the increment from the start till the step (defaults to 1). The end is exclusive. The [::-1] will reverse the sequence. Since the stride is negative, 
  Python swaps the start and end points so that the first offset is the last character and the last offset is the first character (inclusive).
'''

print("Hello")
print('Hello')
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#Strings 
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = "Hello, World!"
print(a[1])

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
print("expensive" not in txt)

# in single quote
s = 'geekforgeeks'

# in double quotes
t = "geekforgeeks"

# multi-line String
m = '''geek 
           for 
               geeks'''

print(s)
print(t)
print(m)
# character literal in single quote
v = 'n'

# character literal in double quotes
w = "a"

print(v)
print(w)

print("------------------Indexin and Slicing--------------------------------")
b = "No, World!"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])

print("------------------String Methods--------------------------------")
a = "Hello, Python!" 
print(a.upper())
print(a.lower())
print(a.strip()) # returns "Hello, Python!"
print(a.split(",")) # returns ['Hello', ' Python!']
print(a.replace("H", "J"))

print("------------------Concatenation (using +)--------------------------------")
a = "Hello"
b = "World"
c = a + b
print(a,b,c)

print("------------------Format Specifier--------------------------------")
age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = "We are the so-called \"Vikings\" from the north."

print(c)

def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()

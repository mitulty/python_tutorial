# -*- coding: utf-8 -*-
# @Author: Mitul Tyagi
# @Date:   2024-12-05 23:48:51
# @Description: User Input , Command Line Arguments and Output
'''
- Python allows for user input. Python 3.6 uses the input() method. Python 2.7 uses the raw_input() method.
- Python stops executing when it comes to the input() function, and continues when the user has given some input. This takes everthing as a string. Type conversion 
  functions can be used on numerical values.
- The print() can be used to give output on the console. The format specifiers format a value based on what flags are inserted ({value:flags}). Some of the flags are:
  -> :.(number)f = round to that many decimal places (fixed point)
  -> :.(number) = use these many digits
  -> :(number) =  allocate that many spaces
  -> :0(number) = allocate and zero pad that many spaces
  -> :< = left justify
  -> :> = right justify (default)
  -> :^ = center align
  -> :+ = use a plus sign to indicate positive value and - sign to indicate a negative value
  -> := = place sign to leftmost position
  -> :  = insert a space before positive numbers
  -> :, = comma separator for each thousands place
- The print functions ends with a newline character by default. To change it, {end=string} is used like print(x, end=" ")
- The syntax is print(object(s), sep=' ' ,end = '\n', file = file, flush = flush) 
      -> object(s) 	Any object. Will be converted to a string before printed
      -> sep 	      (Optional), Specify how to separate the objects, if there is more than one. Default is ' '.
      -> end	      (Optional), Specify what to print at the end. Default is '\n'.
      -> file	      (Optional), An object with a write method. Default is sys. stdout
      -> flush	    (Optional), A Boolean specifies if the output is flushed (True) or buffered (False). Default is False
'''
username = input("Enter username: ")
print("Username is: " + username)

accountid = int(input("Enter 4 digit numeric id: ")) # Converting to an integer.
print("Entered id is: ",accountid)

price1 = 3.14159
price2 = -987.65457
price3 = 12.34

print(f"Price 1 is ${price1:.2f}") # 2 decimal digits
print(f"Price 2 is ${price2:.3f}") # 3 decimal digits
print(f"Price 3 is ${price3:.1f}") # 1 decimal digit
print(f"Price 2 is ${price2:13}")  # 13 spaces to the variable
print(f"Price 2 is ${price2:.3}")  # print 4 digits

print(f"Price 1 is ${price1:010.2f}")  # right align to 10 spaces and pad with zeros at the start
print(f"Price 1 is ${price1:10.2f}")   # right align to 10 spaces
print(f"Price 1 is ${price1:<10.2f}")  # left align to 10 spaces
print(f"Price 1 is ${price1:<010.2f}") # left align to 10 spaces and 0 at the end
print(f"Price 1 is ${price1:>10.2f}")  # right align to 10 spaces 
print(f"Price 1 is ${price1:>010.2f}") # right align to 10 spaces and pad with zeros at the start

print(f"Price 1 is ${price1:^10.2f}")  # center align to 10 spaces
print(f"Price 1 is ${price1:^010.2f}")  # center align to 10 spaces and pad with zeros at both the ends
print(f"Price 1 is ${price1:^+010.2f}")  # center align to 10 spaces and pad with zeros at both the ends with sign
print(f"Price 2 is ${price2:^+010.2f}")  # center align to 10 spaces and pad with zeros at both the ends with sign
print(f"Price 1 is ${price1:+^010.2f}")  # center align to 10 spaces and pad with + at both the ends with sign
print(f"Price 2 is ${price2:+^010.2f}")  # center align to 10 spaces and pad with + at both the ends with sign
print(f"Price 1 is ${price1: ^10.2f}")  # center align to 10 spaces with a space between positive numbers
print(f"Price 2 is ${price2: ^10.2f}")  # center align to 10 spaces with a space between positive numbers


def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()

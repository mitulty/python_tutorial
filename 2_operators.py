# -*- coding: utf-8 -*-
# @Author: Mitul Tyagi
# @Date:   2024-12-05 23:48:51
# @Description: Strings
'''
- Operators are used to perform operations on variables and values.
- Python divides the operators in the following groups:
        -> Arithmetic operators
        -> Assignment operators
        -> Comparison operators
        -> Logical operators
        -> Identity operators
        -> Membership operators
        -> Bitwise operators
- Arithmetic operators are used with numeric values to perform common methematical operations. These are Addition(+), Subtraction(-), Multiplication(*), Division(/),
  Modulus(%), Exponentiation(**) and Floor Division(//).
- Assignment operators are used to assign values to variables. These are: = , +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<= and, :=.
- Comparison operators are used to compare two values. These are: == , !=, >, <, >=, and <=.
- Logical operators are used to combine conditional statements. These are: and, or and not.
        - and: Returns True if both statements are true.
        - or:  Returns True if one of the statments is true.
        - not: Reverses the result, returns Flase if the result is true.
- Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location. These are: is and
  is not. is returns True if both variables are the same object. is not	returns True if both variables are not the same object.
- Membership operators are used to test if a sequence is presented in an object. The in returns True if a sequence with the specified value is present in the object and
  the not in retruns True if a sequence with the specified value is not present in the object.
- Bitwise operators are used to compare (binary) numbers. These are AND(&), OR(|), XOR(^), NOT(~), Zero fill left shift(<<), and Signed right shift (>>).
        -> &  Sets each bit to 1 if both bits are 1
        -> |  Sets each bit to 1 if one of two bits is 1
        -> ^  Sets each bit to 1 if only one of two bits is 1
        -> ~  Inverts all the bits
        -> << Shift left by pushing zeros in from the right and let the leftmost bits fall off
        -> >> Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
- Operator precedence describes the order in which operations are performed. Parentheses has the highest precedence, meaning that expressions inside parentheses must be 
  evaluated first. Multiplication * has higher precedence than addition +, and therefor multiplications are evaluated before additions. If two operators have the same 
  precedence, the expression is evaluated from left to right.
    Operator	        Description
    ()	                Parentheses	
    **	                Exponentiation	
    +x  -x  ~x	        Unary plus, unary minus, and bitwise NOT	
    *  /  //  %	        Multiplication, division, floor division, and modulus	
    +  -	            Addition and subtraction	
    <<  >>	            Bitwise left and right shifts	
    &	                Bitwise AND	
    ^	                Bitwise XOR	
    |	                Bitwise OR	
    ==  !=  >  >=  <  
    <=  is  is not  in  
    not in 	            Comparisons, identity, and membership operators	
    not	                Logical NOT	
    and	                AND	
    or	                OR
- Common built-in functions for arithemtic numbers are: round(x,y), abs(x), pow(b,p), max(a,b,...) and min(a,b,.....).The math module has a lot of functions and members
  like math.pi, math.e, math.sqrt, math.ceil(), math.floor(), etc.
'''
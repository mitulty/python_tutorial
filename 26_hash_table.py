# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2024-12-14 03:17:16
# @Last Modified by:   Your name
# @Last Modified time: 2024-12-14 03:25:09
'''
-  Arrays and Linked Lists have time complexity O(n) for search and delete, while Hash Tables have just O(1) on average! 
- Hash Table elements are stored in storage containers called buckets. Every Hash Table element has a part that is unique that is called the key.
- A hash function takes the key of an element to generate a hash code. The hash code says what bucket the element belongs to, so now we can go directly
  to that Hash Table element: to modify it, or to delete it, or just to check if it exists. Specific hash functions are explained in detail on the next
  two pages.
- A collision happens when two Hash Table elements have the same hash code, because that means they belong to the same bucket. A collision can be solved
  in two ways.
- Chaining is the way collisions are solved by using arrays or linked lists to allow more than one element in the same bucket.
- Open Addressing is another way to solve collisions. With open addressing, if there is a nedd to store an element but there is already an element in that 
  bucket, the element is stored in the next available bucket. This can be achieved by liner probing, quadratic probing or double hashing.
'''

my_hash_table = [
    [None],
    ['Jones'],
    [None],
    ['Lisa'],
    [None],
    ['Bob'],
    [None],
    ['Siri'],
    ['Pete'],
    [None]
]

def hash_function(value):
    return sum(ord(char) for char in value) % 10
    
def add(value):
    index = hash_function(value)
    bucket = my_hash_table[index]
    if value not in bucket:
        bucket.append(value)
        
def contains(value):
    index = hash_function(value)
    bucket = my_hash_table[index]
    return value in bucket

add('Stuart')

print(my_hash_table)
print('Contains Stuart:',contains('Stuart'))

def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()

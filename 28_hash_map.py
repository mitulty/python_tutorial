# -*- coding: utf-8 -*-
# @Author: Mitul Tyagi
# @Date:   2024-12-11 06:44:50
# @Description: Hash Maps
'''
- A hash map (or hash table) in Python is a data structure that provides fast access to values associated with unique keys. It uses a hash function to 
  compute an index into an array of buckets or slots, from which the desired value can be found. Python's built-in dict type is an implementation of a 
  hash map. It implements an abstract array data type.
- A hash map is a data structure that allows for quick insertion, deletion, and retrieval of data. It works by using a hash function to map a key to an 
  index in an array. 
- Python dictionaries are the standard way to implement hash maps. They provide an efficient way to store and retrieve data based on keys.
- The time complexity for lookups, insersins, and deletions is O(1). The insertion order is maintained.
- Python's dictionaries handle collisions using a technique called open addressing with quadratic probing. When two keys hash to the same index, the 
  dictionary searches for the next available slot using a defined probing sequence.
- Following are the perfomance benefits:
    -> Fast Access: Hash maps provide average O(1) time complexity for lookups, insertions, and deletions, making them highly efficient for these 
                    operations.
    -> Efficient Memory Usage: Hash maps dynamically resize to maintain efficient usage of memory.
    -> Easy Management: Python's built-in dictionary type abstracts away the complexities of hash map implementation, including collision management and 
                        resizing.
    -> Versatile: Can store heterogeneous data and different types of keys and values.
    -> Order Preservation: From Python 3.7 onwards, dictionaries maintain the insertion order, providing an added benefit for ordered data access.
- The main differences between HashMap, Hashtable, and HashSet are:
    -> Key-value pairs: HashMap and Hashtable store key-value pairs, while HashSet only stores unique elements. 
    -> Nulls: HashMap allows nulls, while Hashtable does not. 
    -> Synchronization: HashMap is non-synchronized, while Hashtable is synchronized. 
    -> Speed: HashMap is generally faster than Hashtable because it's non-synchronized. 
    -> Implementation: HashSet uses a hash table internally, while HashMap uses a linked list approach. 
    -> Memory efficiency: HashSet is more memory efficient than HashMap because it only stores one copy of each unique element. 
    -> Look-up times: HashSet has slower look-up times than HashMap. 
    -> Suitability for tasks: HashSet is better suited for tasks that require quick look-ups, while HashMap is better suited for tasks that require 
                              frequent updates. 

- Similar to hash table, a hash set is also a collection of objects. In hash table, data was stored in the form of key-value pairs, whereas in hash sets, 
  the data is stored as objects. A hash set internally uses the hash table data structure to store data items. Just like a set, a hash set also does not 
  allow storage of duplicate elements.
  
- A hash map is used when there is a need to store key-value pairs and efficiently retrive values based on their keys. A commone use case is when there is
  a need to track frequencies, counts, or occurrences of elements in an array or list.
- A hash set is used when there is a need to efficiently check for the presence of elements in a collection and ensure uniqueness. A common use case is 
  when there is a need to find unique elements or identify whether there is any overlap between two collections.
'''

# Creating a hash map (dictionary)
hash_map = {}

# Adding key-value pairs
hash_map["name"] = "Alice"
hash_map["age"] = 25
hash_map["city"] = "New York"

# Accessing values
print(hash_map["name"])  # Output: Alice
print(hash_map["age"])   # Output: 25

# Modifying values
hash_map["age"] = 26

# Removing key-value pairs
del hash_map["city"]

# Checking for keys
if "name" in hash_map:
    print("Name is in the hash map")
    
# Function to display hashtable 
def display_hash(hashTable): 
      
    for i in range(len(hashTable)): 
        print(i, end = " ") 
          
        for j in hashTable[i]: 
            print("-->", end = " ") 
            print(j, end = " ") 
              
        print() 
  
# Creating Hashtable as  
# a nested list. 
HashTable = [[] for _ in range(10)] 
  
# Hashing Function to return  
# key for every value. 
def Hashing(keyvalue): 
    return keyvalue % len(HashTable) 
  
  
# Insert Function to add 
# values to the hash table 
def insert(Hashtable, keyvalue, value): 
      
    hash_key = Hashing(keyvalue) 
    Hashtable[hash_key].append(value) 
  
# Driver Code 
insert(HashTable, 10, 'Allahabad') 
insert(HashTable, 25, 'Mumbai') 
insert(HashTable, 20, 'Mathura') 
insert(HashTable, 9, 'Delhi') 
insert(HashTable, 21, 'Punjab') 
insert(HashTable, 21, 'Noida') 
  
display_hash (HashTable) 

class HashTable:

    # Create empty bucket list of given size
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    # Insert values into hash map
    def set_val(self, key, val):
      
        # Get the index from the key
        # using hash function
        hashed_key = hash(key) % self.size
        
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
            
            # check if the bucket has same key as
            # the key to be inserted
            if record_key == key:
                found_key = True
                break

        # If the bucket has same key as the key to be inserted,
        # Update the key value
        # Otherwise append the new key-value pair to the bucket
        if found_key:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))

    # Return searched value with specific key
    def get_val(self, key):
      
        # Get the index from the key using hash function
        hashed_key = hash(key) % self.size
        
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
            
            # check if the bucket has same key as the key being searched
            if record_key == key:
                found_key = True
                break

        # If the bucket has same key as the key being searched,
        # Return the value found
        # Otherwise indicate there was no record found
        if found_key:
            return record_val
        else:
            return "No record found"

    # Remove a value with specific key
    def delete_val(self, key):
      
        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size
        
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
            
            # check if the bucket has same key as
            # the key to be deleted
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return

    # To print the items of hash map
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)


hash_table = HashTable(50)

# insert some values
hash_table.set_val('gfg@example.com', 'some value')
print(hash_table)
print()

hash_table.set_val('portal@example.com', 'some other value')
print(hash_table)
print()

# search/access a record with key
print(hash_table.get_val('portal@example.com'))
print()

# delete or remove a value
hash_table.delete_val('portal@example.com')
print(hash_table)
    
def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()

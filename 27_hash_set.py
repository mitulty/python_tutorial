# -*- coding: utf-8 -*-
# @Author: Mitul Tyagi
# @Date:   2024-12-14 03:09:18
# @Decription: Hash Set
'''
- Similar to hash table, a hash set is also a collection of objects. In hash table, data was stored in the form of key-value pairs, whereas in hash sets,
  the data is stored as objects. A hash set internally uses the hash table data structure to store data items. Just like a set, a hash set also does not 
  allow storage of duplicate elements.
- In Python, sets are implemented using a hash table data structure. This allows for efficient membership testing (checking if an element is present in 
  the set) and insertion/deletion of elements.
- Key points about Python set implementation:
    -> Hash Table: The underlying data structure is a hash table, which maps each element in the set to a specific bucket based on its hash value.
    -> Unique Elements: Sets only store unique elements. If you try to add an element that is already present, it won't be added again.
    -> Unordered: Sets don't maintain any specific order of elements.
    -> Average Case O(1) Time Complexity: Due to the hash table implementation, operations like adding, removing, and checking membership have an average 
                                          time complexity of O(1).
    -> Worst Case O(n) Time Complexity: In rare cases, if there are many hash collisions, the performance can degrade to O(n) time complexity.
'''
class SimpleHashSet:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(size)]  # A list of buckets, each is a list (to handle collisions using chaining)

    def hash_function(self, value):
        # Simple hash function: sum of character codes modulo the number of buckets
        return sum(ord(char) for char in value) % self.size

    def add(self, value):
        # Add a value if it's not already present
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value not in bucket:
            bucket.append(value)

    def contains(self, value):
        # Check if a value exists in the set
        index = self.hash_function(value)
        bucket = self.buckets[index]
        return value in bucket

    def remove(self, value):
        # Remove a value
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value in bucket:
            bucket.remove(value)

    def print_set(self):
        # Print all elements in the hash set
        print("Hash Set Contents:")
        for index, bucket in enumerate(self.buckets):
            print(f"Bucket {index}: {bucket}")

# Creating the Hash Set from the simulation
hash_set = SimpleHashSet(size=10)

hash_set.add("Charlotte")
hash_set.add("Thomas")
hash_set.add("Jens")
hash_set.add("Peter")
hash_set.add("Lisa")
hash_set.add("Adele")
hash_set.add("Michaela")
hash_set.add("Bob")

hash_set.print_set()

print("\n'Peter' is in the set:",hash_set.contains('Peter'))
print("Removing 'Peter'")
hash_set.remove('Peter')
print("'Peter' is in the set:",hash_set.contains('Peter'))
print("'Adele' has hash code:",hash_set.hash_function('Adele'))

def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
# @Author: Mitul Tyagi
# @Date:   2024-12-24 20:37:50
# @Description: Searching Algorithms

'''
- Searching is a process of finding a particular record, which can be a single element or a small chunk, within a huge amount of data. The data can be in various 
  forms: arrays, linked lists, trees, heaps, and graphs etc. With the increasing amount of data nowadays, there are multiple techniques to perform the searching 
  operation.
- Various searching techniques can be applied on the data structures to retrieve certain data. A search operation is said to be successful only if it returns the
  desired element or data; otherwise, the searching method is unsuccessful. There are two categories these searching techniques fall into. They are: 
    -> Sequential Searching -> Interval Searching
- Common search techniques are: Linear Search, Binary Search, Interpolation Search, Jump Search, Hash Table, Exponential Search, etc.
- Linear search is a type of sequential searching algorithm. In this method, every element within the input array is traversed and compared with the key element to be
  found. If a match is found in the array the search is said to be successful; if there is no match found the search is said to be unsuccessful and gives the 
  worst-case time complexity.
- Binary search is a fast search algorithm with run-time complexity of O(log n). This search algorithm works on the principle of divide and conquer, since it divides 
  the array into half before searching. For this algorithm to work properly, the data collection should be in the sorted form. Binary search looks for a particular 
  key value by comparing the middle most item of the collection. If a match occurs, then the index of item is returned. But if the middle item has a value greater 
  than the key value, the right sub-array of the middle item is searched. Otherwise, the left sub-array is searched. This process continues recursively until the size 
  of a subarray reduces to zero.
'''
def linear_search(a, n, key):
   count = 0
   for i in range(n):
      if(a[i] == key):
         print("The element is found at position", (i+1))
         count = count + 1
   if(count == 0):
      print("The element is not present in the array")

a = [14, 56, 77, 32, 84, 9, 10]
n = len(a)
key = 32
linear_search(a, n, key)
key = 3
linear_search(a, n, key)


def binary_search(a, low, high, key):
   mid = (low + high) // 2
   if (low <= high):
      if(a[mid] == key):
         print("The element is present at index:", mid)
      elif(key < a[mid]):
         binary_search(a, low, mid-1, key)
      elif (a[mid] < key):
         binary_search(a, mid+1, high, key)
   if(low > high):
      print("Unsuccessful Search")

a = [6, 12, 14, 18, 22, 39, 55, 182]
n = len(a)
low = 0
high = n-1
key = 22
binary_search(a, low, high, key)
key = 54
binary_search(a, low, high, key)

def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()

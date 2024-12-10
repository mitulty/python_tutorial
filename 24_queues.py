# -*- coding: utf-8 -*-
# @Author: Mitul Tyagi
# @Date:   2024-12-05 23:48:51
# @Description: Queues
'''
- The queue is a linear data structure that stores items in a First In First Out (FIFO) manner. With a queue, the least recently added item is removed 
  first.
- Operations associated with queue are: 
    -> Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition -- Time Complexity : O(1)
    -> Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to 
       be an Underflow condition -- Time Complexity : O(1)
    -> Front: Get the front item from queue -- Time Complexity : O(1)
    -> Rear: Get the last item from queue -- Time Complexity : O(1)
- A queue can be implemented using list, collections.dequeu, queue.Queue and linked lists.
- Queue is built-in module of Python which is used to implement a queue. queue.Queue(maxsize) initializes a variable to a maximum size of maxsize. 
- There are various functions available in this module: 
    -> maxsize - Number of items allowed in the queue.
    -> empty() - Return True if the queue is empty, False otherwise.
    -> full() - Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
    -> get() - Remove and return an item from the queue. If queue is empty, wait until an item is available.
    -> get_nowait() - Return an item if one is immediately available, else raise QueueEmpty.
    -> put(item) - Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
    -> put_nowait(item) - Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
    -> qsize() - Return the number of items in the queue.
'''

# Implementing using lists
queue = []
queue.append('a')
queue.append('b')
queue.append('c')
print("Initial queue")
print(queue)
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print("\nQueue after removing elements")
print(queue)

# Implementing using collections.
from collections import deque
q = deque()
q.append('a')
q.append('b')
q.append('c')
print("Initial queue")
print(q)
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)

# Implementing using Queue
from queue import Queue
q = Queue(maxsize = 3)
print(q.qsize()) 
q.put('a')
q.put('b')
q.put('c')
print("\nFull: ", q.full()) 
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())
print("\nEmpty: ", q.empty())
q.put(1)
print("\nEmpty: ", q.empty()) 
print("Full: ", q.full())

# Implementation using Linked List


# Node class representing a single node in the linked list
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

# Class to implement queue operations using a linked list
class Queue:
    def __init__(self):
        # Pointer to the front and the rear of the linked list
        self.front = None
        self.rear = None

    # Function to check if the queue is empty
    def is_empty(self):
      
        # If the front and rear are null, then the queue is
        # empty, otherwise it's not
        return self.front is None and self.rear is None

    # Function to add an element to the queue
    def enqueue(self, new_data):
      
        # Create a new linked list node
        new_node = Node(new_data)

        # If queue is empty, the new node is both the front
        # and rear
        if self.rear is None:
            self.front = self.rear = new_node
            return

        # Add the new node at the end of the queue and
        # change rear
        self.rear.next = new_node
        self.rear = new_node

    # Function to remove an element from the queue
    def dequeue(self):
      
        # If queue is empty, return
        if self.is_empty():
            print("Queue Underflow")
            return

        # Store previous front and move front one node
        # ahead
        temp = self.front
        self.front = self.front.next

        # If front becomes null, then change rear also
        # to null
        if self.front is None:
            self.rear = None

    # Function to get the front element of the queue
    def get_front(self):
      
        # Checking if the queue is empty
        if self.is_empty():
            print("Queue is empty")
            return float('-inf')
        return self.front.data

    # Function to get the rear element of the queue
    def get_rear(self):
      
        # Checking if the queue is empty
        if self.is_empty():
            print("Queue is empty")
            return float('-inf')
        return self.rear.data
    
def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()

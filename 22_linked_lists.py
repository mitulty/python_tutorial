# -*- coding: utf-8 -*-
# @Author: Mitul Tyagi
# @Date:   2024-12-05 23:48:51
# @Description: Linked Lists
'''
- A linked list is a data structure that plays a crucial role in data organization and management. It contains a series of nodes that are stored at random
  locations in memory, allowing for efficient memory management. Each node in a linked list contains two main components: the data part and a reference to 
  the next node in the sequence. 
- They store elements in various, non-contiguous memory locations and connect them through pointers to subsequent nodes. This structure allows linked 
  lists to add or remove elements at any position by simply modifying the links to include a new element or bypass the deleted one. Once the position of 
  the element is identified and there is direct access to the point of insertion or deletion, adding or removing nodes can be achieved in O(1) time.
- Linked lists can grow and shrink dynamically without the need for reallocation or resizing. 
- Since pointers for each element must be stored to reference the next node, the memory usage per element is higher when using linked lists. Also, this 
  data structure does not allow direct access to data. Accessing an element requires sequential traversal from the beginning of the list, resulting in
  O(n) search time complexity.
- Linked lists are most useful when:
    -> There is a need to frequently insert and delete many elements
    -> The data size is unpredictable or likely to change frequently
    -> Direct access to elements is not a requirement
    -> The dataset contains large elements or structures
- There are three types of linked lists, each offering unique advantages for different scenarios. These types are:
    -> Singly-linked lists
    -> Doubly-linked lists
    -> Circular-linked lists

- A singly-linked list is the simplest type of linked list, where each node contains some data and a reference to the next node in the sequence. They can
  only be traversed in a single direction - from the head (the first node) to the tail (the last node).Each node in a singly-linked list typically consists
  of two parts:
    * Data: The actual information stored in the node.
    * Next Pointer: A reference to the next node. The last node's next pointer is usually set to null.
  Since these data structures can only be traversed in a single direction, accessing a specific element by value or index requires starting from the head 
  and sequentially moving through the nodes until the desired node is found. This operation has a time complexity of O(n), making it less efficient for 
  large lists. Inserting and deleting a node at the beginning of a singly-linked list is highly efficient with a time complexity of O(1). However, 
  insertion and deletion in the middle or at the end requires traversing the list until that point, leading to an O(n) time complexity. The design of 
  singly-linked lists makes them a useful data structure when performing operations that occur at the beginning of the list.

-  Each node in a doubly linked list contains three elements: the data, a pointer to the next node, and a pointer to the previous node.

- Circular linked lists are a specialized form of linked list where the last node points back to the first node, creating a circular structure. This means 
  that, unlike the singly and doubly linked lists the circular linked list does not end; instead, it loops around.

- Access (retrieving the n-th node): Linear — O(n)
- Search (retrieving a specified node): Linear — O(n)
- Insertion (adding a node to the list at the front): Constant — O(1)
- Deletion (removing a specified node at the front): Constant — O(1)
- Insertion (adding a node to the list at the end with no tail): Constant — O(n)
- Deletion (removing a specified node at the end with no tail): Constant — O(n)

'''
class Node:
    def __init__(self, data=None) -> None:
        self.value = data
        self.next = None
    
    def __del__(self):
        print("Node deleted!!!")

class Linked_List:
    
    def __init__(self) -> None:
        self.head = Node("head") # Creating a head node which is the place holder for the first node.
        self.size = 0
    
    def apppend(self, data):
        new_node = Node(data)
        cur = self.head
        self.size +=1
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
    
    def length(self):
        return self.size

    def display(self):
        cur_node = self.head
        elems = []
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.value)
        print("Elements: ",elems)
        # print (''.join((list(map(lambda x: '{}->'.format(x),elems)))))
    
    def get(self, index):
        if index >= self.length() and self.length == 0:
            print("Error: 'Get' Index out of range")
            return None
        cur_node = self.head
        cur_idx = 0
        while cur_node.next != None:
            cur_node = cur_node.next
            if(cur_idx == index):
                return cur_node.value
            cur_idx += 1
    
    def delete(self, index):
        if index >= self.length() and self.length == 0:
            print("Error: 'Erase' Index out of range")
            return None
        cur_node = self.head
        prev_node = self.head
        cur_idx = 0
        while(cur_node.next != None):
            prev_node = cur_node
            cur_node = cur_node.next
            if(cur_idx == index):
                break
            cur_idx += 1
        prev_node.next = cur_node.next
        del cur_node

def main():
    linked_list = Linked_List()
    linked_list.display()
    linked_list.apppend(5)
    linked_list.apppend(45)
    linked_list.apppend(56)
    linked_list.apppend(78)
    linked_list.apppend(2)
    linked_list.apppend(90)
    linked_list.display()
    print("Total Number of Elements: ",linked_list.length())
    
    print("3rd Element (index 2) in the list: ", linked_list.get(2))
    linked_list.delete(2)
    linked_list.display()
    print("3rd Element (index 2) in the list: ", linked_list.get(2))

if __name__ == "__main__":
    main()

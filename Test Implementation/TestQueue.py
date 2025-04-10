"""
IMPLEMENTATION OF QUEUE

Queue is a linear data structure and the are FIFO - first in first out 

Queues can be implemented using Linked List and Lists
Queue operations are

IMPLEMENTATION OF QUEUES USING LINKED LIST 

Enqueue - Adding new Node at the end
Dequeue - Removes node from start
Peek/ front - Returns the first element 
is_empty - Checks if the list is empty
"""

class Node: 
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def enqueue(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head =self.tail= new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.head is None:
            print("Queue Underflow")
            return
        value = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return value
    
    def peek(self):
        if self.head is None:
            print('Queue is empty')
            return
        print(self.head.data)
        return
    
    def is_empty(self):
        if self.head is None:
            print(True)
        else:
            print(False)


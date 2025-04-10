"""
IMPLEMENTATION OF CIRCULAR QUEUE
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularQueue:
    def __init__(self):
        self.head = None
        self.tail = None
    def enqueue(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            self.tail.next = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
        self.tail.next = self.head
    def dequeue(self):
        if self.head is None:
            print('Queue is empty')
            self.tail = None
            return
        self.tail.next = self.head.next 
        self.head = self.head.next
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
    

# Queue -> is FIFO First in First Out
# ENQUEUE = Adds Elements in the end 
# DEQUEUE = Removes element from the head 

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
            self.head = self.tail = new_node
            return
        self.tail.next = new_node 
        self.tail = new_node

    def dequeue(self):
        if self.head is None:
            print('Queue Underflow')
            self.tail = None
            return
        
        removed_data = self.head.data
        self.head = self.head.next
        return removed_data

    def peek(self):
        if self.head is None:
            print("Queue is empty")
            return
        print(self.head.data)

    def display(self):
        if self.head is None:
            print("Queue is empty")
        temp = self.head
        while temp:
            print(temp.data,'->',end=' ')
            temp = temp.next
        print(None)

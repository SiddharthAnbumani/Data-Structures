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
            print("Queue is empty")
        value = self.head.data
        self.head = self.head.next
        return value
    def front(self):
        return self.head.data
    
    def display(self):
        if self.head is None:
            print("Queue Underflow")
            return 
        temp = self.head
        while temp:
            print(temp.next, '->' , end=" ")
            temp = temp.next
        print()

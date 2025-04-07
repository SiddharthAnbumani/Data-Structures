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
            self.tail.next = self.head
            return
        self.tail.next = new_node
        self.tail = new_node
        self.tail.next = self.head
        return
    
    def dequeue(self):
        if self.head is None:
            print("Queue Underflow")
            return
        if self.head == self.tail:
            self.head = self.tail = None
            return
        else :
            value = self.head.data
            self.head = self.head.next
            self.tail.next = self.head
            return value
        
    def display(self):
        if self.head is None:
            print("The queue is empty")
            return
        temp = self.head
        while temp:
            print(temp.data,end=' ')
            temp = temp.next
            if temp == self.head:
                break
        print(None)


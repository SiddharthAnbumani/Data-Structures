class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class StackWithLinkedList:
    def __init__(self):
        self.head = None
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head 
        self.head = new_node
    def pop(self):
        if self.head is None:
            print("Stack Underflow")
            return 
        self.head = self.head.next
    def peek(self):
        return self.head.data
    def display(self):
        temp = self.head
        if temp is None:
            print('List is empty.')
            return
        while temp:
            print(temp.data, '->',end=' ')
            temp = temp.next
        print(None)
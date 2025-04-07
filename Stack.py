# Stack -> LIFO Last in first out 
# PUSH -> adds element in the beginning 
# POP -> Adds Element in the End 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
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
        print(self.head.data)
        return
    def display(self):
        if self.head is None:
            print('Empty Stack')
            return
        temp = self.head
        while temp:
            print(temp.data, '->', end=' ')
            temp = temp.next
        print(None)

# LIST implementation of stack 
# Takes a list and data as an arquement 

def push(list,data):
    list.append(data)
    return f'{data} is pushed'

def pop(list):
    list.pop()
    return 'element Popped'

def peek(list):
    return list[-1]

def display(lisy):
    for i in list:
        print(i, '->',end=' ')
    return
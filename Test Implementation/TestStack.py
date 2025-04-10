""" 
IMPLEMENTATION OF STACK

Implementation of stack can be done using a linked listed and an Array

Stack Operations are are.
Push -> Add elements in the top 
Pop -> Deletes elements from the Top 
Peek -> returns the top most element
Display -> Prints the entire stack

Implementation using a Linked List.

Push -> add elements in the top
Pop -> Deleted elements at the top 
Peek -> returns the first node in the list
Display -> Traverse the Linked List 
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
    def push(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head 
        self.head = new_node 
    def pop(self):
        if self.head is None:
            print('The stack is empty')
            return
        self.head = self.head.next
    def peek(self):
        if self.head is None:
            print("The stack is empty")
            return
        print(self.head.data)
        return
    def display(self):
        if self.head is None:
            print("The Stack is empty")
            return
        temp = self.head
        while temp:
            print(temp.data,'->',end=" ")
            temp = temp.next
        print()
        
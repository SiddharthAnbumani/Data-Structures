class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertStart(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insertEnd(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def insertPosition(self,data,position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head 
        counter = 0
        while temp is not None and counter < position -1 :
            temp = temp.next
            counter +=1
        if temp is None :
            print('Out of bounds')
            return
        new_node.next = temp.next
        temp.next = new_node 

    def deleteStart(self):
        if self.head is None:
            print("The List is empty")
            return
        self.head = self.head.next

    def deleteEnd(self):
        temp = self.head 
        if self.head is None:
            print("The List is empty")
            return
        if temp.next is None:
            self.head = None
            return
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    def deletePosition(self,position):
        temp = self.head
        counter = 0
        if self.head is None:
            print("List is empty")
            return
        if position == 0:
            self.head = self.head.next
            return
        while temp is not None and counter < position -1 :
            temp = temp.next
            counter +=1
        if temp is None or temp.next is None:
            print('Out of bounds')
            return
        temp.next = temp.next.next

    def traverse(self):
        temp = self.head
        if temp is None:
            print('List is empty.')
            return
        while temp:
            print(temp.data, '->',end=' ')
            temp = temp.next
        print(None)

    def search(self,key):
        if self.head is None:
            print('The List is Empty')
            return
        temp = self.head
        position = 0
        while temp:
            if temp.data == key:
                print(f"The key {key} found at position {position +1 }")
                return 
            position +=1
            temp = temp.next
        print("Not found in list")

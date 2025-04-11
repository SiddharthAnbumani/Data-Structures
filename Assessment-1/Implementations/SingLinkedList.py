class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head =None
    def insertStart(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insertEnd(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
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
        while temp and counter < position -1:
            temp = temp.next
            counter +=1
        if temp is None:
            print('Out of Bounds')
            return
        new_node.next = temp.next
        temp.next = new_node

    def deleteStart(self):
        if self.head is None:
            print('List is empty')
            return
        value = self.head.data
        self.head = self.head.next
        return value
    
    def deleteEnd(self):
        if self.head is None:
            print('List is empty')
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
    
    def deletePosition(self,position):
        if self.head is None:
            return 
        if position == 0:
            self.head = self.head.next
            return 
        temp = self.head
        counter = 0
        while temp is not None and counter < position -1:
            temp = temp.next
            counter +=1
        if temp is None or temp.next is None:
            print('out of bounds')
            return
        temp.next = temp.next.next

    def traverse(self):
        if self.head is None:
            print('List is empty')
            return 
        temp = self.head 
        while temp:
            print(temp.data, ' ->', end='')
            temp = temp.next
        print()
        
    def search(self,key):
        if self.head is None:
            print('List is empty')
            return
        temp = self.head
        while temp:
            if temp.data == key:
                print("key Found")
                return
            temp = temp.next
        return

            
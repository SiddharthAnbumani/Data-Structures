class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertStart(self,data):
        new_node = Node(data)
        if self.head is None:
            new_node = self.head
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insertEnd(self,data):
        new_node = Node(data)
        if self.head is None:
            new_node = self.head
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.self.prev = temp

    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def traverse(self):
        if self.head is None:
            print("the List is empty.")
            return 
        temp = self.head
        while temp:
            print(temp.data,'->', end=" ")
            temp = temp.next
            print(None)

    


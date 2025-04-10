class Node:
    def __init__(self,data):
        self.data = Node(data)
        self.next = None

def reverseLinkedList(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

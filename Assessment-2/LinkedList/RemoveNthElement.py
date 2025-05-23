class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None
class solution:
    def RemoveNthElement(self,head,n):
        dummy = Node(0)
        dummy.next = head
        first = dummy
        second = dummy
        
        for _ in range(n+1):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def MiddleOfLinkedList(self,head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
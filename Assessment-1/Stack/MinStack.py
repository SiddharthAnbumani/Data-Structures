"""
MinStack is a stack that performs all regular stack operations and also 
allows constant-time access to the minimum value present in the stack.
"""

class MinStack:
    def __init__(self):
       self.stack = []
       self.minStack = []

    def push(self, val):
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val,self.minStack[-1]))
      
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.minStack[-1]


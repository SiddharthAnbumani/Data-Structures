class MyQueue:
    def __init__(self):
        self.inStack = []
        self.outStack = []

    def enqueue(self,data):
        self.inStack.append(data)

    def dequeue(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        if not self.outStack:
            return None
        return self.outStack.pop()
    
    def front(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        if not self.outStack:
            return None
        return self.outStack[-1]
    
    def is_empty(self):
        return not self.inStack and not self.outStack
    
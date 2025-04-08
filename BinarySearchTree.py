class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        def _insert(current,data):
            if not current:
                 self.root = Node(data)
            if data < current.data:
                current.left = _insert(current.left,data)
            elif data > current.data:
                current.right = _insert(current.right,data)
            return current
        self.root = _insert(self.root,data)

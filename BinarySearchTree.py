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
    
    def search(self,target):
        def _search(current,target):
            if not current:
                return None
            if target == current.data:
                return current
            if target < current.data:
                return _search(current.left,target)
            else:
                return _search(current.right,target)
        return _search(self.root,target)

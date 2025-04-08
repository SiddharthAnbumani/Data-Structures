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
    
    def delete(self,target):
        def _delete(current,target):
            if not current:
                return None
            if target < current.data:
                current.left = _delete(current.left,target)
            elif target > current.data:
                current.right = _delete(current.right,target)
            else :
                # Used to delete lead node
                if not current.left and not current.right :
                    return None
                # If only one child Node
                if not current.left:
                    return current.right
                if not current.right:
                    return current.left
                # when has two childs  
                successor =  current.right # inorder Successor
                while successor.left:
                    successor = successor.left
                current.data = successor.data
                current.right = _delete(current.right,successor.data)
            return current
        self.root = _delete(self.root,target)
                
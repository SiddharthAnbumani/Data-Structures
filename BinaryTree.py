class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self,data):
        self.root = None

    def insert(self,data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return
        queue = [self.root]
        while queue:
            temp = queue.pop(0)
            if not temp.left:
                temp.left = new_node
                return
            else:
                queue.append(temp.left)
            if not temp.right:
                temp.right = new_node
                return
            else:
                queue.append(temp.right)

    def breadthFirstSearch(self):
        if not self.root:
            print('The Tree is empty')
            return
        queue = [self.root] 
        while queue:
            temp = queue.pop(0)
            print(temp.data,end=' ')
            if self.left:
                queue.append(self.left)
            if self.right:
                queue.append(self.right)

    def preorderTraversal(self,node):
        if node:
            print(node.data,end='')
            self.preorderTraversal(self.left)
            self.preorderTraversal(self.right)

    def inorderTraversal(self,node):
        if node:
            self.inorderTraversal(self.left)
            print(node.data,end='')
            self.inorderTraversal(self.right)
    def postorderTraversal(self,node):
        if node:
            self.postorderTraversal(self.left)
            self.postorderTraversal(self.right)
            print(node.data, end=' ')

class Node:
    def __init__(self, left=None,right=None,item=None):
        self.left = left
        self.right = right
        self.item = item
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        self.root = self.rinsert(self.root, data)
    def rinsert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.item:
            root.left = self.rinsert(root.left, data)
        elif data > root.item:
            root.right = self.rinsert(root.right, data)
        return root
    
        
        
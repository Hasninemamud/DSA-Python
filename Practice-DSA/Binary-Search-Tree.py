class Node:
    def __init__(self, left=None, right=None, item=None):
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
            return Node(item=data)
        if data < root.item:
            root.left = self.rinsert(root.left, data)
        elif data > root.item:
            root.right = self.rinsert(root.right, data)
        return root
    
    def search(self, data):
        return self.rsearch(self.root, data)
    def rsearch(self, root, data):
        if root is None or root.item == data:
            return root
        elif data < root.item:
            return self.rsearch(root.left, data)
        else:
            return self.rsearch(root.right, data)
        
    def inorder(self):
        result = []
        self.root = self.rinorder(self.root, result)
        return result
    def rinorder(self, root, result):
        if root:
            self.rinorder(root.left, result)
            result.append(root.item)
            self.rinorder(root.right, result)

bst = BST()
bst.insert(50)
bst.insert(10)
bst.insert(20)
bst.insert(60)
bst.insert(70)
print(bst.inorder())
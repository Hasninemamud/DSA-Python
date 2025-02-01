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
        elif data < root.item:
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
        self.rinorder(self.root, result)
        return result
    
    def rinorder(self, root, result):
        if root:
            self.rinorder(root.left, result)
            result.append(root.item)
            self.rinorder(root.right, result)
    
    def min_value(self, temp):
        current = temp
        while current.left is not None:
            current = current.left
        return current
    
    def max_value(self, temp):
        current = temp
        while current.right is not None:
            current = current.right
        return current
    
    def delete(self, data):
        self.root = self.rdelete(self.root, data)
    
    def rdelete(self, root, data):
        if root is None:
            return root
        if data < root.item:
            root.left = self.rdelete(root.left, data)
        elif data > root.item:
            root.right = self.rdelete(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            temp = self.max_value(root.left)
            root.item = temp.item
            root.left = self.rdelete(root.left, temp.item)
        return root

bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(15)
bst.insert(20)
bst.insert(60)
bst.insert(55)
bst.insert(65)

print("In-order before delete:", bst.inorder())
bst.delete(20)
print("In-order after delete:", bst.inorder())

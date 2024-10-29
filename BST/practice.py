class Node:
    def __init__(self, left=None, right=None, item=None):
        self.left= left
        self.right =right
        self.item=item
    
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        self.root = self.rinsert(self.root, data)
    
    def rinsert(self, root, data):
        if root is None:
            return Node(item = data)
        if data < root.item:
            root.left = self.rinsert(root.left, data)
        elif data > root.item:
            root.right = self.rinsert(root.right, data)
        return root
    
    def search(self, data):
        return self.rsearch(self.root, data)
    
    def rsearch(self, root, data):
        if root is None:
            return None
        elif root.item == data:
            return root
        elif data < root.item:
            return self.rsearch(root.left, data)
        elif data > root.item:
            return self.rsearch(root.right, data)
        
    def preorder(self):
        result = []
        self.rpreorder(self.root, result)
        return result
    
    def rpreorder(self, root, result):
        if root is not None:
            result.append(root.item)
            self.rpreorder(root.left, result)
            self.rpreorder(root.right, result)
            
    def inorder(self):
        result = []
        self.rinorder(self.root, result)
        return result
    
    def rinorder(self, root, result):
        if root is not None:
            self.rinorder(root.left, result)
            result.append(root.item)
            self.rinorder(root.right, result)
            
            
    def postorder(self):
        result = []
        self.rpostorder(self.root, result)
        return result
    
    def rpostorder(self, root, result):
        if root is not None:
            self.rpostorder(root.left, result)
            self.rpostorder(root.right, result)
            result.append(root.item)
            
    def max_value(self, temp):
        current = temp
        while current.right is not None:
            current = current.right
        return current.item
    
    def min_value(self, temp):
        current = temp
        while current.left is not None:
            current = current.left 
        return current.item
    
    def delete(self, data):
        self.root = self.rdelete(self.root, data)
        
    def rdelete(self, root, data):
        if root is None:
            return root
        if data < root.item:
            root.left = self.rdelete(root.left, data)
        elif data > root.item:
            root.right = self. rdelete(root.right, data)
        
        else:
            if root.left is None:
                return root.right 
            elif root.right is None:
                return root.left
            root.item = self.min_value(root.left)
            root.left = self.rdelete(root.left, root.item)
        return root
                
tree = BST()            
tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)
tree.insert(60)
tree.insert(15)        
tree.insert(35)        
tree.insert(32)        
tree.insert(65)        
tree.insert(68)        
    
print("Inorder Traversal:", tree.inorder())           
print("Preorder Traversal:", tree.preorder())        
search_result = tree.search(40)
if search_result is not None:
    print(f"Found: {search_result.item}")
else:
    print("Not Found")
print("Minimum value in the tree:", tree.min_value(tree.root))
print("Maximum value in the tree:", tree.max_value(tree.root))
tree.delete(20)
print("Inorder Traversal:", tree.inorder()) 
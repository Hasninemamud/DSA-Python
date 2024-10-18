class Node:
    def __init__(self, prev=None, item=None, Next=None):
        self.prev = prev
        self.item = item
        self.Next = Next

class Deque:
    def __init__(self):
        self.font = None
        self.rare = None
        self.item_count = 0
        
    def is_empty(self):
        return self.font == None
    
    def insert_font(self, data):
        n = Node(data, None, self.font)
        if self.is_empty():
            self.rare = n
        else:
            self.font.prev=n
        self.font = n
    
    def insert_rare(self, data):
        n = Node(data, self.rare)
        if self.is_empty():
            self.font=n
        else:
            self.rare.Next=n
        self.rare=n
        
    def delete_font(self):
        if self.is_empty():
            raise IndexError()
        elif self.font == self.rare:
            self.font=None
            self.rare=None
        else:
            self.font = self.font.Next
            self.font.prev=None
            
        
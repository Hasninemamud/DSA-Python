from linked_list import *

class Queue(Node, SLL):
    def __init__(self):
        self.font = None
        self.rare = None
        self.count = 0
        
    
    def is_empty(self):
        return self.font== None
    
    def enqueue(self, data):
        n = Node(data)
        if self.is_empty():
            self.font=n
        else:
            self.rare.next = n
        self.rare = n
        self.count += 1
        
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError()
        elif self.font==self.rare:
            self.font=None
            self.rare=None
        else:
            self.font=self.font.next
        self.count -= 1
    
    def get_font(self):
        if self.is_empty():
            raise IndexError()
        else:
            return self.font.item
    
    def get_rear(self):
        if self.is_empty():
            raise IndexError()
        else:
            return self.rare.item
    
    def size(self):
        return self.count
    
s1 = Queue()
s1.enqueue(10)
s1.enqueue(20)
s1.enqueue(30)
print(s1.get_font(), s1.get_rear())
s1.dequeue()
print(s1.get_font(), s1.get_rear())    
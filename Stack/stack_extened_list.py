class Stack(list):
    def is_empty(self):
        if len(self) == 0:
            return True
        else:
            return False
    
    def push(self, X):
        self.append(X)
    
    def pop(self):
        return super().pop(-1)
    
    def peek(self):
        return self[-1]
    
    def size(self):
        return len(self)
    
    def insert(self, index, data):
        raise AttributeError("No attribute insert in stack")
    
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(s)
s.pop()
print(s)
print(s.size())
print(s.is_empty())
print("Top Value", s.peek())
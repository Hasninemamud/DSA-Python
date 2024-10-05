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
    
s = Stack()
s.push(10)
s.push(20)
s.push(30)


print("Pop value is:", s.pop())
print("Pop value is:", s.pop())
print("Pop value is:", s.pop())
print(s)
print("So Peek value is:", s.peek())
print("So size of Stack is:", s.size())
print("So is Empty :", s.is_empty())
        
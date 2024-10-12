# Dequeue Implementation using List

class Dequeue:
    def __init__(self):
        self.dequeue = []
        
    def is_empty(self):
        return len(self.dequeue) == 0
    
    def insert_rare(self, data):
        self.dequeue.append(data)
    
    def insert_font(self, data):
        self.dequeue.insert(0, data)
        
    def delete_font(self):
        if self.is_empty ():
            raise IndexError()
        else:
            return self.dequeue.pop(0)
        
    def delete_rare(self):
        if self.is_empty ():
            raise IndexError()
        else:
            return self.dequeue.pop()
    
    def get_front(self):
        if self.is_empty ():
            raise IndexError()
        else:
            return self.dequeue[0]
    
    def get_rare(self):
        if self.is_empty ():
            raise IndexError()
        else:
            return self.dequeue[-1]
    
    def size(self):
        return len(self.dequeue)
    
q1 = Dequeue()
q1.insert_font(40)
q1.insert_rare(10)
q1.insert_rare(20)
q1.insert_rare(30)
print(q1.dequeue)
q1.delete_font()
q1.delete_rare()
print(q1.dequeue)
print(q1.get_front())
print(q1.get_rare())
print(q1.size())
print(q1.is_empty())
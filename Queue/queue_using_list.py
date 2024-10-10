class Queue(list):
    def __init__(self):
        self.list = []
        
    def is_empty(self):
        return len(self.list) == 0
    
    def enqueue(self, data):
        self.list.append(data)
    
    def dequeue(self):
        self.list.pop(0)
        
    def get_font(self):
        return 'Font Value is: ',self.list[-1] 
    
    def get_rear(self):
        return 'Fear Value is:', self.list[0] 
        
    def size(self):
        return len(self.list)

s1 = Queue()
s1.enqueue(10)
s1.enqueue(20)
s1.enqueue(30)
print(s1.list)
# s1.dequeue()
# s1.dequeue()
print(s1.list)
print(s1.get_font())
print(s1.get_rear())
print(s1.size())
print(s1.is_empty())
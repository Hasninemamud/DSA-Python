class PriorityQueue:
    def __init__(self):
        self.list = []
    
    def is_empty(self):
        return len(self.list)== 0
    
    def push(self, priority, data):
        index = 0
        while index<len(self.list) and self.list[index][0] <= priority:
            index += 1
        self.list.insert(index, (priority, data))
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Lsit is empty")
        else:
            return self.list.pop(0)
    
    def size(self):
        return len(self.list)
    
            
            

i = PriorityQueue()
i.push(1, 10)
i.push(2, 20)
i.push(3, 30)
i.push(4, 40)
i.push(5, 50)
print(i.list)
i.push(0, 100)
print(i.list)
# i.pop()
# i.pop()
# print(i.size())
# print(i.list)
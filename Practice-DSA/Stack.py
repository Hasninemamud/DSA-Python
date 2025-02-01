class Stack:
    def __init__(self, size):
        self.size = size
        self.curren_size = 0
        self.queueList = []
    
    def is_empty(self):
        return len(self.queueList) == 0
    
    def push(self, data):
        if self.size == self.curren_size:
            raise ValueError ("STACk IS FULL")
        self.queueList.append(data)
        self.curren_size += 1
    
    def pop(self):
        if self.is_empty():
            raise ValueError("Stack has no value")
        self.curren_size -= 1
        return self.queueList.pop(-1)
    
    def peek(self):
        return print("Top Value is:", self.queueList[-1])
    
    # def size(self):
    #     return print(len(self.queueList))
    
    def display(self):
        if self.is_empty():
            return print("Queue:", self.queueList)
        return print("Queue:", self.queueList)

myList = Stack(5)
myList.push(10)
myList.push(20)
myList.push(30)
myList.push(40)
myList.push(50)
# myList.push(60)
myList.display()
print("Pop Value is: ", myList.pop())
# print("Pop Value is: ", myList.pop())
myList.push(50)
myList.push(60)
myList.display()
myList.peek()
# print(myList.curren_size)
# print(myList.is_empty())
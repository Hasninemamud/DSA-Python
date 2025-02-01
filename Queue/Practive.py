class Queue:
    def __init__(self, size):
        self.max_size = size
        self.current_size = 0
        self.queueList = []
    
    def is_empty(self):
        return len(self.queueList) == 0
    
    def isFull(self):
        return self.current_size == self.max_size
    
    def enqueue(self, data):
        if self.isFull():
            raise ValueError("Queue is full. Cannot enqueue.")
        self.queueList.append(data)
        self.current_size += 1
        
    
    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty. Cannot dequeue.")
        self.current_size -= 1
        return self.queueList.pop(0)
    
    
    def get_front(self):
        if self.is_empty():
            print("Queue is Empty")
            return None
        return print("Front value is: ", self.queueList[0])
    
    def get_rear(self):
        if self.is_empty():
            print("Queue is Empty")
            return None
        return print("Rear value is: ", self.queueList[-1])
    
    # def size(self):
    #     return self.item
    
    def display(self):
        if self.is_empty():
            print("Queue is Empty")
            return None
        return print(self.queueList)    
    

myList = Queue(5)
myList.enqueue(10)
myList.enqueue(20)
myList.enqueue(30)
myList.enqueue(40)
myList.enqueue(50)

myList.display()
myList.dequeue()
myList.dequeue()
myList.display()
myList.get_front()
myList.get_rear()
print(myList.isFull())
# print(myList.size())
# if myList.is_empty():
#     print(myList.is_empty())
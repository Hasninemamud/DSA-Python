class Queue:
    def __init__(self):
        self.myList = []
        self.queueSize = 0
    
    def isEmpty(self):
        return len(self.myList) == 0
        
    
    def push(self, priority, data):
        self.myList.append((priority, data))
        self.queueSize += 1
    
    def pop(self):
        if self.isEmpty():
            print("Priority Queue is Empty")
            return None
        
        highPriority = 0
        for i in range(1, len(self.myList)):
            if self.myList[i][0] < self.myList[highPriority][0]:
                highPriority = i
        print(self.myList.pop(highPriority))
        return None
        
    
    def displayMylist(self):
        print(self.myList)
        return None

list = Queue()
list.push(3,20)
list.push(6,10)

list.push(1,15)
list.push(2,25)
list.push(0,1)
list.displayMylist()
list.pop()
list.displayMylist()
# list.isEmpty()
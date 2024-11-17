class Heap:
    def __init__(self):
        self.heap= []
    def createHeap(self, list1):
        for i in list1:
            self.insert(i)
    def insert(self, i):
        index = len(self.heap)
        parent_index = (index-1)//2
        while index>0 and self.heap[parent_index<i]:
            if index == len(self.heap):
                self.heap.append(self.heap[parent_index])
            else:
                 self.heap[index]=self.heap[parent_index]
            index = parent_index
            parent_index = (index-1)//2
            
        if index == len(self.heap):
            self.heap.append(i)
        else:
            self.heap[index] = i
class EmptyHeapException(Exception):
    def __init__(self, msg="Empty Heap"):
        self.msg = msg
    
    def __str__(self):
        return self.msg
    def top(self):
        if len(self.heap) == 0:
            raise EmptyHeapException
        return self.heap[0]
            
        
class Node:
    def __init__(self, item=None, next=None):
        self.item = item 
        self.next = next
    
class SLL:
    def __init__(self):
        self.start = None
    
    def is_empty(self):
        return self.start == None
    
    def insert_at_First(self, data):
        n = Node(data)
        self.start = n
    
    def insert_at_last(self, data):
        n = Node(data)
        if self.start is not None:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
            
        else:
            self.start = n
    
    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    
    def insert_after(self, target_data, data):
        n = Node(data)
        temp = self.start
        while temp is not None:
            if temp.item == target_data:
                n.next = temp.next
                temp.next = n
                return
            temp = temp.next
    
    def display(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end="--->")
            temp = temp.next
        print("None")
            
            

myList = SLL()
myList.insert_at_First(10)
myList.insert_after(10, 20)
myList.insert_after(20, 30)
# myList.insert_at_First(30)
myList.insert_at_last(50)
myList.display()

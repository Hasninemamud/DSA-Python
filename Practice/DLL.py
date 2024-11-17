class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self, start=None):
        self.start = start
    
    def is_empty(self):
        return self.start is None
    
    def insert_at_start(self, data):
        n = Node(None, data, self.start)
        if self.start is not None:
            self.start.prev = n
        self.start = n
        
    def insert_at_last(self, data):
        n = Node(None, data, None)
        if self.start is not None:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
            n.prev = temp
        else:
            self.start = n
    
    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    
    def insert_after(self, find_data, data):
        n = Node(None, data, None)
        temp = self.start
        while temp is not None:
            if temp.item == find_data:
                n.next = temp.next
                if temp.next is not None:
                    temp.next.prev = n
                temp.next = n
                n.prev = temp
                return
            temp = temp.next
        print("Data not found")
    
    def display(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ----> ")
            temp = temp.next
        print("None")

# Testing the doubly linked list
myList = DLL()

myList.insert_at_start(10)
myList.insert_at_start(20)
myList.insert_at_start(30)
myList.insert_at_last(40)
myList.insert_after(20, 25)  # Insert 25 after 20
myList.display()
print(myList.is_empty())

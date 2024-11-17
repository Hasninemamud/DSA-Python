class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next
    
class SLL:
    def __init__(self, head=None):
        self.head = head
    
    def is_empty(self):
        return self.head == None
    
    def insert_at_start(self, data):
        n = Node(data, self.head)
        self.head = n
    
    def insert_at_last(self, data):
        n = Node(data)
        if not self.is_empty():
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.head = n
            
    def search(self, data):
        temp = self.head
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n         
        
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.item, end="-->")
            temp = temp.next
        print("None")
    
    
    def delete(self):
        if self.head is not None:
            self.head = self.head.next
    
    
    def delete_last(self):
        if self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next.next  is not None:
                temp = temp.next
            temp.next = None
    
    
    def delete_item(self, data):
        if self.head is not None:
            temp = self.head
            while temp.next.item == data:
                temp.next = temp.next.next
                temp = temp.next
            
    
# Testing the corrected code
myList = SLL()
myList.insert_at_start(10)
myList.insert_at_start(20)
myList.insert_at_start(30)
myList.insert_at_last(50)
myList.display()  # Expected output: 30-->20-->10-->50-->None

myList.delete_item(20)
myList.display()
print(myList.is_empty())  # Expected output: False

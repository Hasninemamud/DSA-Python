class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next
        
class DLL:
    def __init__(self,start=None):
        self.start = start
    
    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self, data):
        n = Node(None,data, self.start)
        if self.start is not None:
            self.start.prev = n
        self.start = n
        
        
    def insert_at_last(self,data):
        n = Node(None, data, None)
        if self.start is not None:
            temp = self.start
            # Got an error 
            while temp.next is not None: 
                temp = temp.next
            temp.next = n
            n.prev = temp
            
        else:
            self.start = n
    
    
    def search(self, data):
        temp = self.start
        if self.start is not None:
            while temp.item == data:
                return temp
            temp = temp.next
        return None
    
    
    def insert_after(self, find_data, data):
        n = Node(None, data, None)
        temp = self.start
        while temp.item == find_data:
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

    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next  
            if self.start is not None:
                self.start.prev = None
    
    def delete_last(self):
       
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next != None:
                temp = temp.next
            temp.next = None
    
    def delete_item(self, data):
        if self.start is None:
            print("List is empty")
            return

    # If the first node contains the data
        if self.start.item == data:
            if self.start.next is None:
            # If there's only one node
                self.start = None
            else:
            # Move the start pointer to the next node
                self.start = self.start.next
                self.start.prev = None
            return

    # Traverse the list to find the node
        temp = self.start
        while temp is not None and temp.item != data:
            temp = temp.next

    # If the data is not found
        if temp is None:
            print("Data Not Found")
            return

    # If the data is found
        if temp.next is not None:
            temp.next.prev = temp.prev
        if temp.prev is not None:
            temp.prev.next = temp.next

    
            
            
        
myList = DLL()

myList.insert_at_start(10)
myList.insert_at_start(20)
myList.insert_at_start(30)
myList.insert_at_last(40)
# myList.insert_after(20, 25)
myList.display()
# myList.delete_first()
# myList.display()
# myList.delete_last()
# myList.display()

myList.delete_item(50)
myList.display()
# print(myList.is_empty())
class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class CLL:
    def __init__(self, last=None):
        self.last = last

    def is_empty(self):
        return self.last is None

    def insert_at_start(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
    
    def insert_at_last(self, data):
        n = Node(data)
        if self.is_empty():  # Check if the list is empty
            n.next = n  # Point to itself
            self.last = n  # Update the last pointer
        else:
            n.next = self.last.next  # New node points to the first node
            self.last.next = n  # Last node points to the new node
            self.last = n  # Update the last pointer to the new node

    

    
    def search(self, data):
        if self.is_empty():
            print("List is Empty")
            return None
        else:
            temp = self.last.next
            while True:
                if temp.item == data:
                    return temp
                temp = temp.next
                if temp == self.last.next:
                   break
            print("Item not found")
            return None
           
    def insert_after(self, target_node, data):
        n = Node(data)
        if self.is_empty():
            return None
        else:
            temp = self.last.next
            while True:
                if temp.item== target_node:
                    n.next = temp.next
                    temp.next = n
                temp = temp.next
                if temp == self.last.next:
                    break
            return "Node not Found"

    def display_item(self):
        if self.last is not None:
            temp = self.last.next
            while temp is not None:
                print(temp.item, end="-->")
                temp = temp.next
                if temp == self.last.next:
                    break
    
    def delete_first(self):
        if self.is_empty():
            return None
        temp = self.last.next
        self.last.next = temp.next
        return temp.item
    
    def delete_last(self):
        temp = self.last.next
        while temp.next != self.last:  # Stop at the second-to-last node
            temp = temp.next

    # Update pointers to remove the last node
        item = self.last.item  # Store the value to return
        temp.next = self.last.next  # Second-to-last node points to the first node
        self.last = temp  # Update `self.last` to the second-to-last node
        return item
        
        

myList = CLL()

myList.insert_at_start(10)
myList.insert_at_start(20)
myList.insert_at_start(30)
myList.insert_at_last(40)
myList.insert_at_last(50)

myList.insert_after(20, 25)

myList.insert_after(40, 45)


print(myList.delete_first())

print(myList.delete_last())
myList.display_item()
# print("Last Delete Item: ",myList.delete_last())
# print("First Delete Item: ",myList.delete_first())
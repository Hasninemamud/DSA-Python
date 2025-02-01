# Stack implementation using LinkedList
class Node:
    def __init__(self, item=None, next=None) :
        self.item = item
        self.next = next
class Stack:
    def __init__(self):
        self.start = None
        self.item_count = 0
        
    
    def is_empty(self):
        return self.start is None
    
    def push(self, data):
        n = Node(data, self.start)
        self.start = n
        self.item_count += 1
    
    def pop(self):
        if self.is_empty():
            print("Stack is Empty")
        poped_item = self.start.item
        self.start = self.start.next
        self.item_count -= 1
        return poped_item
    
    def peek(self):
        if self.is_empty():
            print("Stack is Empty")
            return None
        return print("Top Value is:", self.start.item)
    
    def size(self):
        return print(self.item_count)
        
        
         
        
    
    def display(self):
        if self.is_empty():
            print("Please input value in List")
        else:
            temp = self.start
            while temp is not None:
                print(temp.item, end="-->")
                temp = temp.next  # Move to the next node
            print("None")  # Indicate the end of the list

            
            
                
            

myList = Stack()
myList.push(10)
myList.push(20)
myList.push(30)
myList.push(40)
myList.push(50)
myList.push(60)
myList.display()
myList.pop()
myList.display()
myList.peek()
myList.size()
# print(myList.is_empty())
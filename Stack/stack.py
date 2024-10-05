class Stack:
    def __init__(self, max_size):
        self.values = []
        self.max_size = max_size  # Set the maximum size of the stack

    def push(self, X):
        if not self.is_full():  # Check if stack is full before pushing
            self.values = [X] + self.values
        else:
            return "Stack is full, cannot push."

    def pop(self):
        if not self.is_empty():
            return self.values.pop(0)
        else:
            return "Stack is empty, cannot pop."

    def peek(self):
        if not self.is_empty():
            return self.values[0]
        else:
            return "Stack is empty."

    def is_empty(self):
        return len(self.values) == 0

    def is_full(self):
        return len(self.values) == self.max_size  # Check if stack has reached the maximum size

# Testing the stack with max_size of 3
s = Stack(3)
s.push(10)
s.push(20)
s.push(30)
print(s.push(40))

print("Stack after pushes:", s.values)
print("Is stack full?", s.is_full())  # Checking if stack is full

# Trying to push another element to a full stack
s.push(40)  # This should print a message indicating the stack is full
print("Stack after trying to push:", s.values)

s.pop()
print("Stack after pop:", s.values)
print("Is stack full?", s.is_full())  # Checking if stack is full after pop

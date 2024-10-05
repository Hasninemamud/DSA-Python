from collections import deque

class MyStack:
    def __init__(self):
        # Initialize two queues
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        # Push element to q2
        self.q2.append(x)
        
        # Move all elements from q1 to q2
        while self.q1:
            self.q2.append(self.q1.popleft())
        
        # Swap the names of q1 and q2
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        # Pop the front element from q1
        return self.q1.popleft()

    def top(self) -> int:
        # Peek the front element from q1
        return self.q1[0]

    def empty(self) -> bool:
        # Check if q1 is empty
        return not self.q1

# Example usage:
stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())  # Output: 2
print(stack.pop())  # Output: 2
print(stack.empty())  # Output: False

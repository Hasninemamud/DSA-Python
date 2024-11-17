from heapq import heappop, heappush, heapify, nlargest

# class MaxHeap:
#     def __init__(self, arr=[]):
#         self.max_heap = self.heapify(arr)
              
#     def heapify(self, arr):
#         arr = [-val for val in arr]
#         heapify(arr)
#         return arr
        
#     def push(self, val):
#         # Push the negative of the value to maintain max-heap property
#         heappush(self.max_heap, -val)
    
#     def pop(self):
#         if len(self.max_heap) == 0:
#             raise ValueError("Heap is empty")
#         # Pop the negative of the top value to get the original value
#         return -heappop(self.max_heap)
    
#     def top(self):
#         if len(self.max_heap) == 0:
#             raise ValueError("Heap is empty")
#         # Return the negative of the top value to get the original value
#         return -self.max_heap[0]
    
#     def print_heap(self):
#         # Convert generator to list for proper printing
#         print([ -val for val in self.max_heap])

# # Example usage
# arr = [`10, 24, 4, 70, 34, 45`]
# heap = MaxHeap()
# heap.push(20)
# heap.push(30)
# heap.push(10)
# heap.push(50)
# heap.push(35)
# heap.print_heap()  # Output should show [50, 35, 10, 20, 30] in some order due to heap structure

# heap = MaxHeap(arr)
# heap.push(99)
# heap.print_heap()

arr = [10, 24, 4, 70, 34, 45]
print(nlargest(3, arr))
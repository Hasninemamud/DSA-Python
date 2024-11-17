from heapq import heapify, heappop, heappush
arr = [4, 3, 2, 6]
heap = []
for i in arr:
    heappush(heap, i)

total_cost = 0
while len(heap) > 1:
    first = heappop(heap)
    second = heappop(heap)
    cost = first + second
    total_cost += cost
    heappush(heap, cost)
print(total_cost)
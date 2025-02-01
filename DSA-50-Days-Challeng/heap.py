import heapq

data = [5, 7, 9, 1, 3]
# heapq.heappush(data, 2)
# heapq.heapify(data)
# smallest = heapq.heappop(data)
result = heapq.heappushpop(data, 2)
print(heapq.nsmallest(3, data))
print(heapq.nlargest(3, data))
print(data)
print(result)
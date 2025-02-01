import heapq
def minCost(arr):
    heapq.heapify(arr)
    
    total_cost = 0
    while len(arr)>1:
        rope1 = heapq.heappop(arr)
        rope2 = heapq.heappop(arr)
        
        cost = rope1+rope2
        
        total_cost += cost 
        
        heapq.heappush(arr, cost)
    return total_cost

arr = [3, 2, 4, 5]
print(minCost(arr))
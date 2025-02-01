import heapq

# Function to implement Prim's Algorithm
def prim(graph, start):
    # Min-heap priority queue to get the edge with the smallest weight
    min_heap = []
    heapq.heappush(min_heap, (0, start))  # Start with the arbitrary node, weight 0
    
    # Keep track of vertices included in MST
    in_mst = set()
    
    # Store the MST result
    mst = []
    
    while min_heap:
        weight, node = heapq.heappop(min_heap)
        
        if node not in in_mst:
            in_mst.add(node)
            mst.append((node, weight))
            
            # For every adjacent node of the current node
            for neighbor, edge_weight in graph[node]:
                if neighbor not in in_mst:
                    heapq.heappush(min_heap, (edge_weight, neighbor))
    
    return mst

# Example graph represented as an adjacency list
graph = {
    'A': [('B', 1), ('C', 3), ('D', 4)],
    'B': [('A', 1), ('C', 2)],
    'C': [('A', 3), ('B', 2), ('D', 5)],
    'D': [('A', 4), ('C', 5)],
}

start_node = 'A'
mst = prim(graph, start_node)
print("MST using Prim's Algorithm:", mst) 
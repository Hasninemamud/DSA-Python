import heapq

def prims(graph, start):
    
    mst_heap = []
    
    heapq.heappush(mst_heap,(0, start))
    
    mst = set()
    
    in_mst = []
    
    while mst_heap:
        weight,node = heapq.heappop(mst_heap)
        
        if node not in mst:
            mst.add(node)
            in_mst.append((node, weight))
            
            for neighbot, edge_weight in graph[node]:
                if neighbot not in mst:
                    heapq.heappush(mst_heap,(edge_weight, neighbot))
    return in_mst
        

graph = {
    'A': [('B', 1), ('C', 3), ('D', 4)],
    'B': [('A', 1), ('C', 2)],
    'C': [('A', 3), ('B', 2), ('D', 5)],
    'D': [('A', 4), ('C', 5)],
}


in_mst = prims(graph, 'A')
print("MST using Prim's Algorithm:", in_mst) 
            
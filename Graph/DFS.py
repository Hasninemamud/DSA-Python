def dfs(graph, start_node, visited=None):
    visited = set()
    stack = [start_node]
    
    while stack:
        curent_node= stack.pop()
        
        if curent_node not in visited:
            print(curent_node, end=" ")
            visited.add(curent_node)
            
            for neighbor in reversed(graph[curent_node]):
                if neighbor not in visited:
                    stack.append(neighbor)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
dfs(graph, "A")               
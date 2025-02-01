from collections import deque

def bfs(graph, start_node):
    # Initialize a queue for BFS and a set to track visited nodes
    queue = deque([start_node])
    visited = set([start_node])
    
    # While there are nodes left in the queue to explore
    while queue:
        # Dequeue a node from the front of the queue
        current_node = queue.popleft()
        print(current_node, end=" ")  # Process the node (e.g., print it)

        # Explore all adjacent nodes
        for neighbor in graph[current_node]:
            # If the neighbor has not been visited
            if neighbor not in visited:
                # Mark the neighbor as visited and enqueue 
                visited.add(neighbor)
                queue.append(neighbor)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')

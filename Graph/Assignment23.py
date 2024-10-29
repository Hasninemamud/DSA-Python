class Graph:
    def __init__(self, vertax_count) -> None:
        self.vertax_count = vertax_count
        self.adj_list = [[0]*vertax_count for i in range(vertax_count)]
        
    def add_edge(self, u, v,weight=1):
        if 0<=u<self.vertax_count and 0<=v<self.vertax_count:
            self.adj_list[u][v] = weight
            self.adj_list[v][u] = weight
        else:
            print("Invalid Vertax")
    
    def remove_edge(self, u, v):
        if 0<=u<self.vertax_count and 0<=v<self.vertax_count:
            self.adj_list[u][v] = 0
            self.adj_list[v][u] = 0
        else:
            print("Invalid Vertax")
    
    def has_edge(self, u, v):
        if 0<=u<self.vertax_count and 0<=v<self.vertax_count:
            return self.adj_list[u][v] != 0
        else:
            print("Invalid Vertax")
    
    def print_adj_list(self):
        for row_list in self.adj_list:
            print(" ".join(map(str, row_list)))
        

grp = Graph(5)
grp.add_edge(0, 3)
print(grp.has_edge(0, 3))
# print(grp.remove_edge(0, 3))
grp.print_adj_list()

    
            
            
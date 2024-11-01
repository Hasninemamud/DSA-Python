class Graph:
    def __init__(self, vno):
        self.vertax_so = vno
        self.adj_list = {v: [] for v in range(vno)}
        
    def add_edge(self, u, v, weight =1):
        if 0<=u<self.vertax_so and 0<=v<self.vertax_so:
            self.adj_list[u].append((v, weight))
            self.adj_list[v].append((u, weight))
        else:
            print("Invalid Vertax")
    
    def remove_edge(self, u, v, ):
        if 0<=u<self.vertax_so and 0<=v<self.vertax_so:
            self.adj_list[u]=[(v,weight) for vertax, weight in self.adj_list[u] if vertax!=v]
            self.adj_list[v]=[(u,weight) for vertax, weight in self.adj_list[v] if vertax!=u]   
        else:
            print("Invalid Vertax")
    
    def has_edge(self, u, v):
        if 0<=u<self.vertax_so and 0<=v<self.vertax_so:
            return any(vertax == v for vertax, x in self.adj_list[u])
        else:
            print("Invalid Vertax")
            
    def print_adg_list(self):
        for vartax, n in self.adj_list.items():
            print("V", vartax, ":", n)

grp = Graph(5)
grp.add_edge(2, 3)
grp.print_adg_list()
class Graph:
    def __init__(self, v_no ):
        self.v_no = v_no
        self.adj_matrix = [ [0]*v_no for i in range(v_no) ]
    
    def add_edge(self, u, v, weight=1):
        if 0<=u<self.v_no and 0<=v<self.v_no:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight
        else:
            print("Invalid Vertax")
    
    def remove_edge(self, u, v):
        if 0<=u<self.v_no and 0<=v<self.v_no:
            self.adj_matrix[u][v] = 0
            self.adj_matrix[v][u] = 0
    
    def has_edge(self, u, v):
        if 0<=u<self.v_no and 0<=v<self.v_no:
            return self.adj_matrix[u][v] != 0
        else:
            print("Invalid matrix")
    
    def print_adj_matrix(self):
        for row_list in self.adj_matrix:
            print(" ".join(map(str, row_list)))

mat = Graph(5)
mat.add_edge(0,0)
mat.add_edge(3,4)
mat.remove_edge(3,4)
print(mat.has_edge(1,0))
mat.print_adj_matrix()

        
        
        
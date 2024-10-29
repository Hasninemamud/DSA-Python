class Graph:
    def __init__(self, v_no):
        self.v_no = v_no
        self.adj_matrix = [[0]*v_no for i in range(v_no)]
    
    def add_edge(self, u, v):
        if 0<=u<self.v_no and 0<=u<self.v_no:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1
        else:
            print("Invalid Vertax")
    
    def remove_edge(self, u, v):
        if 0<=u<self.v_no and 0<=u<self.v_no:
            self.adj_matrix[u][v] = 0
            self.adj_matrix[v][u] = 0
        else:
            print("Invalid Vertax")
    
    def has_edge(self, u, v):
        if 0<=u<self.v_no and 0<=u<self.v_no:
            return self.adj_matrix[u][v] != 0
        else:
            print("Invalid Vertax")
            
    def print_matrix(self):
        for row_list in self.adj_matrix:
            print(" ".join(map(str, row_list)))
        
    
      
        
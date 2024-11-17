class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]
        
    def __hash__(self, key):
        return hash(key)%self.size
    
    def insert(self, key, value):
        index = self.__hash__(key)
        
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return 
        self.table[index].append([key, value])
        
    
    def get(self, key):
        index = self.__hash__(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None
    
    def delete(self, key):
        index = self.__hash__(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False
    
    def __str__(self):
        return str(self.table)
        
        
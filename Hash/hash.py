class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)] # Array of lists for chaining

    def _hash(self, key):
        # Simple hash function using the built-in hash and modulo operator
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        # Check if the key already exists and update it if it does
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # If key does not exist, append new (key, value) pair
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  # Key not found

    def delete(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False  # Key not found

    def __str__(self):
        return str(self.table)

# Create a hash table
hash_table = HashTable()

# Insert key-value pairs
hash_table.insert("apple", 10)
hash_table.insert("banana", 20)
hash_table.insert("orange", 30)

# # Retrieve values
# print("Value for 'apple':", hash_table.get("apple"))  # Output: 10
# print("Value for 'banana':", hash_table.get("banana"))  # Output: 20

# # Update value for an existing key
# hash_table.insert("apple", 40)
# print("Updated value for 'apple':", hash_table.get("apple"))  # Output: 40

# # Delete a key
# hash_table.delete("banana")
# print("Value for 'banana' after deletion:", hash_table.get("banana"))  # Output: None

# Print the whole hash table
print("Hash Table:", hash_table)

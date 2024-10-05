class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

n1.next = n2
n2.next = n3
n3.next = n4

start_node = n1

while start_node is not None:
    print(start_node.data, end="->")
    start_node = start_node.next
print("None")

        
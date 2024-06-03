import gc

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Create cyclic references
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3
node3.next = node1  # Circular reference

# Delete references to nodes
del node1
del node2
del node3

# Force garbage collection
gc.collect()

# Check if garbage collection collected the objects
print(gc.garbage)  # Output: []

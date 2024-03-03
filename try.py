import heapq

class Node():
    def __init__(self, state, parent, action, cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

# Create instances of Node with different states represented by letters
node1 = Node('A', None, None, 5)
node2 = Node('B', None, None, 3)
node3 = Node('C', None, None, 7)
node4 = Node('D', None, None, 1)
node5 = Node('E', None, None, 4)


nodes = [] 
heapq.heappush(nodes,node1)
heapq.heappush(nodes,node2)
heapq.heappush(nodes,node3)
heapq.heappush(nodes,node4)
heapq.heappush(nodes,node5)
# Put them in a list
# nodes = [node1, node2, node3, node4, node5]

# Use heapq to sort the nodes based on their costs
heapq.heapify(nodes)

# Pop elements from the heap one by one to get them in sorted order
sorted_nodes = []
while nodes:
    sorted_nodes.append(heapq.heappop(nodes))

# Print sorted nodes
for node in sorted_nodes:
    print(node.state, node.cost)

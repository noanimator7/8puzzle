import heapq
import math
import queue
from collections import deque
goal = ((0, 1, 2), (3, 4, 5), (6, 7, 8))
from helper import * 
class StackFrontier():
    def __init__(self):
        self.frontier = deque()

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            
            return self.frontier.pop()

   
class QueueFrontier:
    def __init__(self):
        self.frontier = queue.Queue()

    def add(self, node):
        self.frontier.put(node)

    def empty(self):
        return self.frontier.empty()

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            
            return self.frontier.get()

def uninformed_search(start, bfs=True):
           # Keep track of number of states explored
        num_explored = 0
        search_depth = 0 

        # Initialize frontier to just the starting position
        start = Node(state=start, parent=None, action=None , level = 0)
        frontier = QueueFrontier() if bfs else StackFrontier()
        frontier.add(start)

        # Initialize an empty explored set
        explored = set()
        frontier_explored = set()

        # Keep looping until solution found
        while True:

            # If nothing left in frontier, then no path
            if frontier.empty():
                raise Exception("no solution")

            # Choose a node from the frontier
            node = frontier.remove()
            # print(node.state)
            num_explored += 1
            search_depth = max(search_depth , node.level)

            # If node is the goal, then we have a solution
            if node.state == goal:
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                solution = (actions, cells)
                return solution , search_depth , num_explored 

            # Mark node as explored
            explored.add(node.state)

            # print("SIU")
            # print(explored.remove())

            # Add neighbors to frontier
            neighbor = neighbors(node.state)
            for state, action in neighbor:
                
                if state not in frontier_explored and state not in explored:
                    child = Node(state=state, parent=node, action=action , level = node.level + 1)
                    frontier.add(child)
                    frontier_explored.add(child)
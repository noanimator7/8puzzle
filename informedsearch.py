import queue
import math
from helper import * 
goal = ((0, 1, 2), (3, 4, 5), (6, 7, 8))

class PQueueFrontier():
    def __init__(self):
        self.frontier = queue.PriorityQueue()

    def add(self, node):
        self.frontier.put(node)

    def empty(self):
        return self.frontier.empty()

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            return self.frontier.get()
def find_element_coordinates(arr, element):
    for i in range(3):
        for j in range(3):
            if arr[i][j] == element:
                return i, j  # Return row and column indices

def h_n_Manhattan(state, goal=[[0, 1, 2], [3, 4, 5], [6, 7, 8]]):
    cost = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                igoal, jgoal = find_element_coordinates(goal, state[i][j])
                cost += abs(igoal - i) + abs(jgoal - j)
                # print(f'from cost function the cost is {cost} , and i=> {igoal} ,and j=> {jgoal} ')
    return cost

def h_n_ecludian(state ,  goal =  goal ):  
    cost = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                igoal, jgoal = find_element_coordinates(goal, state[i][j])
                cost += math.dist( (i,j) , (igoal , jgoal ))
    return cost 


 
def Astar(starts, Eucidean=True):
           # Keep track of number of states explored
        num_explored = 0
        search_depth = 0 

        # Initialize frontier to just the starting position
        h_n = h_n_ecludian if Eucidean else h_n_Manhattan
        start = Node(state=starts, parent=None, action=None , level = 0 )
        frontier = PQueueFrontier()
        frontier.add((h_n(starts), start))

        # Initialize an empty explored set
        # explored = set()
        cost = {}
        cost[starts] = 0

        if start.state == goal:
            return ("",[start.state]),0,1

        # Keep looping until solution found
        while True:

            # If nothing left in frontier, then no path
            if frontier.empty():
                raise Exception("no solution")

            # Choose a node from the frontier
            _, node = frontier.remove()
            # print(node.state)
            num_explored += 1
            search_depth = max(search_depth , node.level)


            # If node is the goal, then we have a solution
            if node.state == goal:
                actions = []
                cells = []
                while node is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                solution = (actions, cells)
                return solution , search_depth , num_explored

            # Add neighbors to frontier
            neighbor = neighbors(node.state)
            for state, action in neighbor:
                new_cost = cost[node.state] + 1
                if state not in cost or new_cost < cost[state]:
                    priority = h_n(state) + new_cost
                    child = Node(state=state, parent=node, action=action  , level= node.level + 1)
                    frontier.add((priority, child))
                cost[state] = new_cost
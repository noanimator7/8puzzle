# from visualizemat import  plot_matrix
import heapq
import math
from collections import deque
class Node():
    def __init__(self, state, parent, action, cost=0 , level = 0  ):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.level = level

    def __lt__(self, other):
        return self.cost < other.cost


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
            # node = self.frontier[-1]
            # self.frontier = self.frontier[:-1]
            # return node
            return self.frontier.pop()
class PQueueFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        heapq.heappush(self.frontier, node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = heapq.heappop(self.frontier)
            # heapq.heapify(self.frontier)
            return node
    def decrease_key(self, state, new_cost):
        # Find the node with the given state
        for i  , node in enumerate(self.frontier):
            if node.state == state:
                if new_cost < node.cost : 
                    # Update the cost of the node
                    # node.cost = new_cost
                    self.frontier[i].cost = new_cost
                    # Re-heapify the frontier
                    heapq.heapify(self.frontier)
                    return
                else :
                    return



class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            # node = self.frontier[0]
            # self.frontier = self.frontier[1:]
            # return node
            return self.frontier.popleft()
goal = ((0, 1, 2), (3, 4, 5), (6, 7, 8))
def dfs(start):

        # Keep track of number of states explored
        num_explored = 0

        # Initialize frontier to just the starting position
        start = Node(state=start, parent=None, action=None)
        frontier = StackFrontier()
        frontier.add(start)

        # Initialize an empty explored set
        explored = set()

        # Keep looping until solution found
        while True:

            # If nothing left in frontier, then no path
            if frontier.empty():
                raise Exception("no solution")

            # Choose a node from the frontier
            node = frontier.remove()
            # print(node.state)
            num_explored += 1

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
                return solution

            # Mark node as explored
            explored.add(tuple(tuple(row) for row in node.state))
            # print("SIU")
            # print(explored.remove())

            # Add neighbors to frontier
            for state, action in neighbors(node.state):
                if not frontier.contains_state(state) and tuple(tuple(row) for row in state) not in explored:
                    # print("here")
                    child = Node(state=state, parent=node, action=action)
                    # print(child.state)
                    frontier.add(child)

def bfs(start):
           # Keep track of number of states explored
        num_explored = 0

        # Initialize frontier to just the starting position
        start = Node(state=start, parent=None, action=None)
        frontier = QueueFrontier()
        frontier.add(start)

        # Initialize an empty explored set
        explored = set()

        # Keep looping until solution found
        while True:

            # If nothing left in frontier, then no path
            if frontier.empty():
                raise Exception("no solution")

            # Choose a node from the frontier
            node = frontier.remove()
            # print(node.state)
            num_explored += 1

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
                return solution

            # Mark node as explored
            explored.add(node.state)
            # print("SIU")
            # print(explored.remove())

            # Add neighbors to frontier
            for state, action in neighbors(node.state):
                if state == goal:
                    actions = [state]
                    cells = [action]
                    while node.parent is not None:
                        actions.append(node.action)
                        cells.append(node.state)
                        node = node.parent
                    actions.reverse()
                    cells.reverse()
                    solution = (actions, cells)
                    return solution
                if not frontier.contains_state(state) and state not in explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)


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


 
def AstarEuclidean(starts):
           # Keep track of number of states explored
        num_explored = 0

        # Initialize frontier to just the starting position

        start = Node(state=starts, parent=None, action=None , cost = h_n_ecludian(starts ))
        frontier = PQueueFrontier()
        frontier.add(start)

        # Initialize an empty explored set
        explored = set()

        # Keep looping until solution found
        while True:

            # If nothing left in frontier, then no path
            if frontier.empty():
                raise Exception("no solution")

            # Choose a node from the frontier
            node = frontier.remove()
            # print(node.state)
            num_explored += 1

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
                return solution

            # Mark node as explored
            explored.add(tuple(tuple(row) for row in node.state))
            # print("SIU")
            # print(explored.remove())

            # Add neighbors to frontier
            for state, action in neighbors(node.state):
                if not frontier.contains_state(state) and tuple(tuple(row) for row in state) not in explored:
                    
                    h_n = h_n_ecludian(state) 
                    g_n = node.level + 1 
                    # print("****************************************************************************************")
                    # print(state)
                    # print(h_n + g_n)
                    child = Node(state=state, parent=node, action=action ,  cost= h_n+ g_n , level= node.level + 1)
                    frontier.add(child)
                elif   frontier.contains_state(state)  :
                    h_n = h_n_ecludian(state) 
                    g_n = node.level  + 1
                    frontier.decrease_key(state, h_n+g_n)
                    
                    




def AstarManhattan(starts):
               # Keep track of number of states explored
        num_explored = 0

        # Initialize frontier to just the starting position

        start = Node(state=starts, parent=None, action=None , cost = h_n_Manhattan(starts ))
        frontier = PQueueFrontier()
        frontier.add(start)

        # Initialize an empty explored set
        explored = set()

        # Keep looping until solution found
        while True:

            # If nothing left in frontier, then no path
            if frontier.empty():
                raise Exception("no solution")

            # Choose a node from the frontier
            node = frontier.remove()
            # print(node.state)
            num_explored += 1

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
                return solution 

            # Mark node as explored
            explored.add(tuple(tuple(row) for row in node.state))
            # print("SIU")
            # print(explored.remove())

            # Add neighbors to frontier
            for state, action in neighbors(node.state):
                if not frontier.contains_state(state) and tuple(tuple(row) for row in state) not in explored:
                    
                    h_n = h_n_Manhattan(state) 
                    g_n = node.level + 1 
                    # print("****************************************************************************************")
                    # print(state)
                    # print(h_n + g_n)
                    child = Node(state=state, parent=node, action=action ,  cost= h_n+ g_n , level= node.level + 1)
                    frontier.add(child)
                elif   frontier.contains_state(state)  :
                    h_n = h_n_Manhattan(state) 
                    g_n = node.level  + 1
                    frontier.decrease_key(state, h_n+g_n)
def get_empty_position(board):
    # print(board)
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

def is_valid_move(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def neighbors(state):
    moves = []
    empty_x, empty_y = get_empty_position(state)

    directions = [(0, 1, 'L'), (0, -1, 'R'), (-1, 0, 'D'), (1, 0, 'U')]

    for dx, dy, action in directions:
        new_x, new_y = empty_x + dx, empty_y + dy
        if is_valid_move(new_x, new_y):
            new_state = []
            for i in range(3):
                row = []
                for j in range(3):
                    if (i, j) == (empty_x, empty_y):
                        row.append(state[new_x][new_y])
                    elif (i, j) == (new_x, new_y):
                        row.append(0)
                    else:
                        row.append(state[i][j])
                new_state.append(tuple(row))

            moves.append((tuple(new_state), f"{new_x}{new_y}{action}"))

    return moves

    
    return moves


def getInvCount(arr):
    newarr =  [] 
    for i in range (3) : 
        for j in range(3) : 
            newarr.append(arr[i][j])
    inv_count = 0
    empty_value = 0 
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if newarr[j] != empty_value and newarr[i] != empty_value and newarr[i] > newarr[j]:
                inv_count += 1
    return inv_count

# if odd no of inversions ==> unsolvable   example ==>  [[1, 2, 3], [4, 5, 6], [8,7,0]]
initial_state = ((8 , 6, 7), (2, 5, 4), (3, 0, 1))
# if (getInvCount(initial_state) % 2  != 0 ) :  
#     print("No solution")
# else:   
# (actions, cells )= AstarEuclidean(initial_state)
i = 0 
# # # plot_matrix(cells , goal, f'E:/ai1/puzzle_animation{i}.gif')
# i += 1
# for cell in cells: 
#     for row in cell: 
#         print(row )
#     print ()
# print(len(cells) )
# print("****************************************************")

(actions, cells)= bfs(initial_state)
# i = 0 
# plot_matrix(cells , goal, f'E:/ai1/puzzle_animation{i}.gif')
i += 1
for cell in cells : 
    for row in cell : 
        print(row )
    print ()
print(len(cells))
print("****************************************************")
(actions, cells )= AstarManhattan(initial_state)
# plot_matrix(cells , goal, f'E:/ai1/puzzle_animation{i}.gif')
i += 1
for cell in cells : 
    for row in cell : 
        print(row )
    print ()
print(len(cells))
# print("****************************************************")

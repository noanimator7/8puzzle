# from visualizemat import  plot_matrix
import heapq
import math
import queue
from collections import deque
goal = ((0, 1, 2), (3, 4, 5), (6, 7, 8))
class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

    def __lt__(self, other):
        return self.state < other.state


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

        # Initialize frontier to just the starting position
        start = Node(state=start, parent=None, action=None)
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
            neighbor = neighbors(node.state)
            for state, action in neighbor:
                
                if state not in frontier_explored and state not in explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)
                    frontier_explored.add(child)


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

        # Initialize frontier to just the starting position
        h_n = h_n_ecludian if Eucidean else h_n_Manhattan
        start = Node(state=starts, parent=None, action=None , cost=h_n(starts))
        frontier = PQueueFrontier()
        frontier.add((h_n(starts), start))

        # Initialize an empty explored set
        # explored = set()
        cost = {}
        cost[starts] = 0

        # Keep looping until solution found
        while True:

            # If nothing left in frontier, then no path
            if frontier.empty():
                raise Exception("no solution")

            # Choose a node from the frontier
            _, node = frontier.remove()
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

            # Add neighbors to frontier
            neighbor = neighbors(node.state)
            for state, action in neighbor:
                new_cost = cost[node.state] + 1
                if state not in cost or new_cost < cost[state]:
                    priority = h_n(state) + new_cost
                    child = Node(state=state, parent=node, action=action , level= node.level + 1)
                    frontier.add((priority, child))
                cost[state] = new_cost
               
                    
                    
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
import time 
# if odd no of inversions ==> unsolvable   example ==>  [[1, 2, 3], [4, 5, 6], [8,7,0]]
initial_state = ((8, 6, 7), (2, 5, 4), (3, 0, 1))
if (getInvCount(initial_state) % 2  != 0 ) :  
    print("No solution")
else:   
    start = time.time()
    (actions, cells )= uninformed_search(initial_state, bfs=False)
    end = time.time()
    i = 0 
    # # # # plot_matrix(cells , goal, f'E:/ai1/puzzle_animation{i}.gif')
    i += 1
    for cell in cells: 
        for row in cell: 
            print(row )
        print ()
    print(f"Number of steps: {len(cells)} time taken: {(end - start) / 60} minutes by A* algorithm with Euclidean heuristic")
    # print("****************************************************")
    # start2 = time.time()
    # (actions, cells)= dfs(initial_state)
    # end2 = time.time()
    # i = 0 
    # # # plot_matrix(cells , goal, f'E:/ai1/puzzle_animation{i}.gif')
    # i += 1
    # for cell in cells : 
    #     for row in cell : 
    #         print(row )
    #     print ()
    # print(f"Number of steps: {len(cells)} time taken: {(end2 - start2) / 60} minutes  by DFS algorithm")
    # print("****************************************************")
#     start3 = time.time()
#     (actions, cells )= AstarManhattan(initial_state)
#     end3 = time.time()
#     # plot_matrix(cells , goal, f'E:/ai1/puzzle_animation{i}.gif')
#     i += 1
#     for cell in cells : 
#         for row in cell : 
#             print(row )
#         print ()
#     print(f"Number of steps: {len(cells)} time taken: {(end3 - start3) / 60} minutes by A* algorithm with manhattan heuristic")
# # print("****************************************************")

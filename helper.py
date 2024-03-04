import math
class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

    def __lt__(self, other):
        return self.state < other.state
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
    
# from visualizemat import  plot_matrix
from visualizemat import   *
import time 
from uninformedsearch import  * 
from informedsearch import  * 
from helper import  * 
i = 0 
goal = ((0, 1, 2), (3, 4, 5), (6, 7, 8))

while True : 
    # if odd no of inversions ==> unsolvable   example ==>  [[1, 2, 3], [4, 5, 6], [8,7,0]]
    initial_state = ((8, 6, 7), (2, 5, 4), (3, 0, 1))
    if (getInvCount(initial_state) % 2  != 0 ) :  
        print("No solution")
    else:   
        x = input("Which algorithm to use?\n1) DFS\n2) BFS\n3) A* with Euclidean Distance\n4) A* with Manhattan Distance\n5)EXIT")
        
        if x == '1':
            print("You chose DFS.")
            start = time.time()
            (actions, cells )= uninformed_search(initial_state, bfs=False)
            end = time.time()
            i += 1
            for cell in cells: 
                for row in cell: 
                    print(row )
                print ()
            print(f"Number of steps: {len(cells)} time taken: {(end - start) / 60} minutes by DFS")
            # break
            git plot_matrix(cells , goal, f'E:/ai1/8puzzle/puzzle_animation{i}.gif')

            
        elif x == '2':
            print("You chose BFS.")
            start = time.time()
            (actions, cells )= uninformed_search(initial_state, bfs= True)
            end = time.time()
            plot_matrix(cells , goal, f'E:/ai1/8puzzle/puzzle_animation{i}.gif')
            i += 1
            for cell in cells: 
                for row in cell: 
                    print(row )
                print ()
            print(f"Number of steps: {len(cells)} time taken: {(end - start) / 60} minutes by BFS")
            # break
        elif x == '3':
            print("You chose A* with Euclidean Distance.")
            start = time.time()
            (actions, cells )= Astar(initial_state, True)
            end = time.time()
            plot_matrix(cells , goal, f'E:/ai1/8puzzle/puzzle_animation{i}.gif')
            i += 1
            for cell in cells: 
                for row in cell: 
                    print(row )
                print ()
            print(f"Number of steps: {len(cells)} time taken: {(end - start) / 60} minutes by A* algorithm with Euclidean heuristic")
            # break
        elif x == '4':
            print("You chose A* with Manhattan Distance.")
            start = time.time()
            (actions, cells )= Astar(initial_state, False)
            end = time.time()
            plot_matrix(cells , goal, f'E:/ai1/8puzzle/puzzle_animation{i}.gif')
            i += 1
            for cell in cells: 
                for row in cell: 
                    print(row )
                print ()
            print(f"Number of steps: {len(cells)} time taken: {(end - start) / 60} minutes by A* algorithm with Manhattan heuristic")
            # break
        elif x == '5' : 
            break  
        else:
            print("Invalid input. Please choose a number from 1 to 4.")

 

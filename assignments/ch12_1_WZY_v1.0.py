## This is course material for Introduction to Python Scientific Programming
## Class 9 Example code: knight_path_DFS.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

from collections import deque
import random
import math

def DFS(board_size, start, goal, legit_moves, current_move):
    ''' DFS search a viable path from start position to goal position on the board_size
    Parameters:
    Input:  board_size  - The dimension of the board
            start       - start position of the piece
            goal        - final destination
            legit_moves - describe how the piece can move on the board
    
    Output: result_path - return a DFS path that reaches the goal, otherwise []
    '''
    # Input sanity check
    if len(board_size)!=2 or type(board_size[0])!=int or type(board_size[1])!=int:#检查棋盘大小及其数字输入的合法性
        raise TypeError('Board size is not a compatible type')
    elif board_size[0]<=0 or board_size[1]<=0:#检查棋盘大小
        raise ValueError('Board size value is not supported')

    if len(start)!=2 or type(start[0])!=int or type(start[1])!=int:#检查起点大小及其数字输入的合法性
        raise TypeError('Start position is not a compatible type')
    elif start[0]<0 or start[1]<0 or start[0]>=board_size[0] or start[1]>=board_size[1]:#检查起点是否超过棋盘
        raise ValueError('Start position value is not supported')

    if len(goal)!=2 or type(goal[0])!=int or type(goal[1])!=int:#检查终点输入合法性
        raise TypeError('Goal position is not a compatible type')
    elif goal[0]<0 or goal[1]<0 or goal[0]>=board_size[0] or goal[1]>=board_size[1]:#检查终点是否超过棋盘
        raise ValueError('Start position value is not supported')

    # Initialization
    search_stack = deque()    #最佳路径走法
    search_stack.append(start)#将起点添加至最佳路径

    parent_map  = [[[None,None] for i in range(board_size[1])] for j in range(board_size[0])]#创建一个棋盘
    is_goal = False#到达终点设置为否
    
    while len(search_stack)>0 and not is_goal:#当最佳路径走法长度大于0且不在终点上
       
        previous_move = current_move#先前的位置等于现在的位置
        current_move = search_stack.pop()#将现在的位置从最佳路径走法中生成
        parent_map[current_move[0]][current_move[1]] = previous_move#在地图上添加上一步的坐标,即我从哪里来的
        temp_stack=[]
        for i in legit_moves:#生成所有合法路径
            
            move_position = [ current_move[0] + i[0],current_move[1] + i[1]]#生成一个合法路径

            if move_position[0]<0 or move_position[1]<0 or move_position[0]>=board_size[0] \
                or move_position[1]>=board_size[1]:#如果超出棋盘外
                continue#继续循环
            elif parent_map[move_position[0]][move_position[1]]!=[None, None]:#如果路径已经走过
                continue#继续循环
            else:
                temp_stack.append(move_position)

        best_position=temp_stack[0]

        for i in temp_stack:
            absolute_distance=math.sqrt(abs(goal[0]-best_position[0])**2+abs(goal[1]-best_position[1])**2)
            temp_distance=math.sqrt(abs(goal[0]-i[0])**2+abs(goal[1]-i[1])**2)
            if absolute_distance>temp_distance:
                best_position=i
            else:
                continue

        search_stack.append(best_position)

        if best_position == goal:#如果到达终点,所有循环停止
            parent_map[move_position[0]][move_position[1]] = current_move
            is_goal = True
            break
        
    path_queue = deque()#新建一个路径
    if is_goal:#如果到了终点
        while is_goal:
            path_queue.appendleft(move_position)#添加当前的位置
            move_position = parent_map[move_position[0]][move_position[1]]#将当前的位置移至上一个位置
            if move_position[0]==-1:#如果到达起点
                is_goal = False#循环中止
            
    return path_queue

board_size = [8,8]#确认棋盘大小
current_move = [-1, -1]#确认起始位置

#编写合法路径
knight_moves = [[-2,-1], [-1,-2], [1,-2],[2,-1], [2,1], [1,2], [-1,2], [-2,1]]
bishop_moves = [[1,1],[-1,1],[1,-1],[-1,-1],\
               [2,2],[-2,2],[2,-2],[-2,-2],\
               [3,3],[-3,3],[3,-3],[-3,-3],\
               [4,4],[-4,4],[4,-4],[-4,-4],\
               [5,5],[-5,5],[5,-5],[-5,-5],\
               [6,6],[-6,6],[6,-6],[-6,-6],\
               [7,7],[-7,7],[7,-7],[-7,-7],\
               [8,8],[-8,8],[8,-8],[-8,-8]]
castle_moves = [[0,1],[0,-1],[1,0],[-1,0],\
               [0,2],[0,-2],[2,0],[-2,0],\
               [0,3],[0,-3],[3,0],[-3,0],\
               [0,4],[0,-4],[4,0],[-4,0],\
               [0,5],[0,-5],[5,0],[-5,0],\
               [0,6],[0,-6],[6,0],[-6,0],\
               [0,7],[0,-7],[7,0],[-7,0],\
               [0,8],[0,-8],[8,0],[-8,0]]
queen_moves = [[0,1],[0,-1],[1,0],[-1,0],\
               [0,2],[0,-2],[2,0],[-2,0],\
               [0,3],[0,-3],[3,0],[-3,0],\
               [0,4],[0,-4],[4,0],[-4,0],\
               [0,5],[0,-5],[5,0],[-5,0],\
               [0,6],[0,-6],[6,0],[-6,0],\
               [0,7],[0,-7],[7,0],[-7,0],\
               [0,8],[0,-8],[8,0],[-8,0],\
               [1,1],[-1,1],[1,-1],[-1,-1],\
               [2,2],[-2,2],[2,-2],[-2,-2],\
               [3,3],[-3,3],[3,-3],[-3,-3],\
               [4,4],[-4,4],[4,-4],[-4,-4],\
               [5,5],[-5,5],[5,-5],[-5,-5],\
               [6,6],[-6,6],[6,-6],[-6,-6],\
               [7,7],[-7,7],[7,-7],[-7,-7],\
               [8,8],[-8,8],[8,-8],[-8,-8]]
king_moves = [[1,1],[1,-1],[-1,1],[-1,-1],\
               [0,-1],[0,1],[1,0],[-1,0]]
pieces_moves = castle_moves          

#确定开始位置
pieces_start = [0,0]

# Create a display of the board game problem
print('Game has started, here is the board with the initial position at 0')
board_display = [[' * ' for i in range(board_size[1])] for j in range(board_size[0])]
board_display[pieces_start[0]][pieces_start[1]] = ' S '
for i in range(board_size[0]):
    display_string = ''.join(board_display[i])
    print(display_string)

# Acquire user input about the goal position
user_input = input('Please input goal position (x, y): ')
pieces_goal = list(eval(user_input))

print('Moving Pieces from {0} to {1}:'.format(pieces_start, pieces_goal))
board_display[pieces_goal[0]][pieces_goal[1]]  = ' G '

pieces_path = DFS(board_size, pieces_start, pieces_goal, pieces_moves, current_move)

print(pieces_path)
if len(pieces_path)>0:
    start = pieces_path.popleft()
    pieces_path.append(start)
    for i in range(1,len(pieces_path)-1):
        current_move = pieces_path.popleft()
        board_display[current_move[0]][current_move[1]]  = ' o '
        pieces_path.append(current_move)
        
for i in range(board_size[0]):
    display_string = ''.join(board_display[i])
    print(display_string)
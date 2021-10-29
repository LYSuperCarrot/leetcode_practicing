from DataStructure_queue import Queue
from DataStructure_stack import Stack
from collections import deque

maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,0,0,1,1,0,0,1],
    [1,0,1,1,1,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,1,0,1],
    [1,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]

dirs = [
	lambda x,y: (x+1,y),
	lambda x,y: (x-1,y),
	lambda x,y: (x,y-1),
	lambda x,y: (x,y+1)
]

def recall_stack_maze(maze, x1, y1, x2, y2):
    stack = []
    stack.append((x1, y1))
    while len(stack) > 0:
        cur_node = stack[-1]
        if cur_node[0] == x2 and cur_node[1] == y2:
            for p in stack:
                print(p)
            return True
        
        for dir in dirs:
            next_node = dir(cur_node[0], cur_node[1])
            if maze[next_node[0]][next_node[1]] == 0:
                stack.append(next_node)
                maze[next_node[0]][next_node[1]] = 2
                break
        else:
            maze[cur_node[0]][cur_node[1]] = 2
            stack.pop()
    else:
        print("no path to maze exit")
        return False
    


def print_r(path):
    cur_node = path[-1]
    realpath = []
    while cur_node[2] != -1:
        realpath.append(cur_node[0:2])
        cur_node = path[cur_node[2]]
    
    realpath.append(cur_node[0:2])
    realpath.reverse()
    for p in realpath:
        print(p)
            

def extent_queue_maze(maze, x1, y1, x2, y2):
    path = []
    queue = deque()
    queue.append((x1, y1, -1))
    while len(queue) > 0:
        cur_node = queue.popleft()
        path.append(cur_node)
        if cur_node[0] == x2 and cur_node[1] == y2:
            print_r(path)
            return True
        
        for dir in dirs:
            next_node = dir(cur_node[0], cur_node[1])
            if maze[next_node[0]][next_node[1]] == 0:
                queue.append((next_node[0], next_node[1], len(path)-1))
                maze[next_node[0]][next_node[1]] = 2
    else:
        print("没有路")
        return False



# recall_stack_maze(maze,1,1,8,8)

print(extent_queue_maze(maze, 1, 1, 8, 8))

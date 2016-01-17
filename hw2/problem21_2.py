"""
Author:
Xinyi Ma xim002@ucsd.edu
Yijun Zhang yiz160@ucsd.edu
"""

import sys
import fileinput
from collections import deque

# Problem21_1 Checking for valid input
for line in fileinput.input():

    try:
        arrangement = [int(x.strip()) for x in line.split(',')]
        print(arrangement)

    except:
        sys.exit('invalid input')

    # more than 3 numbers in the same line
    if len(arrangement) > 3:
        sys.exit('invalid input')

    # initial state not valid
    for k in range(0, 3):
        if arrangement[k] not in [0, 1]:
            sys.exit('invalid input')

    # determine whether the state is a goal state
    if arrangement[0] is 0 and arrangement[1] is 0:
        print('')
        sys.exit()

# Problem21_2  BFS
    frontier = deque([arrangement])
    visited = [arrangement]
    path = {}
    path[tuple(arrangement)] = ''
    action = 'LRS'

    while len(frontier) != 0:
        node = frontier.popleft()
        room = node[2]

        #find goal state
        if node[0] == 0 and node[1] == 0:
            print(path[tuple(node)])
            sys.exit()
        
        step = path[tuple(node)]

        for act in action:
            if act == 'S':
                temp = list(node)
                temp[room] = 0
            elif act == 'R':
                temp = list(node)
                temp[2] = 1
            elif act == 'L':
                temp = list(node)
                temp[2] = 0

            if temp in visited:
                continue
            else:
                frontier.append(temp)
                visited.append(temp)
                path[tuple(temp)] = step + act

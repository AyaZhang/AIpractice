"""
author:
Xinyi Ma xim002@ucsd.edu
Yijun Zhang yiz160@ucsd.edu
Yuanchi Ha yuha@ucsd.edu
"""

import sys
import fileinput

# Problem21_1
count = 0
for line in fileinput.input():
    count += 1

# more than 1 line
if count > 1:
    sys.exit('invalid input')

for line in fileinput.input():

    try:
        arrangement = [int(x.strip()) for x in line.split(',')]

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
        print ''
        sys.exit()

#Problem21_3
    frontier = [arrangement]
    visited = []
    path = {}
    path[id(arrangement)] = ''
    action = 'SRL'

    while len(frontier) != 0:
        node = frontier.pop()
        room = node[2]
        visited.append(node)

        #find goal state
        if node[0] == 0 and node[1] == 0:
            print path[id(node)]
            sys.exit()
        
        step = path[id(node)]

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
                path[id(temp)] = step + act

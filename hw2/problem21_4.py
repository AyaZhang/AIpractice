"""
author:
Xinyi Ma xim002@ucsd.edu
Yijun Zhang yiz160@ucsd.edu
Yuanchi Ha yuha@ucsd.edu
"""

import sys
import fileinput

#Problem21_1
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
        print('')
        sys.exit()

#Problem21_4 depth-limit search
    frontier = [arrangement]
    visited = [arrangement]
    path = {}
    path[tuple(arrangement)] = ''
    action = 'SRL'
    depth = 0

    while len(frontier) != 0 and depth < 5:
        node = frontier.pop()
        depth += 1
        room = node[2]

        #find goal state
        if node[0] == 0 and node[1] == 0:
            print(path[tuple(node)])
            sys.exit()
        
        room=node[2]
        step=path[tuple(node)]
        for act in action:
            if act=='S':
                temp=list(node)
                temp[room]=0
            elif act=='R':
                temp=list(node)
                temp[2]=1
            elif act=='L':
                temp=list(node)
                temp[2]=0

            if temp in visited:
                continue
            else:
                frontier.append(temp)
                visited.append(temp)
                path[tuple(temp)]=step+act
    print('None')

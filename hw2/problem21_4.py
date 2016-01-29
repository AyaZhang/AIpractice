"""
author:
Xinyi Ma xim002@ucsd.edu
Yijun Zhang yiz160@ucsd.edu
Yuanchi Ha yuha@ucsd.edu
"""

import sys
import fileinput

""" 
this method checks whether the algorithm has reached goal state 
"""
def is_goal(state):
    for i in state[:-1]:
        if i != 0:
            return False
    return True

""" 
this method performs depth limited search from a given start state
"""
def depth_limited_search(node, depth, path):
    if node in visited:
        return (None, path)

    if is_goal(node):
        return (node, path)

    visited.append(node)

    action = 'LRS'

    if depth > 0:
        for act in action:

            child = list(node)

            if act == 'L':
                if child[2] > 0:
                    child[2] = 0
            
            elif act == 'R':
                if child[2] < len(node) - 2:
                    child[2] = 1

            elif act == 'S':
                if child[child[2]] != 0:
                    child[child[2]] = 0
            
            if child == node:
                continue
            
            to_return = depth_limited_search(child, depth - 1, path + act)
            
            if to_return[0] is not None:
                return to_return

    return (None, path)

for line in fileinput.input():
    try:
        arrangement = [int(x.strip()) for x in line.split(',')]

    except ValueError:
        sys.exit('invalid input')

    # more than 3 numbers in the same line
    if len(arrangement) > 3:
        sys.exit('invalid input')

    # initial state not valid
    for k in range(0, 3):
        if arrangement[k] not in [0, 1]:
            sys.exit('invalid input')
    
    # determine whether the state is a goal state
    if is_goal(arrangement):
        print ''
        sys.exit()

    solution = ''
    visited = list()

    found = depth_limited_search(arrangement, 5, solution)

    if found[0] is not None:
        print found[1]
        sys.exit()

    print 'None'
    sys.exit()

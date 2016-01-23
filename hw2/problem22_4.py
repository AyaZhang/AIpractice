"""
author:
Xinyi Ma xim002@ucsd.edu
Yijun Zhang yiz160@ucsd.edu
Yuanchi Ha yuha@ucsd.edu
"""

import sys
import fileinput

def is_goal(state):
    for i in state[:-1]:
        if i != 0:
            return False
    return True

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
                if child[-1] > 0:
                    child[-1] -= 1
            
            elif act == 'R':
                if child[-1] < len(node) - 2:
                    child[-1] += 1

            elif act == 'S':
                if child[child[-1]] != 0:
                    child[child[-1]] = 0
            
            if child == node:
                continue
            
            to_return = depth_limited_search(child, depth - 1, path + act)
            
            if to_return[0] is not None:
                return to_return

    return (None, path)
    
    
for line in fileinput.input():
    try:
        arrangement = [int(x.strip()) for x in line.split(',')]
        length = len(arrangement)

    except ValueError:
        sys.exit('invalid input')

    # initial state not valid
    for k in range(0, length-1):
        if arrangement[k] not in [0, 1]:
            sys.exit('invalid input')
    if arrangement[length-1] >= length-1:
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

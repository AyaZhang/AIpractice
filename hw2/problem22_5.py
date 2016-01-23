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
    

    if depth == 0 and is_goal(node):
        return (node, path)

    action = 'LRS'

    if depth > 0:
        for act in action:
            if act == 'S':
                child = list(node)
                if child[child[length-1]] == 0:
                    continue
                else:
                    child[child[length-1]] = 0
            
            elif act == 'R':
                child = list(node)
                if child[length-1] < length - 2:
                    child[-1] += 1
                else:
                    continue
            
            elif act == 'L':
                child = list(node)
                if child[length-1] > 0:
                    child[-1] -= 1
                else:
                    continue
            
            to_return = depth_limited_search(child, depth - 1, path + act)
            
            if to_return[0] is not None:
                return to_return

    return (None, path)

#Problem22_1
for line in fileinput.input():

    try:
        arrangement = [int(x.strip()) for x in line.split(',')]
        length = len(arrangement)

    except ValueError:
        sys.exit('invalid input')


    for k in range(0, length - 1):
        if arrangement[k] not in [0, 1]:
            sys.exit('invalid input')
    if arrangement[length - 1] >= length - 1:
        sys.exit('invalid input')
    
    # determine whether the state is a goal state
    if is_goal(arrangement):
        print ''
        sys.exit()

    solution = ''

    for limit in range(0, 8):

        found = depth_limited_search(arrangement, limit, solution)

        if found[0] is not None:
            print found[1]
            sys.exit()

    print 'None'
    sys.exit()

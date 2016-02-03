"""
author:
Xinyi Ma xim002@ucsd.edu
Yijun Zhang yiz160@ucsd.edu
Yuanchi Ha yuha@ucsd.edu
"""
import sys
import fileinput

""" 
this method performs depth limited search for each iterative step
"""
def depth_limited_search(node, depth, path):

    if depth == 0 and node[0] == 0 and node[1] == 0:
        return (node, path)

    action = 'SRL'

    if depth > 0:
        for act in action:
            if act == 'L':
                child = list(node)
                child[2] = 0
            elif act == 'R':
                child = list(node)
                child[2] = 1
            elif act == 'S':
                child = list(node)
                child[child[2]] = 0

            if child == list(node):
                continue

            path += act
            to_return = depth_limited_search(child, depth - 1, path)
            
            if to_return[0] is not None:
                return to_return

    return (None, path)

def problem21_5():
    #Problem21_1
    #for line in fileinput.input():
    line = sys.stdin.readline()
    try:
        arrangement = [int(x.strip()) for x in line.split(', ')]

    except ValueError:
        return 'invalid input'

    # more than 3 numbers in the same line
    if len(arrangement) > 3:
        return 'invalid input'

    # initial state not valid
    for k in range(0, 3):
        if arrangement[k] not in [0, 1]:
            return 'invalid input'

    # determine whether the state is a goal state
    if arrangement[0] is 0 and arrangement[1] is 0:
        return ''

    solution = ''

    for current_depth in range(0, 8):
        
        found = depth_limited_search(arrangement, current_depth, solution)

        if found[0] is not None:
            return found[1]

    return 'None'

print(problem21_5())

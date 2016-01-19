"""
author:
Xinyi Ma xim002@ucsd.edu
Yijun Zhang yiz160@ucsd.edu
Yuanchi Ha yuha@ucsd.edu
"""
import sys
import fileinput

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
            found = depth_limited_search(child, depth - 1, path)
            
            if found[0] is not None:
                return found

    return (None, path)

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

    path = ''

    for depth in range(0, 8):

        found = depth_limited_search(arrangement, depth, path)

        if found[0] is not None:
            print(found[1])
            sys.exit()

    print('None')
    sys.exit()

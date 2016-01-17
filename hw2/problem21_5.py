"""
author:
Xinyi Ma xim002@ucsd.edu
"""
from DFS import*
import sys
import fileinput
#Problem21_1
for line in fileinput.input():

    try:
        arrangement = [int(x.strip()) for x in line.split(',')]
        print arrangement

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
        print('True')
        sys.exit()
    else:
        print('False')

#Problem21_5 iterative deepening DFS
for i in range(1,9):
    path=depth_first_search(arrangement,i)
    print path








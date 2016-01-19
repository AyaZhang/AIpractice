"""
author:
Yijun Zhang yiz160@ucsd.edu
"""

import sys
import fileinput
from queue import PriorityQueue

class Node:

    def __init__(self, state, cost):
        self.state = state
        self.cost = 0
        self.heuristic = state[0] + state[1]

    def __cmp__(self, other):
        myf = self.cost + self.heuristic
        otherf = other.cost + other.heuristic
        return cmp(myf, otherf)

    def successors():
        left = list(arrangement)
        left[2] = 0
        left_successor = Node(left, self.cost + 1)

        right = list(arrangement)
        right[2] = 1
        right_successor = Node(right, self.cost + 1)

        suck = list(arrangement)
        suck[arrangement[2]] = 0
        suck_successor = Node(suck, self.cost + 1)

        return [left_successor, right_successor, suck_successor]


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

    # A* search
    openlist = PriorityQueue()
    closelist = []

    start = Node(arrangement, 0)
    openlist.put(start)

    while not openlist.empty():
        q = openlist.get()

        for child in q.successors():
            
"""
author:
Yijun Zhang yiz160@ucsd.edu
Xinyi Ma xim002@ucsd.edu
Yuanchi Ha yuha@ucsd.edu
"""

import sys
import fileinput
from queue import PriorityQueue

class Node:

    def __init__(self, state, cost, path):
        self.state = state
        self.cost = 0
        self.heuristic = state[0] + state[1]
        self.path = path

    def __lt__(self, other):
        myf = self.cost + self.heuristic
        otherf = other.cost + other.heuristic
        return myf < otherf

    def successors(self):
        left = list(self.state)
        left[2] = 0
        step = self.path + 'L'
        left_successor = Node(left, self.cost + 1, step)

        right = list(self.state)
        right[2] = 1
        step = self.path + 'R'
        right_successor = Node(right, self.cost + 1, step)

        suck = list(self.state)
        suck[suck[2]] = 0
        step = self.path + 'S'
        suck_successor = Node(suck, self.cost + 1, step)

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

    start = Node(arrangement, 0, '')
    openlist.put(start)

    while not openlist.empty():
        q = openlist.get()

        for child in q.successors():
            if child.state[0] == 0 and child.state[1] == 0:
                print(child.path)
                sys.exit()

            if child.state == q.state:
               continue

            for i in openlist.queue:
                if i < child:
                    continue

            for j in closelist:
                if j < child:
                    continue
            
            openlist.put(child)

        closelist.append(q)

    print('None')
    sys.exit()

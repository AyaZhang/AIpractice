"""
author:
Yijun Zhang yiz160@ucsd.edu
Xinyi Ma xim002@ucsd.edu
Yuanchi Ha yuha@ucsd.edu
"""

import sys
import fileinput
from Queue import PriorityQueue

class Node:

    def __init__(self, state, cost, path, order):
        self.state = state
        self.cost = cost
        self.heuristic = sum(state[:-1])
        self.path = path
        self.order = order

    def __lt__(self, other):
        myf = self.cost + self.heuristic
        otherf = other.cost + other.heuristic
        if myf != otherf:
            return myf < otherf
        else:
            return self.order < other.order

    def successors(self):
        toRet = []
        global insertion_order 

        left = list(self.state)
        if left[-1] > 0:
            left[-1] -= 1
            step = self.path + 'L'
            insertion_order += 1
            left_successor = Node(left, self.cost + 1, step, insertion_order)
            toRet.append(left_successor)

        right = list(self.state)
        if right[-1] < len(right) - 2:
            right[-1] += 1
            step = self.path + 'R'
            insertion_order += 1
            right_successor = Node(right, self.cost + 1, step, insertion_order)
            toRet.append(right_successor)

        suck = list(self.state)
        if suck[suck[len(suck) - 1]]!= 0:
            suck[suck[len(suck) - 1]] = 0
            step = self.path + 'S'
            insertion_order += 1
            suck_successor = Node(suck, self.cost + 1, step, insertion_order)
            toRet.append(suck_successor)

        return toRet

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
        print ''
        sys.exit()

    # A* search
    openlist = PriorityQueue()
    closelist = []
    insertion_order = 0

    start = Node(arrangement, 0, '', 0)
    openlist.put(start)

    while not openlist.empty():
        q = openlist.get()

        for child in q.successors():
            if child.state[0] == 0 and child.state[1] == 0:
                print child.path
                sys.exit()

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

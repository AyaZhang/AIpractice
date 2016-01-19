"""
author:
Yijun Zhang yiz160@ucsd.edu
"""

import sys
import fileinput
from queue import PriorityQueue

class Node:

    def __init__(self, state, cost, path):
        self.state = state
        self.cost = cost
        self.heuristic = sum(state[:-1])
        self.path = path

    def __lt__(self, other):
        myf = self.cost + self.heuristic
        otherf = other.cost + other.heuristic
        return myf < otherf

    def successors(self):
        left = list(self.state)
        if left[-1] > 0:
            left[-1] -= 1
        step = self.path + 'L'
        left_successor = Node(left, self.cost + 1, step)

        right = list(self.state)
        if right[-1] < len(right) - 2:
            right[-1] += 1
        step = self.path + 'R'
        right_successor = Node(right, self.cost + 1, step)

        suck = list(self.state)
        suck[suck[len(suck) - 1]] = 0
        step = self.path + 'S'
        suck_successor = Node(suck, self.cost + 1, step)

        return [left_successor, right_successor, suck_successor]

def isGoal(state):
    flag = True

    for k in range(0, len(state) - 1):
        if state[k] == 1:
            flag = False
            break

    return flag

#Problem21_1
for line in fileinput.input():

    try:
        arrangement = [int(x.strip()) for x in line.split(',')]

    except:
        sys.exit('invalid input')

    # initial state not valid
    length = len(arrangement)
    for k in range(0, length - 1):
        if arrangement[k] not in [0, 1]:
            sys.exit('invalid input')

    if arrangement[length - 1] >= length - 1:
        sys.exit('invalid input')

    # determine whether the state is a goal state
    if isGoal(arrangement):
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
            if isGoal(child.state):
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
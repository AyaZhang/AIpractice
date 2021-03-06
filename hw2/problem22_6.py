"""
author:
Yijun Zhang yiz160@ucsd.edu
Xinyi Ma    xim002@ucsd.edu
"""

import sys
import fileinput
from Queue import PriorityQueue

openlist = PriorityQueue()
closelist = []
insertion_order = 0

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
        to_return = []
        global insertion_order 

        left = list(self.state)
        if left[-1] > 0:
            left[-1] -= 1
            step = self.path + 'L'
            insertion_order += 1
            left_successor = Node(left, self.cost + 1, step, insertion_order)
            to_return.append(left_successor)

        right = list(self.state)
        if right[-1] < len(right) - 2:
            right[-1] += 1
            step = self.path + 'R'
            insertion_order += 1
            right_successor = Node(right, self.cost + 1, step, insertion_order)
            to_return.append(right_successor)

        suck = list(self.state)
        if suck[suck[len(suck) - 1]] != 0:
            suck[suck[len(suck) - 1]] = 0
            step = self.path + 'S'
            insertion_order += 1
            suck_successor = Node(suck, self.cost + 1, step, insertion_order)
            to_return.append(suck_successor)

        return to_return

def is_goal(state):

    for k in range(0, len(state) - 1):
        if state[k] == 1:
            return False

    return True

def problem22_6():
    #for line in fileinput.input():
    line = sys.stdin.readline()
    try:
        arrangement = [int(x.strip()) for x in line.split(', ')]

    except:
        return 'invalid input'

    # initial state not valid
    length = len(arrangement)
    for n in range(0, length - 1):
        if arrangement[n] not in [0, 1]:
            return 'invalid input'

    if arrangement[length - 1] >= length - 1:
        return 'invalid input'

    # determine whether the state is a goal state
    if is_goal(arrangement):
        return ''

    start = Node(arrangement, 0, '', insertion_order)
    openlist.put(start)

    while not openlist.empty():
        q = openlist.get()
            
        for child in q.successors():
            if is_goal(child.state):
                return child.path

            for i in openlist.queue:
                if i < child:
                    continue

            for j in closelist:
                if j < child:
                    continue
                
            openlist.put(child)

        closelist.append(q)

    return 'None'

print(problem22_6())
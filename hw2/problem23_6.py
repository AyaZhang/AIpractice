"""
Author:
Xinyi Ma xim002@ucsd.edu
Yijun Zhang yiz160@ucsd.edu
Yuanchi Ha yuha@ucsd.edu
"""

import sys
import fileinput
from queue import PriorityQueue

class Node:

    def __init__(self, state, cost, path, order):
        self.state = state
        self.cost = cost
        self.heuristic = sum(sum(1 for i in row if i == 1) for row in state[:-1])
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

        left = [row[:] for row in self.state]
        if left[-1][1] > 0:
            left[-1][1] -= 1
            step = self.path + 'L'
            insertion_order += 1
            left_successor = Node(left, self.cost + 1, step, insertion_order)
            toRet.append(left_successor)

        up = [row[:] for row in self.state]
        if up[-1][0] > 0:
            up[-1][0] -= 1
            step = self.path + 'U'
            insertion_order += 1
            up_successor = Node(up, self.cost + 1, step, insertion_order)
            toRet.append(up_successor)

        right = [row[:] for row in self.state]
        if right[-1][1] < len(right[0]) - 1:
            right[-1][1] += 1
            step = self.path + 'R'
            insertion_order += 1
            right_successor = Node(right, self.cost + 1, step, insertion_order)
            toRet.append(right_successor)

        down = [row[:] for row in self.state]
        if down[-1][0] < len(right) - 2:
            down[-1][0] += 1
            step = self.path + 'D'
            insertion_order += 1
            down_successor = Node(down, self.cost + 1, step, insertion_order)
            toRet.append(down_successor)

        suck = [row[:] for row in self.state]
        cur_x = self.state[-1][0]
        cur_y = self.state[-1][1]
        if suck[cur_x][cur_y]!= 0:
            suck[cur_x][cur_y] = 0
            step = self.path + 'S'
            insertion_order += 1
            suck_successor = Node(suck, self.cost + 1, step, insertion_order)
            toRet.append(suck_successor)

        return toRet


def isGoal(state):
    for i in state[:-1]:
        for j in i:
            if j != 0:
                return False
    return True


input = sys.stdin.read()
text = input.splitlines()
row = len(text)
if text:
    column = len(text[0].split(','))
else:
    sys.exit('invalid input')
lines = []

for j in range(0,row):
    li = [int(x.strip()) for x in text[j].split(',')]
    lines.append(li)

#vacumm location not valid
if len(lines[row-1]) == 2:
    if (int(lines[row-1][0]) not in range(0,row-1)) or (int(lines[row-1][1]) not in range(0,column)):
        sys.exit('invalid input: last line')
else:
    sys.exit('invalid input: last line')

# Initial state not valid
for i in range(0,row-1):
    for k in range(0, column):
        if lines[i][k] not in [0,1]:
            sys.exit('invalid input')
            

# Whether the state is a goal state
if isGoal(lines):
    print('')
    sys.exit()

# A* search
openlist = PriorityQueue()
closelist = []
insertion_order = 0

start = Node(lines, 0, '', insertion_order)
openlist.put(start)

while not openlist.empty():
    q = openlist.get()

    children = q.successors()
    for child in children:
        if isGoal(child.state):
            print(child.path)
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

"""
Author:
Xinyi Ma xim002@ucsd.edu
Yijun Zhang yiz160@ucsd.edu
Yuanchi Ha yuha@ucsd.edu
"""

import sys
import fileinput

def isGoal(state):
    for i in state[:-1]:
        for j in i:
            if j != 0:
                return False
    return True


def depth_limited_search(node, depth, path):

    if depth == 0 and isGoal(node):
        return (node, path)

    action = 'LURDS'

    if depth > 0:
        for act in action:

            child = [row[:] for row in node]

            if act == 'L':
                if child[-1][1] > 0:
                    child[-1][1] -= 1
            
            elif act == 'R':
                if child[-1][1] < len(node[0]) - 1:
                    child[-1][1] += 1

            elif act == 'U':
                if child[-1][0] > 0:
                    child[-1][0] -= 1

            elif act == 'D':
                if child[-1][0] < len(node) - 2:
                    child[-1][0] += 1

            elif act == 'S':
                cur_x = node[-1][0]
                cur_y = node[-1][1]
                if child[cur_x][cur_y] != 0:
                    child[cur_x][cur_y] = 0
            
            if child == node:
                continue
            
            foundIn = depth_limited_search(child, depth - 1, path + act)
            
            if foundIn[0] is not None:
                return foundIn

    return (None, path)


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
    print ''
    sys.exit()


path = ''

for depth in range(0, 10):

    found = depth_limited_search(lines, depth, path)

    if found[0] is not None:
        #print(found[1])
        sys.exit()

print 'None'
sys.exit()

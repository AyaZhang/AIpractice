"""
Author:
Xinyi Ma xim002@ucsd.edu
Yijun Zhang yiz160@ucsd.edu
"""

import sys
import fileinput
from collections import deque

#Problem23_2

input = sys.stdin.read()
text = input.splitlines()
row = len(text)
column = len(text[0].split(','))
lines=[]
for j in range(0,row):
        li = [int(x.strip()) for x in text[j].split(',')]
        lines.append(li)
        
#vacumm location not valid
if len(lines[row-1]) == 2:
    if (int(lines[row-1][0]) not in range(0,row-1)) or (int(lines[row-1][1]) not in range(0,column)):
        sys.exit('invalid input: last line')
else:
    sys.exit('invalid input: last line')

for i in range(0,row-1):
    # Initial state not valid
    for k in range(0, column):
        if lines[i][k] not in [0,1]:
            sys.exit('invalid input')
            

# Whether the state is a goal state
count = 0
for i in range(0, row-1):
    for j in range(0, column):
        if (lines[i][j] is 0):
            count += 1
        else:
            break
    if count != column:
        break

# Check if they are all zeros
if count == (row-1)*column:
    sys.exit('')


#Problem23_2 BFS
frontier = deque([lines])
print frontier
visited = [frontier]
path = {}
path[str(tuple(lines))] = ''
action = 'LURDS'

while len(frontier) != 0:
    node = frontier.popleft()
    room = node[row-1]
    
    # Find goal state
    count = 0
    for k in range(0, row-1):
        for v in range(0, column-1, 2):
            if int(node[k][v]) == 0:
                count+=1
            else:
                break
        if count != column:
            break

    if count == (row-1)*column:
        print path[str(tuple(node))]
        sys.exit()
        
    #run BFS
    step = path[str(tuple(node))]
    for act in action:
        if act == 'L':
            temp = list(node)
            temp[row-1][1] = (room[1])-1
            print temp
            if temp in visited:
                continue
            elif temp[row-1][1] >= 0:
                frontier.append(temp)
                visited.append(temp)
                path[str(tuple(temp))] = step + act

        if act=='U':
            temp=list(node)
            temp[row-1][0]=room[0]-1
            if temp in visited:
                continue
            elif temp[row-1][0]>=0:
                frontier.append(temp)
                visited.append(temp)
                path[tuple(temp)]=step+act

        elif act == 'R':
            temp = list(node)
            temp[row-1][1] = (room[1])+1
            print temp
            if temp in visited:
                continue
            elif temp[row-1][1] <= column-1:
                frontier.append(temp)
                visited.append(temp)
                path[str(tuple(temp))] = step + act


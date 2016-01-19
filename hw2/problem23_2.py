"""
Author:
Xinyi Ma xim002@ucsd.edu
Yijun Zhang yiz160@ucsd.edu
Yuanchi Ha yuha@ucsd.edu
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

# Check if they are all zeros
if count == (row-1)*column:
    sys.exit('')


#Problem23_2 BFS
frontier = deque([lines])
#print frontier
visited = [lines]
#print visited
path = {}
path[str(tuple(lines))] = ''
action = 'LURDS'

while len(frontier) != 0:
    #print len(frontier)
    node = frontier.popleft()
    #print 'this is node: '
    #print node
    #print temp
    room = list(node[row-1])

    # Find goal state
    count = 0
    for k in range(0, row-1):
        for v in range(0, column):
            if node[k][v] == 0:
                count+=1
            else:
                break

    #print 'count'
    #print count
    if count == (row-1)*column:
        print 'final path'
        print path[str(tuple(node))]
        sys.exit()
        
    #run BFS
    step = path[str(tuple(node))]

    for act in action:
        #print act
        temp=[]
        for item in node:
            temp.append(list(item))
        if act == 'L':
            temp[row-1][1] = room[1]-1
            if temp in visited:
                #print 'visited'
                continue
            elif temp[row-1][1] >= 0:
                frontier.append(temp)
                visited.append(temp)
                path[str(tuple(temp))] = step + act

        elif act=='U':
            temp[row-1][0]=room[0]-1
            #print 'temp'
            #print temp
            if temp in visited:
                #print 'visited'
                continue
            elif temp[row-1][0]>=0:
                frontier.append(temp)
                visited.append(temp)
                path[str(tuple(temp))]=step+act

        elif act == 'R':
            temp[row-1][1] = (room[1])+1
            if temp in visited:
                continue
            elif temp[row-1][1] <= column-1:
                frontier.append(temp)
                visited.append(temp)
                path[str(tuple(temp))] = step + act

        elif act=='D':
            temp[row-1][0]=room[0]+1
            if temp in visited:
                continue
            elif temp[row-1][0]<=row-2:
                frontier.append(temp)
                visited.append(temp)
                path[str(tuple(temp))]=step+act


        elif act == 'S':
            temp[room[0]][room[1]]=0
            if temp in visited:
                continue
            else:
                frontier.append(temp)
                visited.append(temp)
                path[str(tuple(temp))]=step+act
        #print frontier


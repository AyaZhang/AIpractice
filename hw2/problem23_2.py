"""
Author:
Xinyi Ma xim002@ucsd.edu
Yijun Zhang yiz160@ucsd.edu
"""

import sys
import fileinput
from collections import deque

#Problem23_1

lineNum = 0
input = sys.stdin.read()
lines = input.splitlines()
row = len(lines)
column = len(lines[0].split(','))

#vacumm location not valid
if len(lines[row-1]) == 3:
    if (int(lines[row-1][0]) not in range(0,row-1)) or (int(lines[row-1][2]) not in range(0,column)):
        sys.exit('invalid input: last line')
else:
    sys.exit('invalid input: last line')

for i in range(0,row-1):
    line=lines[i]
    try:
        arrangement = [int(x.strip()) for x in line.split(',')]
        length = len(arrangement)

    except:
        sys.exit('invalid input')
        
    # Initial state not valid
    for k in range(0, length-1):
        if arrangement[k] not in [0,1]:
            sys.exit('invalid input')
            

# Whether the state is a goal state
count = 0
for i in range(0, row-1):
    line=lines[i]
    arrangement = [int(x.strip()) for x in line.split(',')]
    length = len(arrangement)
    for j in range(0, length):
            if (arrangement[j] is 0):
                    count += 1
            else:
                    break
    if count != 3:
         break
# Check if they are all zeros        
if count == (row-1)*column:
        sys.exit('')
           
#Problem23_2 BFS
frontier = deque([lines])
print frontier
visited = [frontier]
path = {}
path[tuple(lines)] = ''
action = 'LURDS'

while len(frontier) != 0:
        length = len(lines)
        node = frontier.popleft()
        room = node[length-1]
        print room

        count = 0
        #for k in range(0, length-1):
 #               if node[k] is 0:
        


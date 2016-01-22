"""
Author:
Xinyi Ma xim002@ucsd.edu
Yijun Zhang yiz160@ucsd.edu
Yuanchi Ha yuha@ucsd.edu
"""

import sys
import fileinput
from collections import deque

lineNum = 0
input = sys.stdin.read()
text = input.splitlines()
row = len(text)
column = len(text[0].split(','))
lines = []
for j in range(0,row):
    li = [int(x.strip()) for x in text[j].split(',')]
    lines.append(li)

#vacumm location not valid
if len(lines[row-1]) == 2:
    if (int(lines[row-1][0]) not in range(0,row-1)) or (int(lines[row-1][1]) not in range(0,column)):
        sys.exit('invalid input')
else:
    sys.exit('invalid input')

for i in range(0,row-1):
    # Initial state not valid
    for k in range(0, column):
        if lines[i][k] not in [0,1]:
            sys.exit('invalid input')
        
    # Whether the state is a goal state
    for k in range(0, column):
        if lines[i][k] is 0:
            continue
        else:
            sys.exit 'False'
        
print 'True'

sys.exit()


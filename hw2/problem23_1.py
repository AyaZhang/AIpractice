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
lines = input.splitlines()
print lines
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
        print arrangement
        length = len(arrangement)

    except:
        sys.exit('invalid input')
        
    # Initial state not valid
    for k in range(0, length-1):
        if arrangement[k] not in [0,1]:
            sys.exit('invalid input')
        
    # Whether the state is a goal state
    for k in range(0, length-1):
        if arrangement[k] is 0:
            continue
        else:
            sys.exit('False')
        
print('True')

sys.exit()


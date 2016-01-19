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
print row
print 'this is col'
print column

# Initial state not valid
if (int(lines[row-1][0]) not in range(0,row-1)) or (int(lines[row-1][2]) not in range(0,column)):
    sys.exit('invalid input: last line')
        
for line in lines:
        try:
            arrangement = [int(x.strip()) for x in line.split(',')]
            length = len(arrangement)

        except:
                sys.exit('invalid input')

        for k in range(0, length-1):
                if arrangement[k] not in [0,1]:
                        sys.exit('invalid input')

        # Whether the state is a goal state
        



"""
Author:
Yijun Zhang yiz160@ucsd.edu
Xinyi Ma   xim002@ucsd.edu
Yuanchi Ha yuha@ucsd.edu
"""
import sys
import fileinput

def problem21_1():
    #for line in fileinput.input():
    line = sys.stdin.readline()
    
    try:
        arrangement = [int(x.strip()) for x in line.split(', ')]
    
    except ValueError:
        return 'invalid input here'

    # more than 3 numbers in the same line
    if len(arrangement) > 3:
        return 'invalid input'
        
    # initial state not valid
    for k in range(0, 3):
        if arrangement[k] not in [0, 1]:
            return 'invalid input'

    # determine whether the state is a goal state
    if arrangement[0] is 0 and arrangement[1] is 0:
        return 'True'
    else:
        return 'False'

print(problem21_1())


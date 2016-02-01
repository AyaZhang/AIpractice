"""
Author: 
Yijun Zhang yiz160@ucsd.edu
Xinyi Ma   xim002@ucsd.edu
Yuanchi Ha yuha@ucsd.edu
"""
import sys
import fileinput

def problem22_1():
    for line in fileinput.input():

        try:
            arrangement = [int(x.strip()) for x in line.split(',')]
            length = len(arrangement)

        except ValueError:
            return 'invalid input'

        # initial state not valid
        for k in range(0, length-1):
            if arrangement[k] not in [0, 1]:
                return 'invalid input'
        if arrangement[length-1] >= length-1:
            return 'invalid input'

        # determine whether the state is a goal state
        for k in range(0, length-1):
            if arrangement[k] is 0:
                continue
            else:
                return 'False'
        return 'True'

print(problem22_1())

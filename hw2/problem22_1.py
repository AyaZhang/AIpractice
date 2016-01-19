"""
Author: 
Yijun Zhang yiz160@ucsd.edu
Xinyi Ma   xim002@ucsd.edu
Yuanchi Ha yuha@ucsd.edu
//TODO
"""
import sys
import fileinput

for line in fileinput.input():

    try:
        arrangement = [int(x.strip()) for x in line.split(',')]
        length=len(arrangement)
        print arrangement

    except:
        sys.exit('invalid input')

    # more than 3 numbers in the same line
    #if len(arrangement) > lengh:
    #    sys.exit('invalid input')

    # initial state not valid
    for k in range(0, length-1):
        if arrangement[k] not in [0, 1]:
            sys.exit('invalid input')
    if arrangement[length-1]>=length-1:
        sys.exit('invalid input')

    # determine whether the state is a goal state
    for k in range(0, length-1):
        if arrangement[k] is 0:
            continue
        else:
            sys.exit('False')
    print('True')

sys.exit()

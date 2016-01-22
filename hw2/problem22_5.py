"""
author:
Xinyi Ma xim002@ucsd.edu
Yijun Zhang yiz160@ucsd.edu
Yuanchi Ha yuha@ucsd.edu
"""

import sys
import fileinput

def isGoal(state):
    for i in state[:-1]:
        if i != 0:
            return False
    return True

def depth_limited_search(node, depth, path):
    

    if depth == 0 and isGoal(node):
        return (node, path)

    action = 'LRS'

    if depth > 0:
        for act in action:
            if act=='S':
                child=list(node)
                if child[child[length-1]]==0:
                    continue
                else:
                    child[child[length-1]] = 0
            
            elif act=='R':
                child = list(node)
                if child[length-1] < length-2:
                    child[-1] += 1
                else:
                    continue
            
            elif act=='L':
                child = list(node)
                if child[length-1] > 0:
                    child[-1] -= 1
                else:
                    continue
            
            #if child == list(node):
            #   continue
            

            #print(child,path)
            found = depth_limited_search(child, depth - 1, path+act)
            
            if found[0] is not None:
                return found

    return (None, path)

#Problem22_1
for line in fileinput.input():

    try:
        arrangement = [int(x.strip()) for x in line.split(',')]
        length=len(arrangement)

    except:
        sys.exit('invalid input')


    for k in range(0, length-1):
        if arrangement[k] not in [0, 1]:
            sys.exit('invalid input')
    if arrangement[length-1]>=length-1:
        sys.exit('invalid input')
    
    # determine whether the state is a goal state
    count=0
    for k in range(0, length-1):
        #print arrangement[k]
        if arrangement[k] is 0:
            count+=1
        else:
            break
    if count==length-1:
        sys.exit('')

    path = ''

    for depth in range(0, 8):

        found = depth_limited_search(arrangement, depth, path)

        if found[0] is not None:
            print(found[1])
            sys.exit()

    print('None')
    sys.exit()

"""
author:
Xinyi Ma xim002@ucsd.edu
Yijun Zhang yiz160@ucsd.edu
Yuanchi Ha yuha@ucsd.edu
"""

import sys
import fileinput

def depth_limited_search(node, depth, path):
    arrange = [int(x.strip()) for x in line.split(',')]
    visited = [arrange]
    frontier = [arrange]
    print node[0:]
    if depth == 0 and node[0:-1] == 0:
        return (node, path)

    action = 'SRL'

    if depth > 0:
        for act in action:
            if act=='S':
                temp=list(node)
                temp[temp[-1]]=0
                if temp in visited:
                    continue
                else:
                    frontier.append(temp)
                    visited.append(temp)
                    path += act
        
            elif act=='R':
                temp=list(node)
                if temp[-1] in range(0,len(temp)-1):
                    temp[-1] += 1
                if temp in visited:
                    continue
                elif temp[length-1]<=length-1:
                    frontier.append(temp)
                    visited.append(temp)
                    path += act
    
            elif act=='L':
                temp=list(node)
                if temp[-1] in range(1,len(temp)):
                    temp[-1] -= 1
                if temp in visited:
                    continue
                elif temp[length-1]>=0:
                    frontier.append(temp)
                    visited.append(temp)
                    path += act


            found = depth_limited_search(temp, depth - 1, path)
            
            if found[0] is not None:
                return found

    return (None, path)

#Problem21_1
for line in fileinput.input():

    try:
        arrangement = [int(x.strip()) for x in line.split(',')]
        length=len(arrangement)

    except:
        sys.exit('invalid input')

    # more than 3 numbers in the same line
    #if len(arrangement) > 3:
    #    sys.exit('invalid input')

    # initial state not valid
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

"""
author:
Xinyi Ma xim002@ucsd.edu
"""

import sys
import fileinput
#Problem21_1
def depth_first_search(arrangement,depth):
    """
    for line in fileinput.input():
        print line
        try:
            arrangement = [int(x.strip()) for x in line.split(',')]
            print arrangement
    
        except:
            sys.exit('invalid input')
    
    # more than 3 numbers in the same line
        if len(arrangement) > 3:
            sys.exit('invalid input')
    
    # initial state not valid
        for k in range(0, 3):
            if arrangement[k] not in [0, 1]:
                sys.exit('invalid input')

        # determine whether the state is a goal state
        if arrangement[0] is 0 and arrangement[1] is 0:
            print('True')
            sys.exit()
        else:
            print('False')
            """
#Problem21_3
    frontier=[arrangement]
    visited=[arrangement]
    path={}
    path[tuple(arrangement)]=''
    action='SRL'
    dep=0
    while len(frontier)!=0 and dep < depth:
        #print len(frontier)
        node=frontier.pop()
        dep+=1
        #print 'depth: '
        #print dep
        if dep==depth:
            continue
        #print 'This is node: '
        #print node
        #print 'path: '+path[tuple(node)]
        room=node[2]
        #find goal state
        if node[0]==0 and node[1]==0:
            return 'final path: '+path[tuple(node)]
        else:
            room=node[2]
            step=path[tuple(node)]
            for act in action:
                #print act
                if act=='S':
                    temp=list(node)
                    temp[room]=0
                    if temp in visited:
                        continue
                    else:
                        frontier.append(temp)
                        visited.append(temp)
                        path[tuple(temp)]=step+act
                        #print frontier
                if act=='R':
                    temp=list(node)
                    if room==1:
                        continue
                    else:
                        temp[2]=1
                    if temp in visited:
                        continue
                    else:
                        frontier.append(temp)
                        visited.append(temp)
                        path[tuple(temp)]=step+act
                        #print frontier
                if act=='L':
                    temp=list(node)
                    if room==0:
                        continue
                    else:
                        temp[2]=0
                        if temp in visited:
                            continue
                        else:
                            frontier.append(temp)
                            visited.append(temp)
                            step=path[tuple(node)]
                            path[tuple(temp)]=step+act
                            #print frontier
    dep=0
    while len(frontier)!=0 and dep < depth:
        #print 'length: '
        #print len(frontier)
        node=frontier.pop()
        dep+=1
        if dep==depth:
            continue
        #print 'This is node: '
        #print node
        #print 'path: '+path[tuple(node)]
        room=node[2]
        #find goal state
        if node[0]==0 and node[1]==0:
            return 'final path: '+path[tuple(node)]
        else:
            room=node[2]
            step=path[tuple(node)]
            for act in action:
                #print act
                if act=='S':
                    temp=list(node)
                    temp[room]=0
                    if temp in visited:
                        continue
                    else:
                        frontier.append(temp)
                        visited.append(temp)
                        path[tuple(temp)]=step+act
                        #print 'frontier: '
                        #print frontier
                if act=='R':
                    temp=list(node)
                    if room==1:
                        continue
                    else:
                        temp[2]=1
                    if temp in visited:
                        continue
                    else:
                        frontier.append(temp)
                        visited.append(temp)
                        path[tuple(temp)]=step+act
                        #print 'frontier: '
                        #print frontier
                if act=='L':
                    temp=list(node)
                    if room==0:
                        continue
                    else:
                        temp[2]=0
                    if temp in visited:
                        continue
                    else:
                        frontier.append(temp)
                        visited.append(temp)
                        step=path[tuple(node)]
                        path[tuple(temp)]=step+act
                        #print 'frontier: '
                        #print frontier

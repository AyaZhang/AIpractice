"""
author:
Xinyi Ma xim002@ucsd.edu
Yijun Zhang yiz160@ucsd.edu
Yuanchi Ha yuha@ucsd.edu
"""

import sys
import fileinput

def Problem21_3():
    for line in fileinput.input():

        try:
            arrangement = [int(x.strip()) for x in line.split(',')]

        except ValueError:
            return 'invalid input'

        # more than 3 numbers in the same line
        if len(arrangement) > 3:
            return 'invalid input'

        # initial state not valid
        for k in range(0, 3):
            if arrangement[k] not in [0, 1]:
                return 'invalid input'

        # determine whether the state is a goal state
        if arrangement[0] is 0 and arrangement[1] is 0:
            return ''

        #Problem21_3
        frontier = [arrangement]
        visited = []
        path = {}
        path[id(arrangement)] = ''
        action = 'SRL'

        while len(frontier) != 0:
            node = frontier.pop()
            room = node[2]
            visited.append(node)

            #find goal state
            if node[0] == 0 and node[1] == 0:
                return path[id(node)]
        
            step = path[id(node)]

            for act in action:
                if act == 'S':
                    temp = list(node)
                    temp[room] = 0
                elif act == 'R':
                    temp = list(node)
                    temp[2] = 1
                elif act == 'L':
                    temp = list(node)
                    temp[2] = 0
                if temp in visited:
                    continue
                else:
                    frontier.append(temp)
                    path[id(temp)] = step + act

print(Problem21_3())
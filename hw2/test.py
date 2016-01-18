"""
author:
Xinyi Ma xim002@ucsd.edu
"""

import sys
import fileinput

def depth_limited_search(node, depth, path):

    if depth == 0 and node[0] == 0 and node[1] == 0:
        return (node, path)

    action = 'SRL'

    if depth > 0:
        for act in action:
            if act == 'L':
                child = list(node)
                child[2] = 0
            elif act == 'R':
                child = list(node)
                child[2] = 1
            elif act == 'S':
                child = list(node)
                child[child[2]] = 0

            if child == list(node):
                continue

            #print(path)
            path += act
            found = depth_limited_search(child, depth - 1, path)
            
            if found[0] is not None:
                return found

    return (None, path)
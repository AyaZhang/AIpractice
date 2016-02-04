# -*- coding: utf-8 -*-
__author__ = 'Please write your names, separated by commas.'
__email__ = 'Please write your email addresses, separated by commas.'

from collections import deque


def ac3(csp, arcs=None):#implement backtracking here?
    """Executes the AC3 or the MAC (p.218 of the textbook) algorithms.

    If the parameter 'arcs' is None, then this method executes AC3 - that is, it will check the arc consistency
    for all arcs in the CSP.  Otherwise, this method starts with only the arcs present in the 'arcs' parameter
    in the queue.

    Note that the current domain of each variable can be retrieved by 'variable.domains'.

    This method returns True if the arc consistency check succeeds, and False otherwise."""

    queue_arcs = deque(arcs if arcs is not None else csp.constraints.arcs())
    # TODO implement this
    while queue_arcs is not empty:
        [xi, xj] = queue_arcs.popleft()
        if remove_inconsistent_values(xi,xj):
            for [xi,xk] in csp.constraints[xi].arcs():  #csp.constraints[xi].arcs() find all constraint related to xi, and xk is the neighbor of xi(a problem here: xk sometime is the same as xi and some xk are repetitive)
                queue_arcs.add(tuple(xk,xi))

def remove_inconsistent_values(xi, xj):
    removed = False
    dom = xi.domain
    for x in xi.domain:
        xi.assign(x)
        while y in xj.domain:
            xj.assign[y]
            if not csp.constraints[xi,xj]:
                #xi.domain = [value in dom if value is not x]   #delete x from domain[xi]
                removed = True
    return removed

def revise(csp, xi, xj):
    # You may additionally want to implement the 'revise' method.
    pass

"""
#debug here
[xi, xj] = queue_arcs.popleft()
    print [xi, xj]
    print [xi]
    print csp.constraints[xi].arcs()
    list = deque(csp.constraints[xi].arcs())
    for [xi, xk] in csp.constraints[xi].arcs():
        print xk
#for [xi, xk] in list:
#print xk
#for constraint in csp.constraints[xi]:
#       print constraint
#print type(constraint)
"""
"""
    print queue_arcs
    for item in queue_arcs:
    print item
    print type(item)
    print item[1]
    """
"""
    dom = [1,2,3,4]
    x = 1
    y = []
    for value in dom and value is not x:
    y.append(value)
    print y
    
    
"""
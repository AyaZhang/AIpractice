# -*- coding: utf-8 -*-
__author__ = 'Please write your names, separated by commas.'
__email__ = 'Please write your email addresses, separated by commas.'

from collections import deque
#from p2_is_consistent import *

def ac3(csp, arcs=None):#implement backtracking here?
    """Executes the AC3 or the MAC (p.218 of the textbook) algorithms.

    If the parameter 'arcs' is None, then this method executes AC3 - that is, it will check the arc consistency
    for all arcs in the CSP.  Otherwise, this method starts with only the arcs present in the 'arcs' parameter
    in the queue.

    Note that the current domain of each variable can be retrieved by 'variable.domains'.

    This method returns True if the arc consistency check succeeds, and False otherwise."""

    queue_arcs = deque(arcs if arcs is not None else csp.constraints.arcs())
    # TODO implement this
    while len(queue_arcs) != 0:
        [xi, xj] = queue_arcs.popleft()
        if len(xi.domain) == 0:# or len(xj.domain) == 0:
            return False

        elif remove_inconsistent_values(csp,xi,xj):
            for [xw,xk] in csp.constraints[xi].arcs():
                if xk != xi and xk != xj:
                    queue_arcs.append((xk,xw))
    return True


def remove_inconsistent_values(csp,xi, xj):
    removed = False
    constrains = csp.constraints[xi,xj]
    for constraint in csp.constraints[xi,xj]:
        for x in xi.domain:
            if not all(constraint.is_satisfied(x,y) for y in xj.domain):
                xi.domain.remove(x)
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

"""
    
    queue_arcs = deque(arcs if arcs is not None else csp.constraints.arcs())
    # TODO implement this
    while len(queue_arcs) != 0:
    #print queue_arcs
    [xi, xj] = queue_arcs.popleft()
    print [xi,xj]
    print 'remove: ',remove_inconsistent_values(csp,xi,xj)
    for constraint in csp.constraints[xi,xj]:
    if constraint.is_satisfied(xi,xj):
    continue
    elif remove_inconsistent_values(csp,xi,xj):
    for [xw,xk] in csp.constraints[xi].arcs():
    if xk != xi and xk != xj:
    queue_arcs.append((xk,xw))
    else: return False
    return True
"""

"""
    queue_arcs = deque(arcs if arcs is not None else csp.constraints.arcs())
    # TODO implement this
    while len(queue_arcs) != 0:
    #print queue_arcs
    [xi, xj] = queue_arcs.popleft()
    print [xi,xj]
    #print 'remove: ',remove_inconsistent_values(csp,xi,xj)
    for constraint in csp.constraints[xi,xj]:
    print 'constraint:',constraint
    print constraint.is_satisfied(xi.value,xj.value)
    if constraint.is_satisfied(xi.value,xj.value):
    print 'here'
    break
    elif remove_inconsistent_values(csp,xi,xj):
    for [xw,xk] in csp.constraints[xi].arcs():
    if xk != xi and xk != xj:
    queue_arcs.append((xk,xw))
    else: return False
    return True
    
    
    def remove_inconsistent_values(csp,xi, xj):
    removed = False
    dom = xi.domain
    for x in xi.domain:
    xi.assign(x)
    for y in xj.domain:
    xj.assign(y)
    for constraint in csp.constraints[xi,xj]:
    print constraint
    print 'satisfied', not constraint.is_satisfied(x,y)
    if not constraint.is_satisfied(x,y):
    xi.domain = []
    #delete x from domain[xi]
    for val in dom:
    if val != x:
    xi.domain.append(val)
    
    removed = True
    return removed
"""
"""
    queue_arcs = deque(arcs if arcs is not None else csp.constraints.arcs())
    #for element in queue_arcs:
    #print element
    # TODO implement this
    while len(queue_arcs) != 0:
    #print queue_arcs
    [xi, xj] = queue_arcs.popleft()
    #print [xi,xj]
    if len(xi.domain) == 0:# or len(xj.domain) == 0:
    return False
    
    elif remove_inconsistent_values(csp,xi,xj):
    for [xw,xk] in csp.constraints[xi].arcs():
    if xk != xi and xk != xj:
    queue_arcs.append((xk,xw))
    #elif constraint.is_satisfied(xi.value,xj.value):
    #    print 'here'
    #    break
    
    #else:return False
    return True
    
    
    def remove_inconsistent_values(csp,xi, xj):
    removed = False
    #dom = xi.domain
    constrains = csp.constraints[xi,xj]
    for constraint in csp.constraints[xi,xj]:
    for x in xi.domain:
    if not all(constraint.is_satisfied(x,y) for y in xj.domain):
    xi.domain.remove(x)
    removed = True
    #print 'removed', removed
    return removed
"""

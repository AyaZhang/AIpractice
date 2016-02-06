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
        if len(xi.domain) == 0:
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
            if not any(constraint.is_satisfied(x,y) for y in xj.domain):
                xi.domain.remove(x)
                removed = True
    return removed

#def revise(csp, xi, xj):
    # You may additionally want to implement the 'revise' method.
#pass



# -*- coding: utf-8 -*-
__author__ = 'Xinyi Ma, Yuanchi Ha, Yijun Zhang'
__email__ = 'xim002@ucsd.edu, yuha@ucsd.edu, yiz160@ucsd.edu'

from collections import deque
from p1_is_complete import *
from p2_is_consistent import *
from p5_ordering import *
from assignment3 import *

def inference(csp, variable):
    """Performs an inference procedure for the variable assignment.
        
        For P6, *you do not need to modify this method.*
        """
    return ac3(csp, csp.constraints[variable].arcs())


def backtracking_search(csp):
    """Entry method for the CSP solver.  This method calls the backtrack method to solve the given CSP.
        
        If there is a solution, this method returns the successful assignment (a dictionary of variable to value);
        otherwise, it returns None.
        
        For P6, *you do not need to modify this method.*
        """
    if backtrack(csp):
        return csp.assignment
    else:
        return None


def backtrack(csp):
    """Performs the backtracking search for the given csp.
        
        If there is a solution, this method returns True; otherwise, it returns False.
        """
    
    # TODO copy from p3
    if is_complete(csp):
        return True
    
    var = select_unassigned_variable(csp)
    for value in order_domain_values(csp, var):
        if is_consistent(csp,var,value):
            csp.variables.begin_transaction()
            var.assign(value)
            inference(csp, var)
            result = backtrack(csp)
            if result:
                return result
            csp.variables.rollback()

    return False


def ac3(csp, arcs=None):
    """Executes the AC3 or the MAC (p.218 of the textbook) algorithms.
        
        If the parameter 'arcs' is None, then this method executes AC3 - that is, it will check the arc consistency
        for all arcs in the CSP.  Otherwise, this method starts with only the arcs present in the 'arcs' parameter
        in the queue.
        
        Note that the current domain of each variable can be retrieved by 'variable.domains'.
        
        This method returns True if the arc consistency check succeeds, and False otherwise.  Note that this method does not
        return any additional variable assignments (for simplicity)."""
    
    queue_arcs = deque(arcs if arcs is not None else csp.constraints.arcs())
    
    # TODO copy from p4
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

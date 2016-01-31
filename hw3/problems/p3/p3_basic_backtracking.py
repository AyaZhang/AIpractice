# -*- coding: utf-8 -*-
__author__ = 'Please write your names, separated by commas.'
__email__ = 'Please write your email addresses, separated by commas.'

from p1_is_complete import *
from p2_is_consistent import *
from assignment3 import *

def select_unassigned_variable(csp):
    """Selects the next unassigned variable, or None if there is no more unassigned variables
    (i.e. the assignment is complete).

    For P3, *you do not need to modify this method.*
    """
    return next((variable for variable in csp.variables if not variable.is_assigned()))


def order_domain_values(csp, variable):
    """Returns a list of (ordered) domain values for the given variable.

    For P3, *you do not need to modify this method.*
    """
    return [value for value in variable.domain]


def inference(csp, variable):
    """Performs an inference procedure for the variable assignment.

    For P3, *you do not need to modify this method.*
    """
    return True


def backtracking_search(csp):
    """Entry method for the CSP solver.  This method calls the backtrack method to solve the given CSP.

    If there is a solution, this method returns the successful assignment (a dictionary of variable to value);
    otherwise, it returns None.

    For P3, *you do not need to modify this method.*
    """
    if backtrack(csp):
        return csp.assignment
    else:
        return None


def backtrack(csp):
    """Performs the backtracking search for the given csp.

    If there is a solution, this method returns True; otherwise, it returns False.
    """

    # TODO implement this
    return recursive_backtracking(csp)
        
def recursive_backtracking(csp):
    if is_complete(csp):
        return True

    var = select_unassigned_variable(csp)
    dom = var.domain
    for value in order_domain_values(csp, var):
        
        if is_consistent(csp,var,value):
            csp.variables.begin_transaction()
            var.assign(value)
            result = recursive_backtracking(csp)
            if result:
                return result
            var.domain = []
            for i in dom:
                var.domain.append(i)
            csp.variables.rollback()

    return False


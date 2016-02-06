# -*- coding: utf-8 -*-
__author__ = 'Xinyi Ma, Yuanchi Ha, Yijun Zhang'
__email__ = 'yiz160@ucsd.edu'

from p1_is_complete import *
from p2_is_consistent import *
from p3_basic_backtracking import *
from assignment3 import *

def select_unassigned_variable(csp):
    """Selects the next unassigned variable, or None if there is no more unassigned variables
    (i.e. the assignment is complete).

    This method implements the minimum-remaining-values (MRV) and degree heuristic. That is,
    the variable with the smallest number of values left in its available domain.  If MRV ties,
    then it picks the variable that is involved in the largest number of constraints on other
    unassigned variables.
    """

    # If there is no more unassigned variables, return None
    if all(i.is_assigned() is True for i in csp.variables):
        return None

    # Return the variable that has minimum-remaining-value
    unassigned = []

    for i in csp.variables:
        if not i.is_assigned():
            unassigned.append(i)

    if len(unassigned) == 1:
        return unassigned[0]

    unassigned.sort(key = lambda x: len(x.domain))

    if (len(unassigned[0].domain) != len(unassigned[1].domain)):
        return unassigned[0]

    # Return the variable that has max occurance in constraints
    occurance = [len(csp.constraints[i]) for i in unassigned]
    nth = occurance.index(max(occurance))

    return unassigned[nth]


def order_domain_values(csp, variable):
    """Returns a list of (ordered) domain values for the given variable.

    This method implements the least-constraining-value (LCV) heuristic; that is, the value
    that rules out the fewest choices for the neighboring variables in the constraint graph
    are placed before others.
    """

    count = []
    copy = variable.domain

    for i in range(len(copy)):
        variable.assign(copy[i])
        count.append((test(csp, variable), copy[i]))

    variable.domain = copy

    count.sort(key = lambda tup: tup[0])

    return [i[1] for i in count]


def test(csp, variable):
    """ Helper method for order_domain_values()

    This method returns the number of violations that would occur if a
    variable is assigned to certain value.
    """

    violations = 0

    for i in csp.constraints[variable]:
        violations += sum(1 for j in i.var2.domain if i.is_satisfied(variable.domain[0], j) == False)

    return violations
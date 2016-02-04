# -*- coding: utf-8 -*-
__author__ = 'Xinyi Ma, Yuanchi Ha, Yijun Zhang'
__email__ = ', yiz160@ucsd.edu'


def is_consistent(csp, variable, value):
    """Returns True when the variable assignment to value is consistent, i.e. it does not violate any of the constraints
    associated with the given variable for the variables that have values assigned.

    For example, if the current variable is X and its neighbors are Y and Z (there are constraints (X,Y) and (X,Z)
    in csp.constraints), and the current assignment as Y=y, we want to check if the value x we want to assign to X
    violates the constraint c(x,y).  This method does not check c(x,Z), because Z is not yet assigned."""


    # TODO implement this
    #print csp.constraints
    #print csp.assignment, '\n'
    #print 'variable\t', variable
    #print 'value\t', value, '\n'
    for constraint in csp.constraints[variable]:
        #print '\t',constraint
        #print '\t', constraint.var1
        #print '\t', constraint.var2
        #print '\t', constraint.relation
        if constraint.var2.is_assigned():
            if not constraint.is_satisfied(value,constraint.var2.value):
                return False
    return True


# -*- coding: utf-8 -*-
__author__ = 'Xinyi Ma, Yuanchi Ha, Yijun Zhang'
__email__ = 'xim002@ucsd.edu, yuha@ucsd.edu, yiz160@ucsd.edu'


def is_complete(csp):
    """Returns True when the CSP assignment is complete, i.e. all of the variables in the CSP have values assigned."""

    # Hint: The list of all variables for the CSP can be obtained by csp.variables.
    # Also, if the variable is assigned, variable.is assigned() will be True.
    # (Note that this can happen either by explicit assignment using variable.assign(value),
    # or when the domain of the variable has been reduced to a single value.)

    # TODO implement this
    #print csp.variables,'\n'
    for var in csp.variables:
        #print var
        if not var.is_assigned():
            return False

    return True


#!/usr/bin/python3

"""
module that contains function
that verifies instance
"""


def is_same_class(obj, a_class):
    """
    verifies is obj is an instance of
    a specified class

    Args:
        obj: object being pass
        a_class: class to compare

    returns:
    """
    if type(obj) == a_class:
        return True
    else:
        return  False

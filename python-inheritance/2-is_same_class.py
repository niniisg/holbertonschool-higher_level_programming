#!/usr/bin/python3

"""
module that contains function
that verifies instance
"""


def is_same_class(obj, a_class):
    """
    verifies if obj is an instance of
    a specified class

    Args:
        obj: object being pass
        a_class: class to compare

    return:
        True if object is an instance
        of specified class
        False if not
    """
    if type(obj) is a_class:
        return True
    else:
        return False

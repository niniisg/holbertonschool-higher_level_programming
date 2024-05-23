#!/usr/bin/python3
"""
this module contains if object is an
instance of a class
"""


def is_kind_of_class(obj, a_class):
    """
    verifies if obj is an instnce
    of a class that inherited

    Args:
        obj: object being pass
        a_class: class to compare
    return:
        True if object is an instance
        of specified class
        False if not
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False

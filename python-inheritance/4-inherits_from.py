#!/usr/bin/python3
"""
this module contains a functions that
verifies instance of a class that inherited
directly or indirectly
"""


def inherits_from(obj, a_class):
    """
    verifies if obj is an instance

    Args:
        obj: the object to be verifie
        a_class the class to be check

    return:
        true if the object is an instance
        false if is not
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False

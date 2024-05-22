#!/usr/bin/python3
"""
this module hold a function that retursn a list
"""


def lookup(obj):
    """
        returns a list of aviable attributes and methods
            of an object.

        agrs:
            object: the object being passed
    """
    return list(dir(obj))

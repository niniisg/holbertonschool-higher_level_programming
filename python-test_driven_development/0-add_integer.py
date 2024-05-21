#!/usr/bin/python3
"""

This file has function add integer
    
"""


def add_integer(a, b=98):
    """
    verifies if a or b are int or float adds two numbers and returns the result.
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a + b)

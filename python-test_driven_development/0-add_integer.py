#!/usr/bin/python3

def add_integer(a, b=98):
    """
    verifies if a or b are int or float
    adds two numbers and returns the result.
    returns:
    int or float: the sum of the two input number
    raises:
    TypeError: if either a or b is not an integer or a float
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a + b)

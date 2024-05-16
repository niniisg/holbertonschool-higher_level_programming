#!/usr/bin/python3
"""
this class contains a square
that defines a square.
"""


class Square:
    """
    a class to represent a square

    Attributes:
        __size: the size of square
    Method:
        None
    """
    def __init__(self, size=0):
        """
        this is a constrocture that takes an option
        argumet name size, and it validates if is an int.
         """
        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

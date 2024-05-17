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

    @property
    def size(self):
        """
        retrives the private property of size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        updates the property of size after
        validation the new value.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        return an area of square
        """
        area = self.__size * self.__size
        return area

    def my_print(self):
        """
        prints size with no new line
        """
        for i in range (self.__size):
            print("#" * self.__size, end="")
            print()

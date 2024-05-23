#!/usr/bin/python3
"""
this class contains an empty BaseGeometry
"""


class BaseGeometry:
    """
    a class representing a BaseGeometry

    Atrributes:
        None:

    Methods:
        None
    """
    def area(self):
        """
        return an area of BaseGeometry
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates if value is an int
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than".format(name))

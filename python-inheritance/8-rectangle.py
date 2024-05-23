#!/usr/bin/python3
"""
this class contains an Rectangle that
inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    a class represint Retangle:
    """
    def __init__(self, width, height):
        """
        defines the value of width and height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

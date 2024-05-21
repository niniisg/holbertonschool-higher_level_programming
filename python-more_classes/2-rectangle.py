#!/usr/bin/python3
"""
defining a Rectangle with properties
for height and width
"""


class Rectangle:
    """
    a class that represent a Rectangle

    """

    def __init__(self, width=0, height=0):
        """
        defines the value of widht and height

        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        getting the widht of the rectangle

        Returns:
            int: the widht of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width of the rectangle

        Args:
            value (int): the width value to set

        Raises:
            TypeError: if the value us not an integer
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        getting the heigth of the rectangle

        Returns:
            int: the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setting the height of the rectangle

        Args:
            value (int) the height value set

        Raises:
            TypeError: if value is not an integer
            ValueError: if value in less than 0
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        return an area of rectangle
        """
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """
        return the perimeter of the rectangle
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        perimeter = (self.__width * 2) + (self.__height * 2)
        return perimeter

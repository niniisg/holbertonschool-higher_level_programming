#!/usr/bin/python3
"""
defines a file appending function
"""


def append_write(filename="", text=""):
    """
    appends a string to the end of specified file
    text file

    Args:
        filename (str) the name of the file to append to
        text(str) the txt to append to the file
    Returns:
        the number of characters to append
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

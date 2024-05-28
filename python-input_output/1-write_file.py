#!/usr/bin/python3
"""
this module defines a writing file function
"""


def write_file(filename="", text=""):
    """
    writes a string to txt files

    Args:
        filename (str): the name of the file to be writing
        text (str) a text to be writing in a file
    Returns:
        the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

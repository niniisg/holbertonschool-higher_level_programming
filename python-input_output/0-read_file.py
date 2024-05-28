#!/usr/bin/python3
""" this module defines a text file-reading function"""


def read_file(filename=""):
    """
    prints and read text files

    Args:
        filename(str) file name to be read
    Reads:
        None
    """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

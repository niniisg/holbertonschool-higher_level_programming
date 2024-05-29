#!/usr/bin/python3
"""
this module contains a python class-to-JSON fucntion
"""
def class_to_json(obj):
    """
    returns a dictionary represention
    """
    return obj.__dict__

#!/usr/bin/python3
"""
defines a string funtion to JSON
"""


import json


def to_json_string(my_obj):
    """
    returns a JSON representation of a string
    """
    return json.dumps(my_obj)

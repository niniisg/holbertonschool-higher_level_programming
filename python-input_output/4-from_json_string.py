#!/usr/bin/python3
"""
module import a JSON object function
"""
import json


def from_json_string(my_str):
    """
    convers a JSON string into a pyhton data structutre
    Args:
        my_str (str) JSON string to convert
    Returns:
        convert from python object
    """
    return json.loads(my_str)

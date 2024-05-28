#!/usr/bin/python3

import json
"""
defines a JSON object funtion
"""


def from_json_string(my_str):
    """
    convers a JSON string into a pyhton data structutre
    """
    return json.loads(my_str)

#!/usr/bin/python3

"""
this module saves an object to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    saves a JSON file in Python object

    Args:
        my_obj: python object to be saved
        filename (str): a path to JSON file where the
        objec will be save

    Returns:
        None
    """
    with open(filename, "w") as f:
      return json.dump(my_obj, f)

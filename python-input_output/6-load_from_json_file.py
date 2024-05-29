#!/usr/bin/python3
"""
this module loads data from JSON
"""
import json


def load_from_json_file(filename):
    """
    load data from a JSON file

    Args:
        filename (Str) the path to JSON file
    Returns:
        dict: dictionary loaded from the JSON file
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)

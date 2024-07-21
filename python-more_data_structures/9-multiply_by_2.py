#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        b_dictionary = a_dictionary.copy()
    for key, value in a_dictionary.items():
        b_dictionary[key] = value * 2
    return b_dictionary
#!/usr/bin/python3

def uppercase(string):
    upper_letter = ""
    for char in string:
        if 'a' <= char <= 'z':
           upper_letter += chr(ord(char) - 32)
        else:
            upper_letter += char
    return upper_letter

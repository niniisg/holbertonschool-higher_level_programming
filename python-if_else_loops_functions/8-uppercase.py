#!/usr/bin/python3

def uppercase(str):
    i = ""
    for letter in str:
        if ord('a') <= ord(letter) <= ord('z'):
            i += chr(ord(letter) - 32)
        else:
            i += letter
    print(i)

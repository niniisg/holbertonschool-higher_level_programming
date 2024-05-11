#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    for hidden in dir(sys):
        if not hidden.startswith("__'):
             print(hidden)

#!/usr/bin/python3

from add_0 import add
if __name__ == "__main__":

    def main(a, b):
        return a + b
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))

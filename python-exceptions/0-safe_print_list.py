#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        for item in range(x):
            print("{:d}".format(my_list[item]), end="")
            counter +=1
        print()
        return counter
    except IndexError:
        print()
        return item

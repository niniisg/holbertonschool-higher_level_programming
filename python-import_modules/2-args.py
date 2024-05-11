#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argument = len(sys.argv) - 1
    number = 0

    if argument == 0:
        print("{} arguments.".format(argument))
    elif argument == 1:
        print("{} argument:".format(argument))
    else:
        print("{} arguments:".format(argument))

    if argument > 0:
        for index in sys.argv:
            if number != 0:
                print("{}: {}".format(number, index))
            number += 1

#!/usr/bin/python3

for two_digit in range(99):

    if two_digit == 98:
        print(two_digit)
    else:
        print("{:02d}".format(two_digit), end=', ')

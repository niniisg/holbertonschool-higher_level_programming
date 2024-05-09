#!/usr/bin/python3

for two_digit in range(100):

    if two_digit == 99:
        print(two_digit)
    else:
        print("{:02d}".format(two_digit), end=', ')

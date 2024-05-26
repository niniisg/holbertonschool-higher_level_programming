#!/usr/bin/python3


for i in range(0, 10):
    for number in range(i + 1, 10):
        if i == 8 and number == 9:
            print("{}{}".format(i, number))
        else:
            print("{}{}".format(i, number), end=", ")

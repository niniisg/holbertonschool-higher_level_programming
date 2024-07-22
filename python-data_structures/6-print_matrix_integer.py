#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for column in range(len(row)):
            if column == 0:
                print("{:d}".format(row[column]), end="")
            else:
                print(" {:d}".format(row[column]), end="")
        print("")

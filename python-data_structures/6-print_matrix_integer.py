#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for item in row:
            print("{:d}".format(item), end=" ")
        if item != len(row) - 1:
            print(" ", end="")
        print()

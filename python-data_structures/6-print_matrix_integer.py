#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for item in row:
            if item !=0:
                print(" ", end="")
            print("{:d}".format(item), end=" ")
        print()

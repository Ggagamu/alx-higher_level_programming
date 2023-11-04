#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for digit in row:
            print('{:3d}'.format(digit), end=" ")
        print()

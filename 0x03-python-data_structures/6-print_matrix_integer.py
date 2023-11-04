#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    else:
        for row in matrix:
            for digit in row:
                print("{:d}".format(digit), end=" " if digit != row[-1] else '\n')
        print()

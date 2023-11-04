#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix != [[]]:
        for row in matrix:
            for dgt in row:
                print("{:d}".format(dgt), end=" "
                      if dgt != row[-1] else '\n')
    else:
        print()

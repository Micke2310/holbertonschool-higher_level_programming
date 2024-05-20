#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for sub_matrix in matrix:
        for element in sub_matrix:
            print("{:d}".format(element), end=" ")
        print()

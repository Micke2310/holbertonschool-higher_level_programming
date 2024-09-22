#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for lista in matrix:
        for elemento in lista:
            print("{:d}".format(elemento), end=" ")

        print()

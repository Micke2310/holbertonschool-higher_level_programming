#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for lista in matrix:
        for elemento in lista:
            print("{}".format(elemento), end="")

        print()

#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for lista in matrix:
        for i in range(len(lista)):
            elemento= lista[i]
            if i == len(lista) -1:
                print("{:d}".format(elemento), end="")
            else:
                print("{:d}".format(elemento), end=" ")

        print()

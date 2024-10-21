#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):

    resultado = map(lambda y: y * number, my_list)

    return list(resultado)

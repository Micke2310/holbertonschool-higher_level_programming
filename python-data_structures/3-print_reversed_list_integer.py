#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):

    if my_list != None:

        for num in range(len(my_list) - 1, -1, -1):
            #el primer -1 del rango marca el inicio de la iteracion
            #(el ultimo elemento), el segundo marca el final (llega hasta el indice 0),
            #y el tercero marca el paso a paso (de 1 en 1 hacia atras).
            print("{:d}".format(my_list[num]))

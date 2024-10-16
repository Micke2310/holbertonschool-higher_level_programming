#!/usr/bin/python3

def uniq_add(my_list=[]):

    sin_repetir = []
    suma = 0

    for i in my_list:
        if i not in sin_repetir:
            suma = suma + i
            sin_repetir.append(i)

    return suma

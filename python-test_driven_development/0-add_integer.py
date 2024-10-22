#!/usr/bin/python3
def add_integer(a, b=98):

    '''

    funcion : add_integer suma de dos argumentos y son enteros
    a = debe ser un valor entero
    b = debe de ser un valor entero

    en caso que los valores sean flotantes convertirlos en enteros y en caso de no ser
    entero o flotante, manejarlo como errores.

    retornar: suma de a y b

    '''

    suma = int(a) + int(b)

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a and b must be integers or floats")

        a = int(a)

        b = int(b)

    return suma

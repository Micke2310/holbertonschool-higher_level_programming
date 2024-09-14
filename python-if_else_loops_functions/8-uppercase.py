#!/usr/bin/python3
def uppercase(string):
    resultado = ""

    for char in string:
        if char >= 'a' and char <= 'z':
            resultado = resultado + chr(ord(char) -32)

        else:
            resultado = resultado + char

    return resultado

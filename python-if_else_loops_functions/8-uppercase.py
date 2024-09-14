#!/usr/bin/python3
def uppercase(string):
    resultado = ""

    for char in string:
        if char in range("a","z"):
            resultado = resultado + chr(ord(char) -32)

        else:
            resultado = resultado + char

    return resultado

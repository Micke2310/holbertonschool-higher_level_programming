#!/usr/bin/python3
def uppercase(string):
    resultado = ""

    for i in string:
        if i in range("96","123"):
            i = ord(i)
            resultado = resultado + chr(ord(i) -32)

        else:
            resultado = resultado + i

    return resultado

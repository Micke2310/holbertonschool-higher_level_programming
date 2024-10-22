#!/usr/bin/python3

def roman_to_int(s):

    diccionario_romano = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    resultado = 0
    valor_ant = 0

    for i in reversed(s)
        valor_actual = diccionario_romano[i]
        if valor_actual > valor_ant:
            resultado -= valor_actual

        else:
            resultado += valor_actual
            valor_ant = valor_actual

    return resultado

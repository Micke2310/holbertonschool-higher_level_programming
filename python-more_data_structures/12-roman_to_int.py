#!/usr/bin/python3

def roman_to_int(s):

    diccionario_romano = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    resultado = None
    valor_ant = None

    for i in range(len(s) -1, -1, -1):
        valor_actual = diccionario_romano[s[i]]
        if valor_actual >= valor_ant:
            resultado += valor_actual

        else:
            resultado -= valor_actual
            valor_ant = valor_actual

    return resultado

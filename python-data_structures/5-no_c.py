#!/usr/bin/python3
def no_c(my_string):
    i = 0 #para recorrer la cadena
    new_string = "" #la nueva cadena donde guardare los caracteres

    while i < len(my_string): #mientras I sea menor que la longitud de la cadena
        if my_string[i] != 'c' and my_string[i] != 'C': # si indice en my_string [i] es diferente de estos caracteres , condicional
            new_string = new_string + my_string[i] #se le agrega a la cadena vacia new_string, el valor de indice [i] al final de la misma
        i= i + 1
    return new_string

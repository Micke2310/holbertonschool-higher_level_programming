#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [] 
    
    for fila in matrix:
        new_fila = []
        
        for elemento in fila:
            cuadrado = elemento * elemento
            new_fila.append(cuadrado)

        new_matrix.append(new_fila)
    return new_matrix

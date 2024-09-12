#!/usr/bin/python3


#def islower(caracter):la 'c' es muetra de un caracter en minuscula "c" o "C"
                    #es el parametro la variable que se define en la funcion,
                    #cuando le asigno un valor a la funcion es el argumento.
def islower(caracter):
    if caracter >= 'a' and caracter <= 'z':
        return True
    else:
        return False


islower = __import__('7-islower').islower

print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))

#!/usr/bin/python3
if __name__ == "__main__":

    from calculator_1 import add, mul, sub, div

    a = 10
    b = 5

    suma = add(a, b)
    print("{} + {} = {}".format(a, b, suma))

    resta = sub(a, b)
    print("{} - {} = {}".format(a, b, resta))

    multiplicacion = mul(a, b)
    print("{} * {} = {}".format(a, b, multiplicacion))

    division = div(a, b)
    print("{} / {} = {}".format(a, b, division))

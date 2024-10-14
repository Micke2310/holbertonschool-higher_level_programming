#!/usr/bin/python3
from calculator_1 import add, mul, sub, div

a = 10
b = 5

suma = add(a, b)
print(f"{a} + {b} = {suma}")

resta = sub(a, b)
print(f"{a} - {b} = {resta}")

multiplicacion = mul(a, b)
print(f"{a} * {b} = {multiplicacion}")

division = div(a, b)
print(f"{a} / {b} = {division}")

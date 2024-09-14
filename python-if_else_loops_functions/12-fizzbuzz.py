#!/usr/bin/python3
def fizzbuzz():
    numeros = 0
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz ", end="")
            numeros = num

        elif num % 3 == 0:
            print("Fizz ", end="")
            numeros = num

        elif num % 5 == 0:
            print("Buzz ", end="")
            numeros = num

        else:
            print(num + " ", end="")
            numeros = num

    return numeros

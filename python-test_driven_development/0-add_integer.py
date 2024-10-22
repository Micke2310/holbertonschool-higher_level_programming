#!/usr/bin/python3
def add_integer(a, b=98):
    """Suma dos números enteros.

    Args:
        a: El primer número. Será convertido a entero si es un flotante.
        b: El segundo número. Si no se proporciona, se utiliza el valor por defecto 98.

    Returns:
        La suma de a y b como un entero.

    Raises:
        TypeError: Si a o b no pueden ser convertidos a enteros.
    """

    suma = int(a) + int(b)

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a and b must be integers or floats")

        a = int(a)

        b = int(b)

    return suma

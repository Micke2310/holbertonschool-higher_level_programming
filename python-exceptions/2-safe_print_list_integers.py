#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    contador = 0

    for i in range(x):
        try:
            dato = my_list[i]

            if isinstance(dato, int):
                print("{:d}".format(dato), end="")
                contador = contador + 1

        except IndexError as e:
            print(e)
            break

    print ("")

    return (contador)

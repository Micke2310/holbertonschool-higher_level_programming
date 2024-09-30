#!usr/bin/python3
def list_division(my_list_1, my_list_2, list_lenght):
    resultado = []

    for i in range(list_lenght):
        
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            resultado.append(a/b)

        except IndexError:
            print("out of range")
            resultado.append(0)
        except ZeroDivisionError:
            print("division by 0")
            resultado.append(0)
        except TypeError:
            print("wrong type")
            resultado.append(0)

    return resultado

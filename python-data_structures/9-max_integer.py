#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max_valor = my_list[0]
        for idx in my_list:
            if idx > max_valor:
                max_valor = idx
        return max_valor
    else:
        return None

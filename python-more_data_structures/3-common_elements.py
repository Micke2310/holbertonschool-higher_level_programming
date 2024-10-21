#!/usr/bin/python3

def common_elements(set_1, set_2):
    '''return set_1 & set_2'''
    set_inter = set()
    for i in set_1:
        for j in set_2:
            if i == j:
                set_inter.add(i)
    return set_inter

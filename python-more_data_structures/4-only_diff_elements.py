#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    '''return set_1 ^ set_2'''
    set_3_diff = set()

    for i en set_1:
        for j in set_2:
            if i != j:
                set_3_diff.append(i)
    return set_3_diff

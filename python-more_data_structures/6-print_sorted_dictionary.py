#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):

    new_dic = sorted(a_dictionary.keys())
    for i in new_dic:
        print(f"{i}: {a_dictionary[i]}")

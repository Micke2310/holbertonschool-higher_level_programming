#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    for idx in range(len(my_list)):
        if idx < 0 or idx >= len(my_list):
            return my_list.copy()
        else:
            new_list = my_list.copy()
            new_list[idx] = element
            print(new_list)

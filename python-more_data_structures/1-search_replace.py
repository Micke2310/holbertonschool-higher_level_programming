#!/usr/bin/python3
def search_replace(my_list, search, replace):
    ''' my_list = lista inicial
        search =  elemnto a remplazar de la lista
        replace = es el nuevo elemnto
    '''

    new_my_list = []

    for i in my_list:
        if i == search:
            new_my_list.append(replace)
        else:
            new_my_list.append(i)
    return new_my_list

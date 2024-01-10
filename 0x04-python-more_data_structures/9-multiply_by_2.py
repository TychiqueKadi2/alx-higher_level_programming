#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict_x2 = a_dictionary.copy()
    list_keys = list(dict_x2.keys())

    for i in list_keys:
        dict_x2[i] *= 2

    return (dict_x2)

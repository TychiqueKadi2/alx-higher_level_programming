#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    Key = list(a_dictionary.keys())

    for dict_value in Key:
        if value == a_dictionary.get(dict_value):
            del a_dictionary[dict_value]

    return (a_dictionary)


#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = set(my_list)
    x = 0

    for i in add:
        x += i

    return (x)

#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    Sorted = list(a_dictionary.keys())
    Sorted.sort()
    for i in Sorted:
        print("{}: {}".format(i, a_dictionary.get(i)))

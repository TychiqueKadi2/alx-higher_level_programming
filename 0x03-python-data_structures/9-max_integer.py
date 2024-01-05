#!/usr/bin/python
def max_integer(my_list=[]):
    if my_list == []:
        return (None)
    else:
        my_list = [int(x) for x in my_list]
        max_value = my_list[0]
        for i in my_list:
            if i > max_value:
                max_value = i
        return max_value

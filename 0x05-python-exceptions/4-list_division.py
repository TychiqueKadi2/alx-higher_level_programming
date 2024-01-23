#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.
    Returns:
        A new list of length list_length containing all the divisions.
    """
    my_list_new = []
    for i in range(0, list_length):
        try:
            div_rslt = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div_rslt = 0
        except ZeroDivisionError:
            print("division by 0")
            div_rslt = 0
        except IndexError:
            print("out of range")
            div_rslt = 0
        finally:
            my_list_new.append(div_rslt)
    return (my_list_new)

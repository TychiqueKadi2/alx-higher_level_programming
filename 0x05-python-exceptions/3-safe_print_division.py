#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
        div_rslt = a / b
    except (TypeError, ZeroDivisionError):
        div_rslt = None
    finally:
        print("Inside result: {}".format(div))
    return (div_rslt)

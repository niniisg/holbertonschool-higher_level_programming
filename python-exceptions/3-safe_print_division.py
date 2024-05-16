#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        safe_divide = a / b

    except ZeroDivisionError:
        safe_divide = None

    finally:
        print("Inside result: {}".format(safe_divide))
        return safe_divide

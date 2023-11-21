#!/usr/bin/python3
def safe_print_division(a, b):
    """Divides 2 integers and prints the result.

    Args:
        a (int): The dividend.
        b (int): The divisor.

    Returns:
        float: The result of the division, or None if division by zero occurred.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
        return result

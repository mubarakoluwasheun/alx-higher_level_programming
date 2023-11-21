#!/usr/bin/python3
def safe_print_integer(value):
    """Print an integer with "{:d}".format().

    Args:
        value: The value to be printed. It can be any type.

    Returns:
        bool: True if value has been correctly printed
              (it means the value is an integer), otherwise False.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False

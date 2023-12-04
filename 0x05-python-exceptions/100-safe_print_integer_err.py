#!/usr/bin/python3
def safe_print_integer_err(value):
    """
    Prints an integer.

    Args:
        value: The value to be printed. It can be any type.

    Returns:
        bool: True if value has been correctly printed
              (it means the value is an integer), otherwise False.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except Exception as e:
        import sys
        print("Exception: {}".format(e), file=sys.stderr)
        return (False)

#!/usr/bin/python3
def safe_function(fct, *args):
    """
    Executes a function safely.

    Args:
        fct (function): A pointer to the function to be executed.
        *args: The arguments to be passed to the function.

    Returns:
        The result of the function, or None if an error
        occurred during the execution of the function.
    """
    try:
        return fct(*args)
    except Exception as e:
        import sys
        print("Exception: {}".format(e), file=sys.stderr)
        return None

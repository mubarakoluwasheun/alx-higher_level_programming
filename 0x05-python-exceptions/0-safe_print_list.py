#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elements of a list.

    This function attempts to print the first x elements of my_list. If x is larger than the length of my_list,
    it will print all elements in my_list without raising an error. The function returns the actual number of
    elements printed. It does not use the len() function.

    Args:
        my_list (list): The list to print elements from. It can contain any type of elements.
        x (int): The number of elements of my_list to print.

    Returns:
        int: The number of elements printed.
    """
    ret = 0
    for i in range(x):
        try:
            # Try to print the element at index i
            print("{}".format(my_list[i]), end="")
            # If successful, increment the counter
            ret += 1
        except IndexError:
            # If an IndexError is encountered, break the loop
            break
    # Print a new line after printing the elements
    print("")
    return ret

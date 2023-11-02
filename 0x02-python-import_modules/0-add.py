#!/usr/bin/python3


if __name__ == "__main__":
    """Main function that uses the add function from add_0 module."""
    from add_0 import add

    a = 1
    b = 2
    result = add(a, b)
    print(f"{a} + {b} = {result}\n")

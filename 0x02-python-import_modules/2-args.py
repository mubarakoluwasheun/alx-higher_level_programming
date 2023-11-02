#!/usr/bin/python3

import sys

# Get the number of arguments
num_args = len(sys.argv) - 1

# Print the number of arguments
if num_args == 1:
    print("{} argument".format(num_args), end="")
else:
    print("{} arguments".format(num_args), end="")

# Check if there are any arguments
if num_args == 0:
    print(".")
else:
    print(":")
    # Print each argument and its position
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")

#!/usr/bin/python3

def islower(c):
    if not c:
        raise ValueError("Input cannot be an empty string")
    return 'a' <= c <= 'z'

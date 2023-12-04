#!/usr/bin/python3

""" This is a module that defines a Square class."""


class Square:
    """This is a class that defines a square."""

    def __init__(self, size=0):
        """
        This is the constructor method for the class.

        Args:
            size(int): size with a default value of 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size  # set the size attribute

    def area(self):
        """This method returns the current square area."""
        return self.__size * self.__size

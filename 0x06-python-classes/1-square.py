#!/usr/bin/python3

""" This is a module that defines a Square class."""


class Square:
    """This is a class that defines a square."""

    def __init__(self, size):
        """
        This is the constructor method for the class.

        Args:
            size(int): size of new square(no type/value verification).
        """
        self.__size = size

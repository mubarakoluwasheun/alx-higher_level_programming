#!/usr/bin/python3

""" This is a module that defines a Square class."""


class Square:
    """
    This is a class for a square.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        The constructor for the Square class.

        Parameters:
           size (int): The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """
        The size property returns the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        The size property setter sets the size of the square.

        Parameters:
            value (int): The size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        The area method returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        The my_print method prints the square using the '#' character.
        If the size of the square is 0, it prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

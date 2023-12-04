#!/usr/bin/python3

""" This is a module that defines a Square class."""


class Square:
    """
    This is a class for a square.

    Attributes:
        size (int): The size of the square.
        position (tuple): The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        The constructor for the Square class.

        Parameters:
           size (int): The size of the square (default is 0).
           position (tuple): The position of the square (default is (0, 0)).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        The position property returns the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        The position property setter sets the position of the square.

        Parameters:
            value (tuple): The position of the square.

        Raises:
            TypeError: If the value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            print("\n" * self.__position[1], end="")
            print("\n".join(" " * self.__position[0] + "#" * self.__size for _ in range(self.__size)))

#!/usr/bin/python3
# square.py
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the class Square.

        Args:
            size (int): The size of the Square.
            x (int): The x-axis of the Square.
            y (int): The y-axis of the Square.
            id (int): The identity of the Square.
            """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Size Getter."""
        return self.width

    @size.setter
    def size(self, value):
        """Size Setter."""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns [Square] (<id>) <x>/<y> - <size>"""
        return "[{}] {}/{} -{}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """Assigns attributes.

        Args:
            *args (ints): New attribute values.
                - 1st arg = id attribute
                - 2nd arg = size attribute
                - 3rd arg = x attribute
                - 4th arg = y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary repreentation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

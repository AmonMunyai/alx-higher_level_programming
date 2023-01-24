#!/usr/bin/python3
"""Define a class square."""


class Square:
    """Represent a new square.

    Args:
        size (int): The size of the new square.
    """
    def __init__(self, size=0):
        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area."""
        return (self.__size * self.__size)

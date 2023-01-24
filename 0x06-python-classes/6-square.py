#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The new size of the square.
            position (tuple): The position of the square.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if ((isinstance(value, tuple) and
                len(value) == 2) and
                all([isinstance(num, int) for num in value]) and
                all([num >= 0 for num in value])):
            self.__position = value
        else:
            raise TypeError("size muist be a tuple of positive integers")

    def area(self):
        """Return the current square area."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints square in stdout using the '#' character."""
        if (self.__size == 0):
            print("")
            return

        if self.__size != 0:
            [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for s in range(self.__position[0])]
            [print("#", end="") for h in range(self.__size)]
            print("")

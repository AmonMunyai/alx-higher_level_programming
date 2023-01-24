#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
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
        return (self.__size * self.__size)

    def my_print(self):
        if (self.__size == 0):
            print("")
            return

        for i in range(self.__size):
            [print(" ", end="") for s in range(self.__position[0])]
            [print("#", end="") for h in range(self.__size)]
            print("")

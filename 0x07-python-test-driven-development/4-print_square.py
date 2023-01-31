#!/usr/bin/python3
"""Defines a function that prints a square with the `#` character."""


def print_square(size):
    """Prints a square with the character `#`.

    Args:
        size (int): size length of the square.
    Raises:
        TypeError: size must be an integer.
        ValueError: size must be >= 0.
    """
    if (not isinstance(size, int)):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")

    for _ in range(size):
        [print("#", end="") for _ in range(size)]
        print("")

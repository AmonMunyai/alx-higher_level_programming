#!/usr/bin/python3
"""Defines a function that adds 2 integers"""


def add_integer(a, b=98):
    """Returns an integer, the addition of `a` and `b`

    Args:
        a (int/float): first argument.
        b (int/float): second argument - optional, 98 by default.
    Raises:
        TypeError: `a` and `b` must be integers or floats.
    Returns:
        an integer, the additon of `a` and `b`.
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

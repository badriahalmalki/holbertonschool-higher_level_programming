#!/usr/bin/python3
"""
Module that provides a simple integer addition function.

This module exposes add_integer which adds two numbers after
validating their types and casting floats to integers.
"""

def add_integer(a, b=98):
    """
    Add two integers and return the result.

    a and b must be integers or floats; floats are cast to int.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

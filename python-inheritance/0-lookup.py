#!/usr/bin/python3
"""
This module provides a function that returns the list of attributes
and methods available for a given object.
"""


def lookup(obj):
    """
    Return a list of attributes and methods of an object.

    Args:
        obj: Any Python object.

    Returns:
        A list containing the names of the object's attributes and methods.
    """
    return dir(obj)

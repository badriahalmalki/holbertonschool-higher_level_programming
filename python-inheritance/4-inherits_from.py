#!/usr/bin/python3
"""
This module provides a function that checks whether an object is an
instance of a subclass of a specified class.
"""


def inherits_from(obj, a_class):
    """
    Determine if an object is an instance of a subclass of a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare inheritance against.

    Returns:
        True if obj is an instance of a class that inherited from a_class,
        otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

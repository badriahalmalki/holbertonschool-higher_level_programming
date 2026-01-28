#!/usr/bin/python3
"""
This module provides a function that checks whether an object is an
instance of a specified class or a class that inherited from it.
"""


def is_kind_of_class(obj, a_class):
    """
    Determine if an object is an instance of a class or a subclass.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class or a subclass of a_class,
        otherwise False.
    """
    return isinstance(obj, a_class)

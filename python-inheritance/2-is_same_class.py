#!/usr/bin/python3
"""
This module provides a function that checks whether an object is
exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Determine if an object is exactly an instance of a given class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class

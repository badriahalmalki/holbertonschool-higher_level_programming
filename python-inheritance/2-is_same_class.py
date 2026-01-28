#!/usr/bin/python3
"""Module that defines a function to check if an object is exactly an instance of a specified class."""
def is_same_class(obj, a_class):
    """
    Checks if `obj` is exactly an instance of the specified class

    Args:
        obj (any): The object to compare
        a_class (any): The class to compare with the object

    Returns:
        `True` if the object is exactly an instance of the
        specified class; otherwise `False`
    """

    if type(obj) == a_class:
        return True

    return False

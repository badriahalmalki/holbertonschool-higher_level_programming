#!/usr/bin/python3
"""Module that defines a function to check if an object is an instance of a specified class or its subclasses."""
def is_kind_of_class(obj, a_class):
    return isinstance(obj, a_class)

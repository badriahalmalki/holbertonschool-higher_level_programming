#!/usr/bin/python3
"""
This module defines the Square class with a private size attribute.
"""


class Square:
    """
    Represents a square with a private size attribute.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size: The size of the square (no type or value validation).
        """
        self.__size = size

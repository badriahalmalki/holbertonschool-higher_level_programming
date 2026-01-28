#!/usr/bin/python3
"""
This module defines the Square class, which inherits from Rectangle
and provides its own string representation.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that validates size and uses Rectangle initialization.
    """

    def __init__(self, size):
        """
        Initialize a Square with a validated private size.

        Args:
            size: The size of the square (must be a positive integer).
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Return the square description in the format:
        [Square] <size>/<size>
        """
        return f"[Square] {self.__size}/{self.__size}"

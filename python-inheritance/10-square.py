#!/usr/bin/python3
"""
This module defines the Square class, which inherits from Rectangle.
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

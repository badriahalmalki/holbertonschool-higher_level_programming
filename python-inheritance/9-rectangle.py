#!/usr/bin/python3
"""
This module defines the Rectangle class, which inherits from BaseGeometry
and implements area calculation and string representation.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that validates width and height using BaseGeometry
    and provides area computation and formatted string output.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle with validated private width and height.

        Args:
            width: Rectangle width (must be a positive integer).
            height: Rectangle height (must be a positive integer).
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        Compute and return the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return the rectangle description in the format:
        [Rectangle] <width>/<height>
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

#!/usr/bin/python3
"""
This module defines the BaseGeometry class with validation utilities.
"""


class BaseGeometry:
    """
    Base class for geometry-related operations.
    """

    def area(self):
        """
        Raise an exception because area is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that value is a positive integer.

        Args:
            name: The name of the parameter.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

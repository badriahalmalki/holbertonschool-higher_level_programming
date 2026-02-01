#!/usr/bin/python3
"""
This module defines a Student class with basic attributes
and a method to retrieve a filtered dictionary representation.
"""


class Student:
    """
    Represents a student with a first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance.

        If attrs is a list of strings, only attributes listed in attrs
        are included. Otherwise, all attributes are returned.

        Args:
            attrs (list): Optional list of attribute names to retrieve.

        Returns:
            dict: A dictionary of selected or all attributes.
        """
        if isinstance(attrs, list):
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        return self.__dict__

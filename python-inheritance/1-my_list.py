#!/usr/bin/python3
"""
This module defines the MyList class, which extends the built-in list
with a method to print the list in sorted order.
"""


class MyList(list):
    """
    A custom list class that inherits from Python's built-in list
    and provides a method to print the list sorted in ascending order.
    """

    def print_sorted(self):
        """
        Print the list elements in ascending sorted order.

        The original list remains unchanged.
        """
        print(sorted(self))

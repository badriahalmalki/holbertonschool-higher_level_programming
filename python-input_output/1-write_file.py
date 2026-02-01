#!/usr/bin/python3
"""
This module provides a function that writes text to a UTF-8 file.
The function creates the file if it does not exist and overwrites it if it does.
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF-8) and return the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text content to write into the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

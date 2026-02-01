#!/usr/bin/python3
"""
This module provides a function that appends text to a UTF-8 file.
If the file does not exist, it will be created automatically.
"""


def append_write(filename="", text=""):
    """
    Append a string to the end of a text file (UTF-8) and return
    the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

#!/usr/bin/python3
"""
This module provides a function that writes a Python object
to a text file using its JSON string representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using JSON representation.

    Args:
        my_obj: The Python object to serialize.
        filename (str): The name of the file to write to.

    Returns:
        None
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))

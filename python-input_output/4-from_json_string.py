#!/usr/bin/python3
"""
This module provides a function that converts a JSON string
into the corresponding Python data structure.
"""

import json


def from_json_string(my_str):
    """
    Convert a JSON string into a Python object.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)

#!/usr/bin/python3
"""
This module provides a function that loads a Python object
from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Create a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        object: The Python data structure represented by the JSON content.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f.read())

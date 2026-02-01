#!/usr/bin/env python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.
    If the file already exists, it will be overwritten.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def load_and_deserialize(filename):
    """
    Load JSON data from a file and deserialize it
    back into a Python dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

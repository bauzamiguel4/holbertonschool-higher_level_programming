#!/usr/bin/python3
"""
This module contains basic serialization functions to save a Python dictionary
to a JSON file and to load and deserialize a JSON file back into a dictionary.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.
    Replaces the file if it already exists.

    Args:
        data (dict): The Python dictionary to serialize.
        filename (str): The filename of the output JSON file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Loads and deserializes JSON data from a file into a Python dictionary.

    Args:
        filename (str): The filename of the input JSON file.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

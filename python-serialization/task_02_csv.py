#!/usr/bin/python3
"""
This module provides a function to convert a CSV file into a JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Reads data from a CSV file and converts it into a JSON format,
    saving the result to data.json.

    Args:
        csv_filename (str): The filename of the CSV to read.

    Returns:
        bool: True if the conversion was successful, False if the file
        was not found or another error occurred.
    """
    try:
        data = []
        with open(csv_filename, 'r', encoding='utf-8') as csvf:
            csv_reader = csv.DictReader(csvf)
            for row in csv_reader:
                data.append(row)

        with open('data.json', 'w', encoding='utf-8') as jsonf:
            json.dump(data, jsonf)

        return True
    except Exception:
        return False

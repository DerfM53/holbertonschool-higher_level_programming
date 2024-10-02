#!/usr/bin/python3
"""
This module provides functionality to convert CSV files to JSON format.

It contains a function that reads data from a CSV file
and writes it to a JSON file.
The module uses the csv and json libraries to handle the conversion process.
"""


import csv
import json


def convert_csv_to_json(csv_file):
    """
    Convert a CSV file to JSON format.

    This function reads data from a specified CSV file,
    converts it to a list of dictionaries,
    and then writes this data to a JSON file named 'data.json'.

    Args:
        csv_filename (str): The name of the CSV file to be converted.

    Returns:
        bool: True if the conversion was successful, False otherwise.

    Raises:
        Exception: Catches and handles any exceptions
        that occur during the process.
    """
    try:
        with open(csv_file, 'r') as file:
            csv_reader = csv.DictReader(file)
            data = list(csv_reader)
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        return True
    except Exception as e:
        return False

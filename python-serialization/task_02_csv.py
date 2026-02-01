#!/usr/bin/env python3
import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Convert CSV data into JSON format and save it to data.json.
    Returns True if successful, False if an error occurs.
    """
    try:
        data_list = []

        # Read CSV file using DictReader
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data_list.append(row)

        # Write JSON output to data.json
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except Exception:
        return False

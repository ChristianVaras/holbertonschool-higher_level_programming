#!/usr/bin/python3
"""
Contains function that adds and saves to Python obj to JSON file; loads objects
"""
import json
from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
# Create the object or calling from json
try:
    obj = load_from_json_file(filename)
except FileNotFoundError:
    obj = []

finally:
    for i in range(1, len(argv)):
    obj.append(argv[i])
    # Create json file
    save_to_json_file(obj, filename)

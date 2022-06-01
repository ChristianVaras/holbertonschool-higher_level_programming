#!/usr/bin/python3
"""
This module defines a script which takes argvs
and appends them to a python list, then writes
the data in a new text file 'add_item.json' in
JSON format.
"""
import json
from sys import argv


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation"""
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(json.dumps(my_obj))


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”"""
    with open(filename, 'r', encoding="utf-8") as file:
        return json.loads(file.read())


object = []
try:
    object = load_from_json_file("add_item.json")
except FileNotFoundError:
    pass
finally:
    for i in range(1, len(argv)):
        object.append(argv[i])
    save_to_json_file(object, "add_item.json")

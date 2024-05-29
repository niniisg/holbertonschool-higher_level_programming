#!/usr/bin/python3

import json
import csv


def convert_csv_to_json(cvs_filename):
    try:
        with open(cvs_filename, "r") as csvf:
            reader = csv.DictReader(csvf)
            data_list = [row for row in csvf]

        with open(data.json, "w") as jsonfile:
            jsonf.dump(data, jsonfile, indent=4)

        return True
    except FileNotFoundError:
        return False

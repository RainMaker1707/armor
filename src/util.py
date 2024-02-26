import json
import re
from datetime import datetime


def from_json_to_dict(raw_file):
    data = dict()
    with open(raw_file, 'r') as file:
        data = json.load(file)
    return data


def from_xml_to_dict(raw_file):
    pass


def iso_format_checker(date):
    if date is None: return True
    # pattern matching  YYYY-MM-DD
    pattern = "[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]"
    if len(re.findall(pattern, date)) == 0:
        return False
    splitted = date.split("-")
    year = int(splitted[0])
    month = int(splitted[1])
    day = int(splitted[2])
    if year < 1950 or year > int(str(datetime.today()).split("-")[0]):
        return False
    if month  <= 0 or month > 12:
        return False
    if day <= 0 or day > 31:
        return False
    if month not in [1, 2, 3, 5, 7, 8, 10, 12]:
        if day > 30: 
            return False
    elif month == 2:
        if year%4 == 0:
            return day <= 29
        else:
            return day <= 28
    return True

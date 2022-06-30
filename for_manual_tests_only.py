import logging
import json
import os
import creating_fake_data
import unittest
import main
import glob
import random
import re




"""
def test.add_lines_to_file():
    file_name = "magic_file_generator.json"
    d_schema = "{\"date\": \"timestamp:\"} "
    path = "/Users/kpodlaska/Desktop"
    f_line_given=10

    file_given = main.create_output_file(f_line_given, d_schema, path, file_name)
    print(file_given)
    f = open(file_given)
    data = json.load(f)
    f.close()
    self.assertEqual(f_given_lines, len(data))
    #poprawione, teraz probujemy to przeczytac
"""

if __name__ == '__main__':


    b = main.existing_dir("../Capstone")
    print(b)
"""    
def create_list_of_fake_data(data_types):
    result = []
    possibilities = list(data_types)
    for possibility in possibilities:
        if "int" in possibility:
            if "rand" in possibility and len(possibility) > 3:
                chars = re.findall(r"[\w']+", possibility)
                digits_for_randint = []
                for char in chars:
                   if char.isdigit():
                       digits_for_randint.append(char)
                min_v = int(min(digits_for_randint))
                max_v = int(max(digits_for_randint))
                value = random.randint(min_v, max_v)
                result.append(value)
            elif len(possibility) == 3:
                value = random.randint(0, 100)
                result.append(value)
        elif "timestamp" in possibility:
            value = create_fake_timestamp()
            result.append(value)
        elif "[" in possibility:
            x = possibility.replace("[", "").replace("]", "").replace(",", "").replace("'", '').split()
            value = random.choice(x)
            result.append(value)
        elif "str" in possibility and "rand" in possibility:
            fake = Faker()
            value = fake.pystr()
            result.append(value)
    return result"""
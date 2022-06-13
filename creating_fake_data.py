import logging
import argparse
import configparser
import uuid
import os
import random
import json
from faker import Faker
import re

def create_fake_timestamp():
    fake = Faker()
    some_data = fake.date_time_between(start_date='-15y', end_date='now')
    some_data = some_data.replace(microsecond=random.randint(0, 999_999))
    some_data = some_data.timestamp()
    value = some_data
    return value

  
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
    return result


def create_fake_dict(data_schema):
    schema_dict = json.loads(data_schema)
    schema_keys = schema_dict.keys()
    schema_data_types = schema_dict.values()
    f_values = create_list_of_fake_data(schema_data_types)
    f_dict = dict(zip(schema_keys, f_values))
    return f_dict


f_name = "test.json"
d_schema = "{\"date\": \"timestamp:\",\"name\": \"str:rand\",\"type\": \"['client', 'partner', 'government']\"," \
           "\"animal_type\": \"['cat', 'dog', 'monkey','tiger']\",\"age\": \"int:rand(1, 90)\",\"kids_number\": " \
           "\"int:rand(1, 6)\"} "



#fake_dict = create_fake_dict(d_schema)


"""next step is to put everything into main and create function which generate huge amount on data based on schema,
It will consume a lot of CPU so please give me some feedback about code above.
I wonder if data created for name is ok. In sample is different format. Millisecond with timestamp still unresolved."""

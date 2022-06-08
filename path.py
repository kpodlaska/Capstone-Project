import logging
import argparse
import configparser
import uuid
import os
import random
import json
from faker import Faker
import re
f_name = "test.json"
d_schema = "{\"date\": \"timestamp:\",\"name\": \"str:rand\",\"type\": \"['client', 'partner', 'government']\",\"age\": \"int:rand(1, 90)\"}"

schema_dict=json.loads(d_schema)
schema_keys=schema_dict.keys()
schema_data_types=schema_dict.values()

def creating_fake_timestamp():
    fake = Faker()
    some_data = fake.date_time_between(start_date='-15y', end_date='now')
    value = some_data.timestamp()
    return value
    #TODO: add miliseconds

separators=[]
def create_list_of_fake_data(data_types):
    result=[]
    possibilities=list(data_types)
    print(possibilities)
    print((possibilities),type(possibilities))
    for possibility in possibilities:
        if "int" in possibility:
            if "rand" in possibility and len(possibility)>3:
                chars = re.findall(r"[\w']+", possibility)
                digits_for_randint=[]
                for char in chars:
                    if char.isdigit()==True:
                        digits_for_randint.append(char)

                min_v=int(min(digits_for_randint))
                max_v=int(max(digits_for_randint))
                value=random.randint(min_v,max_v)
                result.append(value)
            elif len(possibility)==3:
                    value = random.randint(0, 100)
                    result.append(value)
        elif "timestamp" in possibility:
            value=creating_fake_timestamp()
            result.append(value)
        elif "[" in possibility:
            x=possibility.replace("[","").replace("]","").replace(",","").replace("'",'').split()
            value=random.choice(x)
            result.append(value)
        elif "str" in possibility and "rand" in possibility:
            fake=Faker()
            value=fake.pystr()
            result.append(value)
    print("to jest wynik fukncji creating_fake_list:",result)
    return result

def creating_fake_dict(keys,values):
    f_dict = dict(zip(keys, values))
    print(f_dict)

values=create_list_of_fake_data(schema_data_types)

creating_fake_dict(schema_keys,values)
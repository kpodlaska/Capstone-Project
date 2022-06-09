import logging
import argparse
import configparser
import uuid
import os
import random
import json
from faker import Faker
import re
from string import ascii_lowercase
f_name = "test.json"
d_schema = "{\"date\": \"timestamp:\",\"name\": \"str:rand\",\"type\": \"['client', 'partner', 'government']\",\"animal_type\": \"['cat', 'dog', 'monkey','tiger']\",\"age\": \"int:rand(1, 90)\",\"kids_number\": \"int:rand(1, 6)\"}"

schema_dict=json.loads(d_schema)
schema_keys=schema_dict.keys()
schema_data_types=schema_dict.values()

def creating_fake_timestamp():
    fake = Faker()
    some_data = fake.date_time_between(start_date='-15y', end_date='now')
    some_data=some_data.replace(microsecond=random.randint(0,999_999))
    some_data=some_data.timestamp()
    value = some_data
    return value

def creating_name_from_numbers_and_lowercase():
    numbers='0123456789'
    symbol='-'
    all =  ascii_lowercase + numbers
    lenght_1 = 8
    lenght_2 = 4
    lenght_3 = 12
    mid_lenght_part ="".join(random.sample(all, lenght_1))
    short_lenght_part = "".join(random.sample(all, lenght_2))
    long_lenght_part = "".join(random.sample(all, lenght_3))
    name =mid_lenght_part+symbol+(short_lenght_part+symbol)*3+long_lenght_part
    return name

def create_list_of_fake_data(data_types):
    result=[]
    possibilities=list(data_types)
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
            value=creating_name_from_numbers_and_lowercase()
            result.append(value)
    return result

def creating_fake_dict(keys,values):
    f_dict = dict(zip(keys, values))
    print(f_dict)

values=create_list_of_fake_data(schema_data_types)

creating_fake_dict(schema_keys,values)

"""next step is to put everything into main and create function which generate huge amount on data based on schema,
It will consume a lot of CPU so please give me some feedback about code above.
I wonder if data created for name is ok. In sample is different format. Millisecond with timestamp still unresolved."""
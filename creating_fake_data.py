import logging
import random
import json
from faker import Faker
import re
from string import ascii_lowercase

def create_value_list_from_schema(schema):
    schema_dict = json.loads(d_schema)
    schema_data_types = list(schema_dict.values())
    return schema_data_types

def create_key_list_from_schema(schema):
    schema_dict = json.loads(d_schema)
    schema_key_data_types = list(schema_dict.keys())
    return schema_key_data_types

def create_fake_timestamp():
    fake = Faker()
    some_data = fake.date_time_between(start_date='-15y', end_date='now')
    some_data = some_data.replace(microsecond=random.randint(0, 999_999))
    some_data = some_data.timestamp()
    value = some_data
    return value

def creating_name_from_numbers_and_lowercase():
    numbers='0123456789'
    symbol='-'
    all = ascii_lowercase + numbers
    lenght_1 = 8
    lenght_2 = 4
    lenght_3 = 12
    mid_lenght_part ="".join(random.sample(all, lenght_1))
    short_lenght_part = "".join(random.sample(all, lenght_2))
    long_lenght_part = "".join(random.sample(all, lenght_3))
    name =mid_lenght_part+symbol+(short_lenght_part+symbol)*3+long_lenght_part
    return name

def create_list_of_fake_data(schema):
    result = []
    possibilities = create_value_list_from_schema(schema)
    for possibility in possibilities:
        """integers as possible result"""
        if "int" in possibility:
            if "int:" in possibility and "rand" not in possibility:
                naked_possibility = possibility.replace("int:","")
                if naked_possibility.isdigit():
                    result.append(naked_possibility)
                else:
                    logging.error("You choose int type value for non int deflaut parameter. Can't do do this! Value 6 as integer was used instead")
                    result.append(6)
            elif "rand" in possibility and len(possibility) > 3:
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
        elif "str" in possibility:
            if 'rand' not in possibility:
                naked_possibility = possibility.replace("str:", "")
                if naked_possibility.isalpha():
                    result.append(naked_possibility)
                else:
                    logging.error(
                        "You choose str type value for non str deflaut parameter. Can't do do this! Value MagicIsCool  was used instead")
                    result.append("MagicIsCool")
            elif "rand" in possibility:
                value = creating_name_from_numbers_and_lowercase()
                result.append(value)
                """
            elif 'rand' not in possibility and "str:" in possibility:
                naked_possibility = possibility.replace("str:", "")
                if naked_possibility.isalpha():
                    result.append(naked_possibility)
                else:
                    logging.error(
                        "You choose str type value for non str deflaut parameter. Can't do do this! Value MagicIsCool  was used instead")
                    result.append("MagicIsCool")"""

    return result


def create_fake_dict(data_schema):
    f_keys = create_key_list_from_schema(data_schema)
    f_values = create_list_of_fake_data(data_schema)
    f_dict = dict(zip(f_keys, f_values))
    return f_dict


f_name = "test.json"
d_schema = "{\"date\": \"timestamp:\",\"name\": \"str:pies\",\"type\": \"['client', 'partner', 'government']\"," \
           "\"animal_type\": \"['cat', 'dog', 'monkey','tiger']\",\"age\": \"int:rand(1, 90)\",\"kids_number\": " \
           "\"int\"} "


"""next step is to put everything into main and create function which generate huge amount on data based on schema,
It will consume a lot of CPU so please give me some feedback about code above.
I wonder if data created for name is ok. In sample is different format. Millisecond with timestamp still unresolved."""

if __name__ == '__main__':
    d_schema = "{\"date\": \"timestamp:\",\"name\": \"str:kocimietka\",\"type\": \"['client', 'partner', 'government']\"," \
               "\"animal_type\": \"['cat', 'dog', 'donkey', 'monkey', 'tiger']\",\"age\": \"int:78\",\"kids_number\": " \
               "\"int:rand(1, 6)\"} "
    print(create_fake_dict(d_schema))
from faker import Faker
import json
import logging
import os
import random
import re
from string import ascii_lowercase
import uuid


def create_value_list_from_schema(d_schema):
    schema_dict = json.loads(d_schema)
    schema_data_types = list(schema_dict.values())
    return schema_data_types


def create_key_list_from_schema(d_schema):
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
    numbers = '0123456789'
    symbol = '-'
    all_ = ascii_lowercase + numbers
    lenght_1 = 8
    lenght_2 = 4
    lenght_3 = 12
    mid_lenght_part = "".join(random.sample(all_, lenght_1))
    short_lenght_part = "".join(random.sample(all_, lenght_2))
    long_lenght_part = "".join(random.sample(all_, lenght_3))
    name = mid_lenght_part+symbol+(short_lenght_part+symbol)*3+long_lenght_part
    return name


def create_list_of_fake_data(schema):
    result = []
    possibilities = create_value_list_from_schema(schema)
    for possibility in possibilities:
        """integers as possible result"""
        if "int" in possibility:
            if "int:" in possibility and "rand" not in possibility:
                naked_possibility = possibility.replace("int:", "")
                if naked_possibility.isdigit():
                    result.append(naked_possibility)
                else:
                    logging.error("You choose int type value for non int default parameter. Value 6 was used instead")
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
                        "You choose str type value for non str default parameter! Value MagicIsCool  was used instead")
                    result.append("MagicIsCool")
            elif "rand" in possibility:
                value = creating_name_from_numbers_and_lowercase()
                result.append(value)

    return result


def create_fake_dict(data_schema):
    f_keys = create_key_list_from_schema(data_schema)
    f_values = create_list_of_fake_data(data_schema)
    f_dict = dict(zip(f_keys, f_values))
    return f_dict


def existing_dir(prospective_dir):
    if prospective_dir == ".":
        prospective_dir = os. getcwd()
        logging.debug(f"You are in current directory. Path : {prospective_dir}")
        return prospective_dir
    elif os.path.isfile(prospective_dir):
        logging.debug(f"Your directory is  file not a dir. Parent DIR used as a path")
        prospective_dir = os.path.dirname(os.path.abspath(prospective_dir))
        return prospective_dir
    elif os.path.isdir(prospective_dir):
        return prospective_dir
    else:

        try:
            os.makedirs(prospective_dir, exist_ok=True)
            created_dir = os.path.abspath(prospective_dir)
            logging.info(f"Your directory {prospective_dir} has been created successfully. "
                         f"Absolute path to dir is {created_dir}")

        except OSError:
            print("Directory '%s' can not be created")
            logging.critical(f"Wrong path. Can't continue")


def construct_files(file_name, prefix, how_many_files):
    ext = "json"
    prefixes = []
    if prefix == "count":
        for n in range(how_many_files):
            prefixes.append(str(n+1))
    elif prefix == "random":
        for n in range(how_many_files):
            number = random.randint(1, 1_000_000_000_000)
            prefixes.append(number)
    elif prefix == "uuid":
        for n in range(how_many_files):
            x_n = uuid.uuid4()
            prefixes.append(x_n)
    full_filenames = []
    for prefix_ in prefixes:
        full_filename = file_name+"_" + str(prefix_) + "."+ext
        full_filenames.append(full_filename)
    return full_filenames


def create_data_without_output_file(lines, d_schema):
    if lines > 0:
        for i in range(lines):
            data = create_fake_dict(d_schema)
            print(f"{data}")
    else:
        logging.critical("You can't process with {} number of lines".format(lines))


def create_output_file(f_line, d_schema, path, f_name):
    path_to_file = existing_dir(path)
    new_file_with_dir = os.path.join(path_to_file, f_name)
    lines = int(f_line)
    with open(new_file_with_dir, "w") as f:
        for i in range(lines):
            data = create_fake_dict(d_schema)
            json.dump(data, f)
            f.write('\n')
        logging.debug(f"File {f_name} created")
        return new_file_with_dir


def clear_files_in_path(path, file_name):
    existing_dir(path)
    "check if path exists"
    files = os.listdir(path)
    result = []
    for file in files:
        if file.endswith("json"):
            if file_name in file:
                result.append(file)
                new_dir = os.path.join(path, file)
                logging.info(f"Delete file {file}")
                os.remove(new_dir)

if __name__ == '__main__':
    data_schema2 = "{\"date\": \"timestamp:\",\"name\": \"str:rand\",\"type\": \"['client', 'partner', 'government']\",\"animal_type\": \"['cat', 'dog', 'monkey','tiger']\",\"age\": \"int:rand(1, 90)\",\"kids_number\": \"int:rand(1, 6)\"} "
    x=create_fake_dict(data_schema2).values()
    print(x)
    print(type(create_fake_dict(data_schema2).values()))
"""Hope for the best but plan for the worst"""

import argparse
import os
import uuid

from concurrent.futures import ThreadPoolExecutor

import logging
import random
import json
from faker import Faker
import re
from string import ascii_lowercase


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
                    logging.error("You choose int type value for non int deflaut parameter. Value 6 was used instead")
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
                        "You choose str type value for non str deflaut parameter! Value MagicIsCool  was used instead")
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
                        "You choose str type value for non str deflaut parameter! Value MagicIsCool  was used instead")
                    result.append("MagicIsCool")"""

    return result


def create_fake_dict(data_schema):
    f_keys = create_key_list_from_schema(data_schema)
    f_values = create_list_of_fake_data(data_schema)
    f_dict = dict(zip(f_keys, f_values))
    return f_dict


def init_arg_parser():
    parser = argparse.ArgumentParser(prog='magicgenerator')

    parser.add_argument('--path_to_save_files',
                        help="Define a path to output file. For current path use '.', As deflaut is ./Capstone",
                        type=str,
                        default="/Users/kpodlaska/PycharmProjects/pythonProject/Capstone")
    parser.add_argument('--files_count', help="Define how many json file do you want to generate", type=int)
    parser.add_argument('--file_name', help="Choose name to your file", type=str)
    parser.add_argument('--file_prefix', help="If you chose more than 1 output file please choose prefix", type=str,
                        choices=['count', 'random', 'uuid'])
    parser.add_argument('--data_schema', help='Provide data Schema for your output files')
    parser.add_argument('--data_lines', help='How many lines your output file has')
    parser.add_argument('--multiprocessing', help='The number of processes used to create files', default=5)
    parser.add_argument('--clear_path', help='Clear all files in path_to_save_files that match file_name', action='store_true')
    args = parser.parse_args()

    return args


def existing_dir(prospective_dir):
    if prospective_dir == ".":
        prospective_dir = os. getcwd()
        logging.debug(f"You are in current directory. Path : {prospective_dir}")
        return prospective_dir
    elif os.path.isfile(prospective_dir):
        return prospective_dir
    elif os.path.isdir(prospective_dir):
        return prospective_dir
    else:
        logging.critical(f"Wrong path. Can't continue")


def init_logger():
    """
    Here we will put potential
    settings for the parser
    :return:
    """
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s | %(levelname)s | %(pathname)s | %(message)s')
    logging.getLogger('faker').setLevel(logging.ERROR)
    return None


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
        logging.critical("You can't proccess with {} number of lines".format(lines))


def create_output_file(f_line, d_schema, path, f_name):
    path_to_file = existing_dir(path)
    new_file_with_dir = os.path.join(path_to_file, f_name)
    lines = int(f_line)
    with open(new_file_with_dir, "w") as f:
        list_ = []
        for i in range(lines):
            data = str(create_fake_dict(d_schema))
            list_.append(data)
        json.dump(list_, f)
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

#TODO: add argparse for this function


def main():
    """
    Having main helps organize code,
    we can see where main routine happens
    We can clearly see the steps
    :return:
    """
    print("Hello from main!")
    init_logger()
    parsed_args = init_arg_parser()
    logging.info(parsed_args)

    logging.info(f'Current path : {parsed_args.path_to_save_files}')
    logging.info(f'You choose to generate {parsed_args.files_count} files')
    logging.debug(f'Name of your files is {parsed_args.file_name} with prefixes {parsed_args.file_prefix}. '
                  f'Every file have {parsed_args.data_lines} lines')

    if parsed_args.path_to_save_files == ".":
        path = os.getcwd()
        logging.debug(f"You are in current directory. Path : {path}")
    else:
        path = existing_dir(parsed_args.path_to_save_files)
        logging.debug(f"Path : {path}")

    if parsed_args.path_to_save_files is None and parsed_args.files_count is not None:
        logging.info("You didn't choose the path dir, so path is current file ")

    if int(parsed_args.files_count) > 0 and (parsed_args.file_name, parsed_args.file_prefix, parsed_args.path_to_save_files, parsed_args.data_lines, parsed_args.data_schema) is not None:
        logging.debug(f'The number of processes used to create files is {parsed_args.multiprocessing}')
        files = construct_files(parsed_args.file_name, parsed_args.file_prefix, parsed_args.files_count)

        with ThreadPoolExecutor(max_workers=int(parsed_args.multiprocessing)) as executor:
            futures = [executor.submit(create_output_file, parsed_args.data_lines, parsed_args.data_schema, parsed_args.path_to_save_files, file) for file in files]
        logging.info(f"All files created. Created {len(futures)} files")

    if int(parsed_args.files_count) == 0 and (parsed_args.data_lines, parsed_args.data_schema) is not None:
        logging.info("You choose to generate 0 files, so result is printed without output file, nor file_name, file_prefix or path_to_save_files won't needed")
        lines = int(parsed_args.data_lines)
        create_data_without_output_file(lines, parsed_args.data_schema)
    if int(parsed_args.files_count) < 0:
        logging.error("Incorrect value!!! There is no possibility to generate {}. Put positive number or zero to "
                      "generate answer without output files".format(parsed_args.files_count))

    if parsed_args.file_name is not None and parsed_args.file_prefix is not None and int(parsed_args.files_count) > 0 and int(parsed_args.data_lines) > 0 and parsed_args.data_schema is not None:
        logging.info(f"You generated {parsed_args.files_count} file with {parsed_args.data_lines} lines named: {parsed_args.file_name} with prefix {parsed_args.file_prefix} method")


if __name__ == '__main__':
    main()

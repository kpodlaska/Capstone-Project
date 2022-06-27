"""Hope for the best but plan for the worst"""

import argparse
import json
import glob
import logging
import os
import uuid
import random
from string import ascii_lowercase

import creating_fake_data
from concurrent.futures import  ThreadPoolExecutor


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
    parser.add_argument('--clear_path',
                        help='If this flag is on, before the script starts creating new data files, all files in '
                             'path_to_save_files that match file_name will be deleted.')
    parser.add_argument('--multiprocessing', help='The number of processes used to create files', default=5)
    parser.add_argument('--clear_path', help='Clear all files in path_to_save_files that match file_name', action="store_true")
    args = parser.parse_args()

    return args

def existing_dir(prospective_dir):
    """Chech if path existing (files or directory"""
    if os.path.isfile(prospective_dir):
        logging.info(f"file {prospective_dir}) exists")
        return prospective_dir
    elif os.path.isdir(prospective_dir):
        logging.info(f"directory {prospective_dir}) exists")
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
    ext="json"
    prefixes = []
    if prefix == "count":
        for n in range(how_many_files):
            prefixes.append(str(n+1))
    elif prefix == "random":
        for n in range(how_many_files):
            number=random.randint(1,1_000_000_000_000)
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


def create_data_without_output_file(lines, d_schema):
    if lines > 0:
        for i in range(lines):
            data = creating_fake_data.create_fake_dict(d_schema)
            print(f"{data}")
    else:
        logging.critical("You can't proccess with {} number of lines".format(lines))

def create_output_files(f_line, d_schema, path, f_name, f_prefix, f_number):
    new_files = construct_files(f_name, f_prefix, f_number)
    lines = int(f_line)
    for new_file in new_files:
        path_to_file = existing_dir(path)
        new_file_with_dir = os.path.join(path_to_file, new_file)
        with open(new_file_with_dir, "w") as f:
            for i in range(lines):
                data = creating_fake_data.create_fake_dict(d_schema)
                json.dump(data, f)
            return new_file_with_dir

def create_output_file(f_line, d_schema, path, f_name):
    path_to_file = existing_dir(path)
    new_file_with_dir = os.path.join(path_to_file, f_name)
    lines=int(f_line)
    with open(new_file_with_dir, "w") as f:
        list_ = []
        for i in range(lines):
            data = str(creating_fake_data.create_fake_dict(d_schema))
            list_.append(data)
        json.dump(list_, f)
        return new_file_with_dir

def clear_files_in_path(path, file_name):
    main.existing_dir(path)
    files = os.listdir(path)
    result=[]
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
    if existing_dir(parsed_args.path_to_save_files):
        pass
    else:
        logging.info("Directory doesn't exist!")

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

        with ThreadPoolExecutor(max_workers=parsed_args.multiprocessing) as executor:
            futures = [executor.submit(create_output_file, parsed_args.data_lines, parsed_args.data_schema, parsed_args.path_to_save_files, file) for file in files]
       # create_output_file(parsed_args.data_lines, parsed_args.data_schema, parsed_args.path_to_save_files,
        #                   parsed_args.file_name, parsed_args.file_prefix, parsed_args.files_count)

    if int(parsed_args.files_count) == 0 and (parsed_args.data_lines, parsed_args.data_schema) is not None:
        logging.info("You choose to generate 0 files, so result is printed without output file, nor file_name, file_prefix or path_to_save_files won't needed")
        lines = int(parsed_args.data_lines)
        create_data_without_output_file(lines,parsed_args.data_schema)
            #TODO: I used print in create_data_without_output_file, can stay that way?
    if int(parsed_args.files_count) < 0:
        logging.error("Incorrect value!!! There is no possibility to genereate {}. Put positive number or zero to "
                      "generate answer without output files".format(parsed_args.files_count))

    if parsed_args.file_name is not None and parsed_args.file_prefix is not None and int(parsed_args.files_count) > 0 and int(parsed_args.data_lines) > 0 and parsed_args.data_schema is not None:
        logging.info(f"You choose to generate {parsed_args.files_count} file with {parsed_args.data_lines} lines named: {parsed_args.file_name} with prefix {parsed_args.file_prefix} method")


if __name__ == '__main__':

    main()

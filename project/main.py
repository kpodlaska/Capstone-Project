"""Hope for the best but plan for the worst"""
import argparse
import configparser
import logging
import os
import utils

from concurrent.futures import ThreadPoolExecutor
from creating_config_file import create_config_ini

DEFAULT_VALUES = "default.ini"


def init_arg_parser():
    parser = argparse.ArgumentParser(prog='magicgenerator')
    config = configparser.ConfigParser()
    config.read(DEFAULT_VALUES)
    parser.add_argument('--path_to_save_files',
                        help="Define a path to output file. For current path use '.',"
                             " As default is ./Users/kpodlaska/PycharmProjects/pythonProject/Capstone",
                        type=str,
                        default=config["DEFAULT"]["path_to_save_files"])
    parser.add_argument('--files_count',
                        help="Define how many json file do you want to generate. Default value is 1",
                        type=int,
                        default=config["DEFAULT"]["files_count"])
    parser.add_argument('--file_name',
                        help="Choose name to your file. Default value is fake_data_file",
                        type=str,
                        default=config["DEFAULT"]["file_name"])
    parser.add_argument('--file_prefix',
                        help="If you chose more than 1 output file please choose prefix. Default is count",
                        type=str,
                        choices=['count', 'random', 'uuid'],
                        default=config["DEFAULT"]["file_prefix"])
    parser.add_argument('--data_schema',
                        help='Provide data Schema for your output files. '
                             'Default is data_schema = {'
                             '"date": "timestamp:",'
                             '"name": "str:rand",'
                             '"type": "["client", "partner", "government"]",'
                             '"animal_type": "["cat", "dog", "monkey,"tiger"]",'
                             '"age": "int:rand(1, 90)",'
                             '"kids_number": "int:rand(1, 6)"}',
                        default=config["DEFAULT"]["data_schema"])
    parser.add_argument('--data_lines',
                        help='How many lines your output file has. Default is 100',
                        default=config["DEFAULT"]["data_lines"])
    parser.add_argument('--multiprocessing',
                        help='The number of processes used to create files. default is 5',
                        default=config["DEFAULT"]["multiprocessing"])
    parser.add_argument('--clear_path',
                        help='Clear all files in path_to_save_files that match file_name',
                        action='store_true')
    args = parser.parse_args()
    return args


def init_logger():
    """
    Here we will put potential
    settings for the parser
    :return:
    """
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s | %(levelname)s | %(pathname)s | %(message)s')
    logging.getLogger('faker').setLevel(logging.ERROR)
    return None


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
    number_of_processes = os.cpu_count()

    logging.info(f'Current path : {parsed_args.path_to_save_files}')
    logging.info(f'You choose to generate {parsed_args.files_count} files')
    logging.debug(f'Name of your files is {parsed_args.file_name} with prefixes {parsed_args.file_prefix}. '
                  f'Every file have {parsed_args.data_lines} lines')

    if parsed_args.clear_path:
        logging.info("Cleared data before generating files")

    if int(parsed_args.multiprocessing) <= 0:
        logging.error(f"You chose {parsed_args.multiprocessing} number of processes used to create files. "
                      f"Can't be less than 0")

    if int(parsed_args.files_count) > 0:
        logging.debug(f'The number of processes used to create files is {parsed_args.multiprocessing}')
        files = utils.construct_files(parsed_args.file_name, parsed_args.file_prefix, parsed_args.files_count)
        workers_number = int(parsed_args.multiprocessing)
        if workers_number > number_of_processes:
            logging.info(f"Value of multiprocessing is higher than CPUs in the system. "
                         f"Max CPU {number_of_processes} used instead")
            workers_number = number_of_processes
        with ThreadPoolExecutor(max_workers=workers_number) as executor:
            futures = [executor.submit(utils.create_output_file, parsed_args.data_lines, parsed_args.data_schema,
                                       parsed_args.path_to_save_files, file) for file in files]
        logging.info(f"All files created. Created {len(futures)} files")

    if int(parsed_args.files_count) == 0:
        logging.info("You choose to generate 0 files, so result is printed without output file, "
                     "nor file_name, file_prefix or path_to_save_files won't needed")
        lines = int(parsed_args.data_lines)
        utils.create_data_without_output_file(lines, parsed_args.data_schema)

    if int(parsed_args.files_count) < 0:
        logging.error("Incorrect value!!! There is no possibility to generate {}. Put positive number or zero to "
                      "generate answer without output files".format(parsed_args.files_count))

    if int(parsed_args.files_count) > 0 and int(parsed_args.data_lines) > 0:
        logging.info(f"You generated {parsed_args.files_count} file with {parsed_args.data_lines} lines named: "
                     f"{parsed_args.file_name} with prefix {parsed_args.file_prefix} method")


if __name__ == '__main__':
    create_config_ini()
    main()

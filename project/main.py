"""Hope for the best but plan for the worst"""
import configparser
import argparse
import os
import utils
from concurrent.futures import ThreadPoolExecutor

import logging


def init_arg_parser():
    parser = argparse.ArgumentParser(prog='magicgenerator')
    config = configparser.ConfigParser()
    config.read("/Users/kpodlaska/PycharmProjects/pythonProject/Capstone/project/default.ini")
    parser.add_argument('--path_to_save_files',
                        help="Define a path to output file. For current path use '.', As default is ./Users/kpodlaska/PycharmProjects/pythonProject/Capstone",
                        type=str,
                        default=config["DEFAULT"]["path_to_save_files"])
    parser.add_argument('--files_count', help="Define how many json file do you want to generate. Default value is 1", type=int, default=config["DEFAULT"]["files_count"])
    parser.add_argument('--file_name', help="Choose name to your file. Default value is fake_data_file", type=str, default=config["DEFAULT"]["file_name"])
    parser.add_argument('--file_prefix', help="If you chose more than 1 output file please choose prefix. Default is count", type=str,
                        choices=['count', 'random', 'uuid'], default=config["DEFAULT"]["file_prefix"])
    parser.add_argument('--data_schema', help='Provide data Schema for your output files. Default is data_schema = {"date": "timestamp:","name": "str:rand","type": "["client", "partner", "government"]","animal_type": "["cat", "dog", "monkey,"tiger"]","age": "int:rand(1, 90)","kids_number": "int:rand(1, 6)"}',
 default=config["DEFAULT"]["data_schema"])
    parser.add_argument('--data_lines', help='How many lines your output file has. Default is 100', default=config["DEFAULT"]["data_lines"])
    parser.add_argument('--multiprocessing', help='The number of processes used to create files. default is 5',default=config["DEFAULT"]["multiprocessing"] )
    parser.add_argument('--clear_path', help='Clear all files in path_to_save_files that match file_name', action='store_true')
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

    if parsed_args.path_to_save_files == ".":
        path = os.getcwd()
        logging.debug(f"You are in current directory. Path : {path}")
    else:
        path = utils.existing_dir(parsed_args.path_to_save_files)
        logging.debug(f"Path : {path}")

    if parsed_args.clear_path and parsed_args.path_to_save_files and parsed_args.file_name:
        logging.info("You decide to clear path before work")
        utils.clear_files_in_path(parsed_args.path_to_save_files, parsed_args.file_name)

    if parsed_args.clear_path:
        logging.info("Cleared data before generating files")

    if int(parsed_args.multiprocessing) <= 0:
        logging.error(f"You chose {parsed_args.multiprocessing} number of processes used to create files. Can't be less than 0")

    if parsed_args.path_to_save_files is None and parsed_args.files_count is not None:
        logging.info("You didn't choose the path dir, so path is current file ")

    if int(parsed_args.files_count) > 0 and (parsed_args.file_name, parsed_args.file_prefix, parsed_args.path_to_save_files, parsed_args.data_lines, parsed_args.data_schema) is not None:
        logging.debug(f'The number of processes used to create files is {parsed_args.multiprocessing}')
        files = utils.construct_files(parsed_args.file_name, parsed_args.file_prefix, parsed_args.files_count)
        workers_number = int(parsed_args.multiprocessing)
        if workers_number > number_of_processes:
            logging.info(f"Value of multiprocessing is higher than CPUs in the system. max CPU {number_of_processes} used instead")
            workers_number = number_of_processes
        with ThreadPoolExecutor(max_workers=workers_number) as executor:
            futures = [executor.submit(utils.create_output_file, parsed_args.data_lines, parsed_args.data_schema, parsed_args.path_to_save_files, file) for file in files]
        logging.info(f"All files created. Created {len(futures)} files")

    if int(parsed_args.files_count) == 0 and (parsed_args.data_lines, parsed_args.data_schema) is not None:
        logging.info("You choose to generate 0 files, so result is printed without output file, nor file_name, file_prefix or path_to_save_files won't needed")
        lines = int(parsed_args.data_lines)
        utils.create_data_without_output_file(lines, parsed_args.data_schema)
    if int(parsed_args.files_count) < 0:
        logging.error("Incorrect value!!! There is no possibility to generate {}. Put positive number or zero to "
                      "generate answer without output files".format(parsed_args.files_count))

    if parsed_args.file_name is not None and parsed_args.file_prefix is not None and int(parsed_args.files_count) > 0 and int(parsed_args.data_lines) > 0 and parsed_args.data_schema is not None:
        logging.info(f"You generated {parsed_args.files_count} file with {parsed_args.data_lines} lines named: {parsed_args.file_name} with prefix {parsed_args.file_prefix} method")


if __name__ == '__main__':
    main()

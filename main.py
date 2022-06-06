"""Hope for the best but plan for the worst"""
import logging
import argparse
import configparser
import uuid
import os


def init_arg_parser():
    parser = argparse.ArgumentParser(prog='magicgenerator')

    parser.add_argument('--path_to_save_files',
                        help="Define a path to output file. For current path use '.', As deflaut is ./Capstone",
                        type=str,
                        default="/Capstone")
    parser.add_argument('--files_count', help="Define how many json file do you want to generate", type=int)
    parser.add_argument('--file_name', help="Choose name to your file", type=str)
    parser.add_argument('--file_prefix', help="If you chose more than 1 output file please choose prefix", type=str,
                        choices=['count', 'random', 'uuid'])
    parser.add_argument('--data_schema', help='Provide data Schema for your output files')
    parser.add_argument('--data_lines', help='How many lines your output file has')
    parser.add_argument('--clear_path',
                        help='If this flag is on, before the script starts creating new data files, all files in '
                             'path_to_save_files that match file_name will be deleted.')
    parser.add_argument('--multiprocessing', help='The number of processes used to create files')

    args = parser.parse_args()

    return args




"""
config = configparser.ConfigParser()
config['DEFAULT'] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                      'CompressionLevel': '9'}
config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}

topsecret = config['topsecret.server.com']
topsecret['Port'] = '50022'     # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'
with open('example.ini', 'w') as configfile:
    config.write(configfile)

print('If you read this line it means that you have provided '
      'all the parameters')"""


def init_logger():
    """
    Here we will put potential
    settings for the parser
    :return:
    """
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s | %(levelname)s | %(pathname)s | %(message)s')
    return None

def construct_files(file_name, prefix):
    ext="json"
    parsed_args = init_arg_parser()
    file_name=parsed_args.file_name
    how_many_files=parsed_args.files_count
    prefixes=[]
    if prefix="count":
        for n in range(how_many_files):
            prefixes.append(str(n+1))
    if prefix="random":
        i = 0
        while i < how_many_files:
            number = random.randint(1, maksliczba)
            if prefixes.count(liczba) == 0:
                prefixes.append(number)
                i = i + 1
    if prefix="uuid":
        for i in range(4):
            x_i = uuid.uuid4()
            prefixes.append(x_i)
    # I get list of prefixes




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
    if existing_dir("/Capstone"):
        logging.info("Correct path to folder")
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

    # # # cos tu nie dziala
    #
    counter = 0
    if parsed_args.files_count:
        if parsed_args.files_count < 0:
            logging.error("Incorrect value!!! There is no possibility to genereate {}. Put positive number or zero to "
                          "generate answer without output files".format(parsed_args.files_count))
        elif parsed_args.files_count == 0:
            logging.debug("Generate result:")  # What you want to do here? -Print result without creating JSON file
        elif parsed_args.files_count > 0:
            logging.info("Generate {} files. Here is the result".format(parsed_args.files_count))
            counter = parsed_args.files_count

    if parsed_args.file_name and parsed_args.file_prefix == "-count":
        logging.info("Creating multiple files with count method prefix")

    # if args.file_name and args.file_prefix == "--random":
    #     print("Creating multiple files with random method prefix")
    #
    # if args.file_name and args.file_prefix == "--uuid":
    #     print("Creating multiple files with uuid method prefix")


if __name__ == '__main__':
    main()

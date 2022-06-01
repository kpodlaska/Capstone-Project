"""Hope for the best but plan for the worst"""
import logging
import argparse
import configparser
import uuid
import os
parser = argparse.ArgumentParser(prog='magicgenerator')
"zdefiniujmy typ readabe dla path_to_save_file - sprawdzimy czy istnieje, jesli nie wyrzucimy error +rowniez w loggach"
def existing_file(prospective_dir):
    isdir = os.path.isdir(path_to_save_files)
    """Jak to poprawic bo odwoluje sie sama do siebie """
    try:
        isdir
        return prospective_dir
    except TypeError:
        print("Check the path one more time")
        logging.critical("DIR not exsist!!")


parser.add_argument('--path_to_save_files', help="Define a path to output file. For current path use '.', As deflaut is ./Capstone", type=str, default="/Capstone")
parser.add_argument('--files_count', help="Define how many json file do you want to generate", type=int)
parser.add_argument('--file_name', help="Choose name to your file", type=str)
parser.add_argument('--file_prefix', help="If you chose more than 1 output file please choose prefix", type=str,
                    choices=['-count','-random', '-uuid'])
parser.add_argument('--data_schema', help='Provide data Schema for your output files')
parser.add_argument('--data_lines', help='How many lines your output file has')
parser.add_argument('--clear_path', help='If this flag is on, before the script starts creating new data files, all files in path_to_save_files that match file_name will be deleted.')
parser.add_argument('--multiprocessing', help='The number of processes used to create files')
args = parser.parse_args()
a=args.path_to_save_files
print(a)
if args.path_to_save_files:

    print("Jesteś w pliku bieżącym")

if args.files_count < 0:
    print("Incorrect value")
    logging.error("There is no possibility to genereate those number of files. Put positive number or zero to generate answear without output files")
if args.files_count == 0:
    print("Result:")
if args.files > 0:
    print("tu dopisz resztę programu dla wyniku więcej niz 0")
    counter=args.files

if args.file_name and args.file_prefix=="-count":
    print("Creating multiple files with count method prefix")


if args.file_name and args.file_prefix=="--random":
    print("Creating multiple files with random method prefix")

if args.file_name and args.file_prefix=="--uuid":
    print("Creating multiple files with uuid method prefix")

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
      'all the parameters')

logging.basicConfig(filename="log.log",
                    level=logging.INFO,
                    filemode="w", format='%(asctime)s %(message)s')

logging.debug("Debug")
logging.info("Info")
logging.warning("Warning")
logging.error("Error")
logging.critical("Critical")

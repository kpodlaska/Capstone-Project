"""Hope for the best but plan for the worst"""
import logging
import argparse
import configparser
import uuid
import os

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s | %(levelname)s | %(pathname)s | %(message)s')
parser = argparse.ArgumentParser(prog='magicgenerator')


parser.add_argument('--path_to_save_files', help="Define a path to output file. For current path use '.', As deflaut is ./Capstone", type=str, default="/Capstone")
parser.add_argument('--files_count', help="Define how many json file do you want to generate", type=int)
parser.add_argument('--file_name', help="Choose name to your file", type=str)
parser.add_argument('--file_prefix', help="If you chose more than 1 output file please choose prefix", type=str,
                    choices=['count','random', 'uuid'])
parser.add_argument('--data_schema', help='Provide data Schema for your output files')
parser.add_argument('--data_lines', help='How many lines your output file has')
parser.add_argument('--clear_path', help='If this flag is on, before the script starts creating new data files, all files in path_to_save_files that match file_name will be deleted.')
parser.add_argument('--multiprocessing', help='The number of processes used to create files')
args = parser.parse_args()

logging.info('Current path : {}'.format(args.path_to_save_files))
logging.info('You choose to generate {} files'.format(args.files_count))
logging.debug('Name of your files is {} with prefixes {}. Every file have {} lines'.format(args.file_name,args.file_prefix,args.data_lines))


def existing_dir(prospective_dir):
    isdir = os.path.isdir(args.path_to_save_files)
    try:
        isdir
        return prospective_dir
    except TypeError:
        print("Check the path one more time")
        logging.critical("DIR not exsist!!")





if args.path_to_save_files==".":
    path = os.getcwd()
    logging.debug("You are in current directory. Path :".format(path))
else:
    path=existing_dir(args.path_to_save_files)
    logging.debug("Path :", format(path))


if args.files_count < 0:
    logging.error("Incorrect value!!! There is no possibility to genereate {}. Put positive number or zero to generate answear without output files".forma(args.files_count))
if args.files_count == 0:
    logging.debug("Generate result:")
if args.files_count > 0:
    logging.info("Generate {} files. Here is the result".format(args.files_count))
    counter=args.files_count

if args.file_name and args.file_prefix=="-count":
    print("Creating multiple files with count method prefix")

if args.file_name and args.file_prefix=="--random":
    print("Creating multiple files with random method prefix")

if args.file_name and args.file_prefix=="--uuid":
    print("Creating multiple files with uuid method prefix")



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
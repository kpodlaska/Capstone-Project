import logging
import json
import os
import creating_config_file
import unittest
import main
import glob
import random
import re

def clear_files_in_path(path, file_name):
    main.existing_dir(path)
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
    clear_files_in_path("/Users/kpodlaska/Desktop", "grzybek")
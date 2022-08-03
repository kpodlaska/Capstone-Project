import json
import pytest
from project.utils import create_fake_dict, create_output_file, existing_dir, clear_files_in_path, construct_files
import os

DATA_SCHEMA = "{\"date\": \"timestamp:\",\"name\": \"str:rand\",\"type\": \"['client', 'partner', 'government']\"," \
                  "\"animal_type\": \"['cat', 'dog', 'monkey','tiger']\",\"age\": \"int:rand(1, 90)\",\"kids_number\": " \
                  "\"int:rand(1, 6)\"} "
ABSOLUTE_PATH = os.path.dirname(os.path.abspath("main.py"))
PATH = os.path.join(ABSOLUTE_PATH, "results")
FILE_NAME = "magic_file_generator.json"
GIVEN_PREFIX = "count"
DEFAULT_FILE_LINES = 5
TESTED_FILE_NUMBER = 10

def count_files_in_path(path, file_name):
    existing_dir(path)
    "check if path exists"
    files = os.listdir(path)
    result = []
    for file in files:
        if file.endswith("json"):
            if file_name in file:
                result.append(file)
    return len(result)

def validateJsonText(jsonText):
    try:
        json.loads(jsonText)
    except ValueError as err:
        print(err)
        return False
    return True


def test_dict_len_matches_key_number():
    dict_given = create_fake_dict(DATA_SCHEMA)
    dict_values = dict_given.values()
    dict_keys = dict_given.keys()
    assert len(dict_values) == len(dict_keys)

def test_write_to_file():
    f_line_given = 1
    file_given = create_output_file(f_line_given, DATA_SCHEMA, PATH, FILE_NAME)
    print(file_given)
    with open(file_given) as file:
        lines = json.load(file)
    assert bool(lines) == True

lines_of_data = [(1), (2),(4), (7), (10), (19), (32)]

@pytest.mark.parametrize("f_line_given", lines_of_data)
def test_add_lines_to_file(f_line_given):
    file_given = create_output_file(f_line_given, DATA_SCHEMA, PATH, FILE_NAME)
    list_of_rows = [json.loads(line) for line in open(file_given, 'r')]
    """clear data after getting result"""
    clear_files_in_path(PATH, FILE_NAME)
    assert len(list_of_rows) == f_line_given


data = [(1), (2),(4), (7), (20)]

@pytest.mark.parametrize("expected_value", data)
def test_created_number_of_files(expected_value):
    files = construct_files(FILE_NAME, GIVEN_PREFIX, expected_value)
    """clear data before test"""
    clear_files_in_path(PATH, FILE_NAME)
    for file in files:
        create_output_file(DEFAULT_FILE_LINES, DATA_SCHEMA, PATH, file)
    assert count_files_in_path(PATH, FILE_NAME) == expected_value



def test_clear_path():
    """create output file"""
    create_output_file(DEFAULT_FILE_LINES, DATA_SCHEMA, PATH, FILE_NAME)
    if count_files_in_path(PATH, FILE_NAME) > 0:
        clear_files_in_path(PATH, FILE_NAME)
        assert count_files_in_path(PATH, FILE_NAME) == 0
    else:
        assert False == True

def test_data_schema_is_json_format():
    assert validateJsonText(DATA_SCHEMA) == True


def test_save_file_on_disc():
    """clear data before test"""
    clear_files_in_path(PATH, FILE_NAME)
    create_output_file(DEFAULT_FILE_LINES, DATA_SCHEMA, PATH, FILE_NAME)
    assert count_files_in_path(PATH, FILE_NAME) == 1


testdata = [("{\"age\": \"int:rand(1:90)\"} ", True),("{\"kids_number\": \"int:rand(1:6)\"} ",True), ("{\"favourite_number\": \"int\"} ",True)]

@pytest.mark.parametrize("a, expected", testdata)
def test_is_digit(a, expected):
    values = list(create_fake_dict(a).values())
    given = values[0]
    assert (int(given)/1).is_integer() == expected


test_schema = [("{\"date\": \"timestamp:\",\"name\": \"str:rand\",\"type\": \"['client', 'partner', 'government']\",\"age\": \"int:rand(1, 90)\"} ", True), ("{name: str:rand}", False), ("I'm not json format", False)]

@pytest.mark.parametrize("given, expected", test_schema)
def test_data_schema_is_json_format(given, expected):
    assert validateJsonText(given) == expected





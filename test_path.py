import json
import pytest
import main
import os

@staticmethod
def validateJsonText(jsonText):
    try:
        json.loads(jsonText)
    except ValueError as err:
        print(err)
        return False
    return True


def test_dict_len_matches_key_number():
    data_schema = "{\"date\": \"timestamp:\",\"name\": \"str:rand\",\"type\": \"['client', 'partner', 'government']\"," \
                  "\"animal_type\": \"['cat', 'dog', 'monkey','tiger']\",\"age\": \"int:rand(1, 90)\",\"kids_number\": " \
                  "\"int:rand(1, 6)\"} "
    dict_given = main.create_fake_dict(data_schema)
    dict_values = dict_given.values()
    dict_keys = dict_given.keys()
    assert len(dict_values) == len(dict_keys)

def test_add_lines_to_file():
    file_name = "magic_file_generator.json"
    d_schema = "{\"date\": \"timestamp:\"} "
    path = "/Users/kpodlaska/Desktop"
    f_line_given = 10
    file_given = main.create_output_file(f_line_given, d_schema, path, file_name)
    print(file_given)
    f = open(file_given)
    data = json.load(f)
    f.close()
    assert f_line_given == len(data)

@staticmethod
def count_files_in_path(path, file_name):
    main.existing_dir(path)
    "check if path exists"
    files = os.listdir(path)
    result = []
    for file in files:
        if file.endswith("json"):
            if file_name in file:
                result.append(file)
    return len(result)



def test_creating_number_of_files():
    expected_value = 1
    d_schema = "{\"date\": \"timestamp:\"} "
    f_name = "test_file_for_testing_path.json"
    path= "/Users/kpodlaska/Desktop"
    cleaning_before_testing = main.clear_files_in_path(path, f_name)
    main.create_output_file(20, d_schema, path, f_name)
    assert count_files_in_path(path, f_name) == expected_value



def test_clear_path():
        how_many_files = 5
        f_line = 1
        d_schema = "{\"date\": \"timestamp:\"} "
        f_name = "test_file_for_testing_path.json"
        prefix="count"
        path = "/Users/kpodlaska/Desktop"
        cleaning_before_testing = main.clear_files_in_path(path,f_name)

        files = main.construct_files(f_name,prefix, how_many_files)
        for file in files:
            created_file = main.create_output_file(f_line,d_schema,path,file)
        assert count_files_in_path(path, f_name) == how_many_files


def test_data_schema_is_json_format(self):
    data_schema = "{\"date\": \"timestamp:\",\"name\": \"str:rand\",\"type\": \"['client', 'partner', 'government']\"," \
                  "\"animal_type\": \"['cat', 'dog', 'monkey','tiger']\",\"age\": \"int:rand(1, 90)\",\"kids_number\": " \
                  "\"int:rand(1, 6)\"} "
    assert validateJsonText(data_schema) == True



def test_save_file_on_disc():
        pass


testdata = [("{\"age\": \"int:rand(1:90)\"} ", True),("{\"kids_number\": \"int:rand(1:6)\"} ",True), ("{\"favourite_number\": \"int\"} ",True)]

@pytest.mark.parametrize("a, expected", testdata)
def test_is_digit(a, expected):
    values = list(main.create_fake_dict(a).values())
    given = values[0]
    assert (int(given)/1).is_integer() == expected


test_schema = [("{\"date\": \"timestamp:\",\"name\": \"str:rand\",\"type\": \"['client', 'partner', 'government']\",\"age\": \"int:rand(1, 90)\"} ", True), ("{name: str:rand}", False), ("I'm not json format", False)]

@pytest.mark.parametrize("given, expected", test_schema)
def test_data_schema_is_json_format(given, expected):
    assert validateJsonText(given) == expected

if __name__ == '__main__':
    main()

